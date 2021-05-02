from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        if ctx.manydeclaration():
            return Program(ctx.manydeclaration().accept(self))
        else:
            return Program([])

    def visitManydeclaration(self, ctx: BKITParser.ManydeclarationContext):
        if ctx.manydeclaration():
            return ctx.declarations().accept(self) + ctx.manydeclaration().accept(self)
        else:
            return ctx.declarations().accept(self)

    def visitDeclarations(self, ctx: BKITParser.DeclarationsContext):
        if ctx.var_declarations():
            return ctx.var_declarations().accept(self)
        else:
            return ctx.main_statement().accept(self)

    def visitVar_declarations(self, ctx: BKITParser.Var_declarationsContext):
        return ctx.variable_list().accept(self)

    def visitVariable_list(self, ctx: BKITParser.Variable_listContext):
        if ctx.variable_list():
            return ctx.var_part().accept(self) + ctx.variable_list().accept(self)
        else:
            return ctx.var_part().accept(self)

    def visitVar_part(self, ctx: BKITParser.Var_partContext):
        if ctx.init_var():
            return ctx.init_var().accept(self)
        else:
            return ctx.un_init_var().accept(self)

    def visitUn_init_var(self, ctx: BKITParser.Un_init_varContext):
        if ctx.dimension():
            return [VarDecl(Id(ctx.ID().getText()), ctx.dimension().accept(self), None)]
        else:
            return [VarDecl(Id(ctx.ID().getText()), [], None)]

    def visitInit_var(self, ctx: BKITParser.Init_varContext):
        if ctx.normal_literals():
            return [VarDecl(Id(ctx.ID().getText()), [], ctx.normal_literals().accept(self))]
        else:
            return [VarDecl(Id(ctx.ID().getText()), ctx.dimension().accept(self), ctx.array_literal().accept(self))]

    def visitVar_name(self, ctx: BKITParser.Var_nameContext):
        if ctx.ID():
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + ctx.dimension().accept(self)

    def visitDimension(self, ctx: BKITParser.DimensionContext):
        if ctx.dimension():
            return [int(ctx.INTLIT().getText(), 0)] + ctx.dimension().accept(self)
        else:
            return [int(ctx.INTLIT().getText(), 0)]

    def visitNormal_literals(self, ctx: BKITParser.Normal_literalsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText(), 0))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        else:
            return ctx.one_array().accept(self)

    def visitMain_statement(self, ctx: BKITParser.Main_statementContext):
        if ctx.parameter_list() and ctx.var_body() and ctx.statement_lists():
            return [
                FuncDecl(Id(ctx.ID().getText()), ctx.parameter_list().accept(self),
                         (ctx.var_body().accept(self), ctx.statement_lists().accept(self)))]
        elif ctx.parameter_list():
            if ctx.var_body():
                return [
                    FuncDecl(Id(ctx.ID().getText()), ctx.parameter_list().accept(self),
                             (ctx.var_body().accept(self), []))]
            elif ctx.statement_lists():
                return [
                    FuncDecl(Id(ctx.ID().getText()), ctx.parameter_list().accept(self),
                             ([], ctx.statement_lists().accept(self)))]
            else:
                return [
                    FuncDecl(Id(ctx.ID().getText()), ctx.parameter_list().accept(self),
                             [[], []])]
        elif ctx.var_body():
            if ctx.statement_lists():
                return [FuncDecl(Id(ctx.ID().getText()), [],
                                 (ctx.var_body().accept(self), ctx.statement_lists().accept(self)))]
            else:
                return [FuncDecl(Id(ctx.ID().getText()), [], (ctx.var_body().accept(self), []))]
        elif ctx.statement_lists():
            return [FuncDecl(Id(ctx.ID().getText()), [], [[], ctx.statement_lists().accept(self)])]
        else:
            return [FuncDecl(Id(ctx.ID().getText()), [], [[], []])]

    def visitParameter_list(self, ctx: BKITParser.Parameter_listContext):
        if ctx.parameter_list():
            return ctx.un_init_var().accept(self) + ctx.parameter_list().accept(self)
        else:
            return ctx.un_init_var().accept(self)

    def visitVar_body(self, ctx: BKITParser.Var_bodyContext):
        if ctx.var_body():
            return ctx.var_declarations().accept(self) + ctx.var_body().accept(self)
        else:
            return ctx.var_declarations().accept(self)

    def visitStatement_lists(self, ctx: BKITParser.Statement_listsContext):
        if ctx.statement_lists():
            return ctx.statement_list().accept(self) + ctx.statement_lists().accept(self)
        else:
            return ctx.statement_list().accept(self)

    def visitStatement_list(self, ctx: BKITParser.Statement_listContext):
        if ctx.assign_statement():
            return ctx.assign_statement().accept(self)
        elif ctx.if_statement():
            return ctx.if_statement().accept(self)
        elif ctx.for_statement():
            return ctx.for_statement().accept(self)
        elif ctx.while_statement():
            return ctx.while_statement().accept(self)
        elif ctx.do_while_statement():
            return ctx.do_while_statement().accept(self)
        elif ctx.continue_statement():
            return ctx.continue_statement().accept(self)
        elif ctx.call_statement():
            return ctx.call_statement().accept(self)
        elif ctx.return_statement():
            return ctx.return_statement().accept(self)
        elif ctx.var_declarations():
            return ctx.var_declarations().accept(self)

    def visitAssign_statement(self, ctx: BKITParser.Assign_statementContext):
        return [Assign(ctx.lhs().accept(self), ctx.exp().accept(self))]

    def visitLhs(self, ctx: BKITParser.LhsContext):
        if ctx.index_expression():
            return ctx.index_expression().accept(self)
        else:
            return Id(ctx.ID().getText())

    def visitBody_part(self, ctx: BKITParser.Body_partContext):
        if ctx.var_body() and ctx.statement_lists():
            return [ctx.var_body().accept(self), ctx.statement_lists().accept(self)]
        elif ctx.var_body():
            return [ctx.var_body().accept(self), []]
        elif ctx.statement_lists():
            return [[], ctx.statement_lists().accept(self)]
        else:
            return [[], []]

    def visitIf_statement(self, ctx: BKITParser.If_statementContext):
        c = ctx.elseif_part().accept(self) if ctx.elseif_part() else []
        d = ctx.else_part().accept(self) if ctx.else_part() else [[], []]
        a = ctx.var_body().accept(self) if ctx.var_body() else []
        b = ctx.statement_lists().accept(self) if ctx.statement_lists() else []
        e = [(ctx.exp().accept(self), a,b)] + c
        return [If(e, d)]

    def visitElseif_part(self, ctx: BKITParser.Elseif_partContext):
        if ctx.elseif_part():
            a = ctx.var_body().accept(self) if ctx.var_body() else []
            b = ctx.statement_lists().accept(self) if ctx.statement_lists() else []
            return [(ctx.exp().accept(self), a, b)] + ctx.elseif_part().accept(self)
        else:
            a = ctx.var_body().accept(self) if ctx.var_body() else []
            b = ctx.statement_lists().accept(self) if ctx.statement_lists() else []
            return [(ctx.exp().accept(self), a, b)]

    def visitElse_part(self, ctx: BKITParser.Else_partContext):
        if ctx.var_body() and ctx.statement_lists():
            return [ctx.var_body().accept(self), ctx.statement_lists()]
        elif ctx.var_body():
            return [ctx.var_body().accept(self), []]
        elif ctx.statement_lists():
            return [[], ctx.statement_lists().accept(self)]
        else:
            return [[], []]

    def visitFor_statement(self, ctx: BKITParser.For_statementContext):
        a = ctx.init_exp().accept(self)
        b = ctx.condition_exp().accept(self)
        c = ctx.update_exp().accept(self)
        d = ctx.var_body().accept(self) if ctx.var_body() else []
        e = ctx.statement_lists().accept(self) if ctx.statement_lists() else []
        return [For(Id(ctx.ID().getText()), a, b, c, (d, e))]

    def visitInit_exp(self, ctx: BKITParser.Init_expContext):
        return ctx.exp().accept(self)

    def visitCondition_exp(self, ctx: BKITParser.Condition_expContext):
        return ctx.exp().accept(self)

    def visitUpdate_exp(self, ctx: BKITParser.Update_expContext):
        return ctx.exp().accept(self)

    def visitWhile_statement(self, ctx: BKITParser.While_statementContext):
        # if ctx.body_part():
        return [While(ctx.exp().accept(self), ctx.body_part().accept(self))]

    # else:
    #     return [While(ctx.exp().accept(self), [[], []])]

    def visitDo_while_statement(self, ctx: BKITParser.Do_while_statementContext):
        # if ctx.statement_list():
        return [Dowhile(ctx.body_part().accept(self), ctx.exp().accept(self))]

    # else:
    #     return [Dowhile([[], []], ctx.exp().accept(self))]

    def visitBreak_statement(self, ctx: BKITParser.Break_statementContext):
        return [Break()]

    def visitContinue_statement(self, ctx: BKITParser.Continue_statementContext):
        return [Continue()]

    def visitCall_statement(self, ctx: BKITParser.Call_statementContext):
        return ctx.function_call().accept(self)

    def visitReturn_statement(self, ctx: BKITParser.Return_statementContext):
        if ctx.exp():
            return [Return(ctx.exp().accept(self))]
        else:
            return [Return(None)]

    def visitExp(self, ctx: BKITParser.ExpContext):
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.NOTEQUALINT():
            return BinaryOp(ctx.NOTEQUALINT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESSTHANINT():
            return BinaryOp(ctx.LESSTHANINT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATERTHANINT():
            return BinaryOp(ctx.GREATERTHANINT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESSEQUALINT():
            return BinaryOp(ctx.LESSEQUALINT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATEREQUALINT():
            return BinaryOp(ctx.GREATEREQUALINT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.NOTEQUALFLOAT():
            return BinaryOp(ctx.NOTEQUALFLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESSTHANFLOAT():
            return BinaryOp(ctx.LESSTHANFLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATERTHANFLOAT():
            return BinaryOp(ctx.GREATERTHANFLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.LESSEQUALFLOAT():
            return BinaryOp(ctx.LESSEQUALFLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        elif ctx.GREATEREQUALFLOAT():
            return BinaryOp(ctx.GREATEREQUALFLOAT().getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
        else:
            return ctx.exp1(0).accept(self)

    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), ctx.exp1().accept(self), ctx.exp2().accept(self))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), ctx.exp1().accept(self), ctx.exp2().accept(self))
        else:
            return ctx.exp2().accept(self)

    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.ADDINT():
            return BinaryOp(ctx.ADDINT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        elif ctx.ADDFLOAT():
            return BinaryOp(ctx.ADDFLOAT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        elif ctx.SUBINT():
            return BinaryOp(ctx.SUBINT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        elif ctx.SUBFLOAT():
            return BinaryOp(ctx.SUBFLOAT().getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))
        else:
            return ctx.exp3().accept(self)

    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.MULINT():
            return BinaryOp(ctx.MULINT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.MULFLOAT():
            return BinaryOp(ctx.MULFLOAT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.DIVINT():
            return BinaryOp(ctx.DIVINT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.DIVFLOAT():
            return BinaryOp(ctx.DIVFLOAT().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))
        else:
            return ctx.exp4().accept(self)

    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), ctx.exp4().accept(self))
        else:
            return ctx.exp5().accept(self)

    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.SUBINT():
            return UnaryOp(ctx.SUBINT().getText(), ctx.exp5().accept(self))
        elif ctx.SUBFLOAT():
            return UnaryOp(ctx.SUBFLOAT().getText(), ctx.exp5().accept(self))
        else:
            return ctx.exp6().accept(self)

    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.literals():
            return ctx.literals().accept(self)
        elif ctx.exp():
            return ctx.exp().accept(self)
        elif ctx.index_expression():
            return ctx.index_expression().accept(self)
        elif ctx.function_call():
            return ctx.function_call().accept(self)
        else:
            return []

    def visitLiterals(self, ctx: BKITParser.LiteralsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText(), 0))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(bool(ctx.TRUE().getText()))
        elif ctx.FALSE():
            return BooleanLiteral(bool(ctx.FALSE().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        # elif ctx.array_name():
        #     return ctx.array_name().accept(self)
        else:
            return ctx.array_name().accept(self)
            # return ctx.array_literal().accept(self)

    def visitArray_name(self, ctx: BKITParser.Array_nameContext):
        return ArrayCell(Id(ctx.ID().getText()), ctx.dimen().accept(self))

    def visitDimen(self, ctx: BKITParser.DimenContext):
        if ctx.dimen():
            return [ctx.exp().accept(self)] + ctx.dimen().accept(self)
        else:
            return [ctx.exp().accept(self)]

    def visitIndex_expression(self, ctx: BKITParser.Index_expressionContext):
        return ArrayCell(ctx.index_expression_name().accept(self), ctx.index_operator().accept(self))

    def visitIndex_operator(self, ctx: BKITParser.Index_operatorContext):
        if ctx.index_operator():
            return [ctx.exp().accept(self)] + ctx.index_operator().accept(self)
        else:
            return [ctx.exp().accept(self)]

    def visitIndex_expression_name(self, ctx: BKITParser.Index_expression_nameContext):
        if ctx.function_call():
            return ctx.function_call().accept(self)
        else:
            return Id(ctx.ID().getText())

    def visitFunction_call(self, ctx: BKITParser.Function_callContext):
        if ctx.argument_list():
            return [CallStmt(Id(ctx.ID().getText()), ctx.argument_list().accept(self))]
        else:
            return [CallStmt(Id(ctx.ID().getText()), [])]

    def visitArgument_list(self, ctx: BKITParser.Argument_listContext):
        if ctx.argument_list():
            return [ctx.exp().accept(self)] + ctx.argument_list().accept(self)
        else:
            return [ctx.exp().accept(self)]

    def visitArray_literal(self, ctx: BKITParser.Array_literalContext):
        if ctx.many_array():
            return ctx.many_array().accept(self)
        elif ctx.one_array():
            return ctx.one_array().accept(self)
        else:
            return ctx.array_value().accept(self)

    def visitMany_array(self, ctx: BKITParser.Many_arrayContext):
        if ctx.many_array():
            return ctx.one_array().accept(self) + ctx.many_array().accept(self)
        else:
            return ctx.one_array().accept(self)

    def visitOne_array(self, ctx: BKITParser.One_arrayContext):
        return ctx.array_value().accept(self)

    def visitArray_value(self, ctx: BKITParser.Array_valueContext):
        # if ctx.getChildCount()==1:
        #     return ArrayLiteral([ctx.normal_literals().accept(self)])
        # else:
        return ArrayLiteral([self.visit(x) for x in ctx.normal_literals()])
