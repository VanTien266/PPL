# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#manydeclaration.
    def visitManydeclaration(self, ctx:BKITParser.ManydeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declarations.
    def visitDeclarations(self, ctx:BKITParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declarations.
    def visitVar_declarations(self, ctx:BKITParser.Var_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_list.
    def visitVariable_list(self, ctx:BKITParser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_part.
    def visitVar_part(self, ctx:BKITParser.Var_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#un_init_var.
    def visitUn_init_var(self, ctx:BKITParser.Un_init_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_var.
    def visitInit_var(self, ctx:BKITParser.Init_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_name.
    def visitVar_name(self, ctx:BKITParser.Var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#normal_literals.
    def visitNormal_literals(self, ctx:BKITParser.Normal_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#main_statement.
    def visitMain_statement(self, ctx:BKITParser.Main_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_body.
    def visitVar_body(self, ctx:BKITParser.Var_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_lists.
    def visitStatement_lists(self, ctx:BKITParser.Statement_listsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_statement.
    def visitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lhs.
    def visitLhs(self, ctx:BKITParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body_part.
    def visitBody_part(self, ctx:BKITParser.Body_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif_part.
    def visitElseif_part(self, ctx:BKITParser.Elseif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_part.
    def visitElse_part(self, ctx:BKITParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_exp.
    def visitInit_exp(self, ctx:BKITParser.Init_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#condition_exp.
    def visitCondition_exp(self, ctx:BKITParser.Condition_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#update_exp.
    def visitUpdate_exp(self, ctx:BKITParser.Update_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_name.
    def visitArray_name(self, ctx:BKITParser.Array_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimen.
    def visitDimen(self, ctx:BKITParser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_expression.
    def visitIndex_expression(self, ctx:BKITParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operator.
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_expression_name.
    def visitIndex_expression_name(self, ctx:BKITParser.Index_expression_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argument_list.
    def visitArgument_list(self, ctx:BKITParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_literal.
    def visitArray_literal(self, ctx:BKITParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_array.
    def visitMany_array(self, ctx:BKITParser.Many_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#one_array.
    def visitOne_array(self, ctx:BKITParser.One_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_value.
    def visitArray_value(self, ctx:BKITParser.Array_valueContext):
        return self.visitChildren(ctx)



del BKITParser