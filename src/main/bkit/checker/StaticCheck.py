"""
 * @author luuvavtien
 ID: 1814315
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *
import copy


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    pass


class FloatType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float", MType([FloatType()], IntType())),
            Symbol("float_of_int", MType([IntType()], FloatType())),
            Symbol("int_of_string", MType([StringType()], IntType())),
            Symbol("string_of_int", MType([IntType()], StringType())),
            Symbol("float_of_string", MType([StringType()], FloatType())),
            Symbol("string_of_float", MType([FloatType()], StringType())),
            Symbol("bool_of_string", MType([StringType()], BoolType())),
            Symbol("string_of_bool", MType([BoolType()], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("printStr", MType([StringType()], VoidType())),
            Symbol("printStrLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def typeCheckBinary(self, lhs, rhs):
        if type(lhs) is IntType and type(rhs) is IntType:
            return IntType()
        elif type(lhs) in [FloatType, IntType] and type(rhs) in [FloatType, IntType]:
            return FloatType()
        return None

    def typeCheck(self, lhs, rhs, type_check=True):
        # type_check = true -> check assignment statement, mean no check arraytype,String type
        # In call function/ procedure, lhs is parameter in function/procedure and rhs is parameter pass
        if type(lhs) is type(rhs) and type(lhs) in [IntType, BoolType]:
            return lhs
        elif type(lhs) is FloatType and type(rhs) in [FloatType, IntType]:
            return FloatType()
        if (type_check == False):  # check parameters in function /procdure
            if type(lhs) is StringType and type(rhs) is StringType:
                return StringType()
            if type(lhs) is ArrayType and type(rhs) is ArrayType:
                if (int(lhs.lower) == int(rhs.lower)) and (int(lhs.upper) == int(rhs.upper)) and (
                        type(lhs.eleType) == type(rhs.eleType)):
                    return lhs
        return None

    def getIndex(self, lst, key):
        for x in lst:
            if key == x[0]:
                return lst.index(x)
        return None
        # def raiseRedeclared(self, kind, name, list_check, func_list):

    #     dupName = self.lookup(name.lower(), list_check, func_list)
    #     if dupName is not None:
    #         raise Redeclared(kind, name)
    #     return False

    def visitProgram(self, ast, c):
        c = []
        for x in self.global_envi:
            c.append([x.name, x.mtype.intype, x.mtype.restype])
        for x in ast.decl:
            if type(x) is VarDecl:
                self.visitVarDecl(x, c)
            if type(x) is FuncDecl:
                self.visitFuncDecl(x, c)
        flag = False
        for x in c:
            if x[0] == 'main':
                flag = True
        if flag == False:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, c):
        for x in c:
            if ast.variable.name == x[0]:
                raise Redeclared(Variable(), ast.variable.name)
        else:
            name = ast.variable.name
            typ = ast.varInit
            dimen = ast.varDimen
            # print(type(dimen),dimen,len(dimen))
            if typ is None:
                typ = Unknown()
            else:
                typ = self.visit(typ, c)
            c.append([name, dimen, typ])

    def visitFuncDecl(self, ast, c):
        for x in c:
            if ast.name.name == x[0]:
                raise Redeclared(Function(), ast.name.name)
        param = []
        local_variable = []
        flag = False
        for para in ast.param:
            for x in param:
                if para.variable.name == x[0]:
                    flag = True
                    break
            if flag == True:
                raise Redeclared(Parameter(), para.variable.name)
            self.visit(para, param)
        for x in param:
            for y in c:
                # print('x',x,'y',y)
                if x[0] == y[0]:
                    x[2] = y[2]
        for local_var in list(ast.body)[0]:
            self.visit(local_var, local_variable)
        for x in local_variable:
            for y in param:
                if x[0] == y[0]:
                    raise Redeclared(Variable(), x[0])
        env = copy.deepcopy(param)
        env += local_variable + c
        # print('Before',env)
        # print(list(ast.body[1]))
        flag = False
        ret = VoidType()
        for x in list(ast.body)[1]:
            # print(x)
            if str(x)[0:6] == 'Return':
                ret = self.visit(x, env)
            else:
                # print('-------', env)
                self.visit(x, env)
                # print('-------', env)
        # print('Middle', env)
        # print(param)
        for x in c:
            idx1 = self.getIndex(param, x[0])
            idx2 = self.getIndex(local_variable, x[0])
            # print(x, idx1, idx2)
            if idx1 is None and idx2 is None:
                # print('Infer run in',x)
                index1 = self.getIndex(env, x[0])
                index2 = self.getIndex(c, x[0])
                # print(env[index1])
                # print(c[index2])
                c[index2][2] = env[index1][2]
        # print('After',env)
        c.append([ast.name.name, param, ret])
        # print(c)

    def visitAssign(self, ast, c):
        # print('Assign run!')
        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.rhs, c)
        if type(lhs) == VoidType:
            raise TypeMismatchInStatement(ast)
        else:
            if type(lhs) == Unknown and type(rhs) == Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(lhs) == Unknown and type(rhs) != Unknown:
                index = self.getIndex(c, ast.lhs.name)
                c[index][2] = rhs
            elif type(lhs) != Unknown and type(rhs) == Unknown:
                index = self.getIndex(c, ast.rhs.name)
                c[index][2] = lhs
            elif type(lhs) != type(rhs):
                raise TypeMismatchInStatement(ast)
        # print("left", ast.lhs)
        # return None

    def visitBinaryOp(self, ast, c):
        lhs = self.visit(ast.left, c)
        rhs = self.visit(ast.right, c)
        result_type = self.typeCheckBinary(lhs, rhs)
        # print('Lhs type:', ast.left, type(lhs))
        # print('Rhs type:', ast.right, type(rhs))
        if ast.op in ['&&', '||']:
            if type(lhs) == BoolType and type(rhs) == BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['+', '-', '*', '/', '%']:
            # print(ast)
            # print(lhs, rhs)
            if type(lhs) == IntType and type(rhs) == IntType:
                return IntType()
            elif type(lhs) == IntType and type(rhs) == Unknown:
                index = self.getIndex(c, ast.right.name)
                c[index][2] = IntType()
                return IntType()
            elif type(rhs) == IntType and type(lhs) == Unknown:
                index = self.getIndex(c, ast.left.name)
                c[index][2] = IntType()
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['+.', '-.', '*.', '/.']:
            if type(lhs) == FloatType and type(rhs) == FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['==', '!=', '>', '<', '>=', '<=']:
            if type(lhs) == IntType and type(rhs) == IntType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ['=/=', '>.', '<.', '>=.', '<=.']:
            if type(lhs) == FloatType and type(rhs) == FloatType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        stm = self.visit(ast.body, c)
        if ast.op == '!':
            if type(stm) == BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '-':
            if type(stm) == IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '-.':
            if type(stm) == FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            for x in c:
                if ast.op.name == c[0]:
                    return x[2]

    def visitCallStmt(self, ast, c):
        # print('Call statement run')
        check = False
        params = []
        for x in ast.param:
            # print(x)
            params += [self.visit(x, c)]
        # print('Param:', params)
        for x in c:
            # print(ast.method.name, x[0])
            if ast.method.name == x[0]:
                check = True
                # print(ast.method)
                # if type(x[2])==MType:
                # print(params, x[1])
                if len(params) == len(x[1]):
                    for i in range(0, len(params)):
                        # print(type(params[i]), type(x[1][i][2]))
                        if type(params[i]) != type(x[1][i][2]):
                            raise TypeMismatchInStatement(ast)
                        elif type(params[i]) == Unknown and type(x[1][i][2]) == Unknown:
                            raise TypeCannotBeInferred(ast)
                else:
                    raise TypeMismatchInStatement(ast)
        if check == False:
            raise Undeclared(Function(), ast.method.name)

    def visitIf(self, ast, c):
        for x in ast.ifthenStmt:
            if type(self.visit(list(x)[0], c)) != BoolType:
                raise TypeMismatchInStatement(ast)
            for y in list(x)[1]:
                self.visit(y, c)
            for z in list(x)[2]:
                self.visit(z, c)
        for x in list(ast.elseStmt[0]):
            self.visit(x, c)
        for x in list(ast.elseStmt[1]):
            self.visit(x, c)

    def visitFor(self, ast, c):
        # env=copy.deepcopy()
        idx = self.visit(ast.idx1, c)
        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)
        if type(idx) == Unknown and type(expr1) == Unknown:
            raise TypeCannotBeInferred(ast)
        if type(idx) == Unknown and type(expr1) == IntType:
            index = self.getIndex(c, ast.idx1.name)
            c[index][2] = expr1
            idx = expr1
        elif type(idx) == IntType and type(expr1) == Unknown:
            index = self.getIndex(c, ast.expr1.name)
            c[index][2] = idx
            expr1 = idx
        # print(idx, expr1, expr2, expr3)
        if type(idx) != IntType or type(expr1) != IntType or type(expr3) != IntType:
            raise TypeMismatchInStatement(ast)
        if type(expr2) != BoolType:
            raise TypeMismatchInStatement(ast)
        for x in list(ast.loop)[0]:
            self.visit(x, c)
        for x in list(ast.loop)[1]:
            self.visit(x, c)

    def visitWhile(self, ast, c):
        env = []
        env = c.copy()
        expr = self.visit(ast.exp, env)
        if type(expr) != BoolType:
            raise TypeMismatchInStatement(ast)
        for x in list(ast.sl)[0]:
            self.visit(x, env)
        for x in list(ast.sl)[1]:
            self.visit(x, env)

    def visitDowhile(self, ast, c):
        # print('Do While run !')
        env = []
        env = c.copy()
        for x in list(ast.sl)[0]:
            # print(x)
            self.visit(x, env)
        for x in list(ast.sl)[1]:
            # print(x)
            self.visit(x, env)
        # print(c)
        expr = self.visit(ast.exp, env)
        if type(expr) != BoolType:
            raise TypeMismatchInStatement(ast)

    def visitBreak(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        if ast.expr is None:
            return VoidType()
        else:
            return self.visit(ast.expr, c)

    def visitCallExpr(self, ast, c):
        # print('Call statement run')
        check = False
        params = []
        for x in ast.param:
            # print(x)
            params += [self.visit(x, c)]
        # print('Param:', params)
        for x in c:
            # print(ast.method.name, x[0])
            if ast.method.name == x[0]:
                check = True
                # print(params, x[1])

                if len(params) == len(x[1]):
                    for i in range(0, len(params)):
                        # print(type(params[i]), type(x[1][i][2]))
                        if type(params[i]) != type(x[1][i][2]):
                            raise TypeMismatchInExpression(ast)
                        elif type(params[i]) == Unknown and type(x[1][i][2]) == Unknown:
                            raise TypeCannotBeInferred(ast)

                else:
                    raise TypeMismatchInExpression(ast)
        if check == False:
            raise Undeclared(Function(), ast.method.name)
        index = self.getIndex(ast.method, c)
        return c[index][2]

    def visitId(self, ast, c):
        check = False
        for x in c:
            if x[0] == ast.name:
                check = True
                tmp = x
                break
        if check == False:
            raise Undeclared(Identifier(), ast.name)
        else:
            # print(tmp)
            return tmp[2]

    def visitArrayLiteral(self, ast, c):
        return ArrayType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitUnknown(self, ast, c):
        return Unknown()
