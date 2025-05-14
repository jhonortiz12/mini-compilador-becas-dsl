# Generated from BecasParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BecasParser import BecasParser
else:
    from BecasParser import BecasParser

# This class defines a complete listener for a parse tree produced by BecasParser.
class BecasParserListener(ParseTreeListener):

    # Enter a parse tree produced by BecasParser#program.
    def enterProgram(self, ctx:BecasParser.ProgramContext):
        pass

    # Exit a parse tree produced by BecasParser#program.
    def exitProgram(self, ctx:BecasParser.ProgramContext):
        pass


    # Enter a parse tree produced by BecasParser#instruction.
    def enterInstruction(self, ctx:BecasParser.InstructionContext):
        pass

    # Exit a parse tree produced by BecasParser#instruction.
    def exitInstruction(self, ctx:BecasParser.InstructionContext):
        pass


    # Enter a parse tree produced by BecasParser#loadInstruction.
    def enterLoadInstruction(self, ctx:BecasParser.LoadInstructionContext):
        pass

    # Exit a parse tree produced by BecasParser#loadInstruction.
    def exitLoadInstruction(self, ctx:BecasParser.LoadInstructionContext):
        pass


    # Enter a parse tree produced by BecasParser#filterInstruction.
    def enterFilterInstruction(self, ctx:BecasParser.FilterInstructionContext):
        pass

    # Exit a parse tree produced by BecasParser#filterInstruction.
    def exitFilterInstruction(self, ctx:BecasParser.FilterInstructionContext):
        pass


    # Enter a parse tree produced by BecasParser#aggregateInstruction.
    def enterAggregateInstruction(self, ctx:BecasParser.AggregateInstructionContext):
        pass

    # Exit a parse tree produced by BecasParser#aggregateInstruction.
    def exitAggregateInstruction(self, ctx:BecasParser.AggregateInstructionContext):
        pass


    # Enter a parse tree produced by BecasParser#printInstruction.
    def enterPrintInstruction(self, ctx:BecasParser.PrintInstructionContext):
        pass

    # Exit a parse tree produced by BecasParser#printInstruction.
    def exitPrintInstruction(self, ctx:BecasParser.PrintInstructionContext):
        pass


    # Enter a parse tree produced by BecasParser#operator.
    def enterOperator(self, ctx:BecasParser.OperatorContext):
        pass

    # Exit a parse tree produced by BecasParser#operator.
    def exitOperator(self, ctx:BecasParser.OperatorContext):
        pass


    # Enter a parse tree produced by BecasParser#value.
    def enterValue(self, ctx:BecasParser.ValueContext):
        pass

    # Exit a parse tree produced by BecasParser#value.
    def exitValue(self, ctx:BecasParser.ValueContext):
        pass


    # Enter a parse tree produced by BecasParser#aggregateFunc.
    def enterAggregateFunc(self, ctx:BecasParser.AggregateFuncContext):
        pass

    # Exit a parse tree produced by BecasParser#aggregateFunc.
    def exitAggregateFunc(self, ctx:BecasParser.AggregateFuncContext):
        pass


    # Enter a parse tree produced by BecasParser#logicalOperator.
    def enterLogicalOperator(self, ctx:BecasParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by BecasParser#logicalOperator.
    def exitLogicalOperator(self, ctx:BecasParser.LogicalOperatorContext):
        pass



del BecasParser