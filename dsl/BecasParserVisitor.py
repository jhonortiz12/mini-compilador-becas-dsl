# Generated from BecasParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BecasParser import BecasParser
else:
    from BecasParser import BecasParser

# This class defines a complete generic visitor for a parse tree produced by BecasParser.

class BecasParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BecasParser#program.
    def visitProgram(self, ctx:BecasParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#instruction.
    def visitInstruction(self, ctx:BecasParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#loadInstruction.
    def visitLoadInstruction(self, ctx:BecasParser.LoadInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#filterInstruction.
    def visitFilterInstruction(self, ctx:BecasParser.FilterInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#SimpleExpr.
    def visitSimpleExpr(self, ctx:BecasParser.SimpleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#AndExpr.
    def visitAndExpr(self, ctx:BecasParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#OrExpr.
    def visitOrExpr(self, ctx:BecasParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#aggregateInstruction.
    def visitAggregateInstruction(self, ctx:BecasParser.AggregateInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#printInstruction.
    def visitPrintInstruction(self, ctx:BecasParser.PrintInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#operator.
    def visitOperator(self, ctx:BecasParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#value.
    def visitValue(self, ctx:BecasParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BecasParser#aggregateFunc.
    def visitAggregateFunc(self, ctx:BecasParser.AggregateFuncContext):
        return self.visitChildren(ctx)



del BecasParser