# Generated from BecasParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,1,
        8,10,0,2,4,6,8,10,12,14,16,18,0,3,1,0,12,17,1,0,18,19,1,0,5,8,67,
        0,21,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,35,1,0,0,0,8,39,1,0,0,0,
        10,56,1,0,0,0,12,62,1,0,0,0,14,65,1,0,0,0,16,67,1,0,0,0,18,69,1,
        0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,
        24,1,0,0,0,24,1,1,0,0,0,25,30,3,4,2,0,26,30,3,6,3,0,27,30,3,10,5,
        0,28,30,3,12,6,0,29,25,1,0,0,0,29,26,1,0,0,0,29,27,1,0,0,0,29,28,
        1,0,0,0,30,3,1,0,0,0,31,32,5,1,0,0,32,33,5,18,0,0,33,34,5,21,0,0,
        34,5,1,0,0,0,35,36,5,2,0,0,36,37,3,8,4,0,37,38,5,21,0,0,38,7,1,0,
        0,0,39,40,6,4,-1,0,40,41,5,3,0,0,41,42,5,18,0,0,42,43,3,14,7,0,43,
        44,3,16,8,0,44,53,1,0,0,0,45,46,10,3,0,0,46,47,5,10,0,0,47,52,3,
        8,4,4,48,49,10,2,0,0,49,50,5,11,0,0,50,52,3,8,4,3,51,45,1,0,0,0,
        51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,9,1,0,
        0,0,55,53,1,0,0,0,56,57,5,4,0,0,57,58,3,18,9,0,58,59,5,3,0,0,59,
        60,5,18,0,0,60,61,5,21,0,0,61,11,1,0,0,0,62,63,5,9,0,0,63,64,5,21,
        0,0,64,13,1,0,0,0,65,66,7,0,0,0,66,15,1,0,0,0,67,68,7,1,0,0,68,17,
        1,0,0,0,69,70,7,2,0,0,70,19,1,0,0,0,4,23,29,51,53
    ]

class BecasParser ( Parser ):

    grammarFileName = "BecasParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'filter'", "'column'", "'aggregate'", 
                     "'count'", "'sum'", "'average'", "'between'", "'print'", 
                     "'AND'", "'OR'", "'>'", "'<'", "'>='", "'<='", "'=='", 
                     "'!='", "<INVALID>", "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "FILTER", "COLUMN", "AGGREGATE", 
                      "COUNT", "SUM", "AVERAGE", "BETWEEN", "PRINT", "AND", 
                      "OR", "GT", "LT", "GE", "LE", "EQ", "NEQ", "STRING", 
                      "NUMBER", "ID", "SEMICOLON", "WS" ]

    RULE_program = 0
    RULE_instruction = 1
    RULE_loadInstruction = 2
    RULE_filterInstruction = 3
    RULE_filterExpr = 4
    RULE_aggregateInstruction = 5
    RULE_printInstruction = 6
    RULE_operator = 7
    RULE_value = 8
    RULE_aggregateFunc = 9

    ruleNames =  [ "program", "instruction", "loadInstruction", "filterInstruction", 
                   "filterExpr", "aggregateInstruction", "printInstruction", 
                   "operator", "value", "aggregateFunc" ]

    EOF = Token.EOF
    LOAD=1
    FILTER=2
    COLUMN=3
    AGGREGATE=4
    COUNT=5
    SUM=6
    AVERAGE=7
    BETWEEN=8
    PRINT=9
    AND=10
    OR=11
    GT=12
    LT=13
    GE=14
    LE=15
    EQ=16
    NEQ=17
    STRING=18
    NUMBER=19
    ID=20
    SEMICOLON=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BecasParser.InstructionContext)
            else:
                return self.getTypedRuleContext(BecasParser.InstructionContext,i)


        def getRuleIndex(self):
            return BecasParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BecasParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.instruction()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 534) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadInstruction(self):
            return self.getTypedRuleContext(BecasParser.LoadInstructionContext,0)


        def filterInstruction(self):
            return self.getTypedRuleContext(BecasParser.FilterInstructionContext,0)


        def aggregateInstruction(self):
            return self.getTypedRuleContext(BecasParser.AggregateInstructionContext,0)


        def printInstruction(self):
            return self.getTypedRuleContext(BecasParser.PrintInstructionContext,0)


        def getRuleIndex(self):
            return BecasParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = BecasParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.loadInstruction()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.filterInstruction()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.aggregateInstruction()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.printInstruction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(BecasParser.LOAD, 0)

        def STRING(self):
            return self.getToken(BecasParser.STRING, 0)

        def SEMICOLON(self):
            return self.getToken(BecasParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BecasParser.RULE_loadInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadInstruction" ):
                listener.enterLoadInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadInstruction" ):
                listener.exitLoadInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadInstruction" ):
                return visitor.visitLoadInstruction(self)
            else:
                return visitor.visitChildren(self)




    def loadInstruction(self):

        localctx = BecasParser.LoadInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(BecasParser.LOAD)
            self.state = 32
            self.match(BecasParser.STRING)
            self.state = 33
            self.match(BecasParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(BecasParser.FILTER, 0)

        def filterExpr(self):
            return self.getTypedRuleContext(BecasParser.FilterExprContext,0)


        def SEMICOLON(self):
            return self.getToken(BecasParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BecasParser.RULE_filterInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterInstruction" ):
                listener.enterFilterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterInstruction" ):
                listener.exitFilterInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterInstruction" ):
                return visitor.visitFilterInstruction(self)
            else:
                return visitor.visitChildren(self)




    def filterInstruction(self):

        localctx = BecasParser.FilterInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(BecasParser.FILTER)
            self.state = 36
            self.filterExpr(0)
            self.state = 37
            self.match(BecasParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BecasParser.RULE_filterExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SimpleExprContext(FilterExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BecasParser.FilterExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COLUMN(self):
            return self.getToken(BecasParser.COLUMN, 0)
        def STRING(self):
            return self.getToken(BecasParser.STRING, 0)
        def operator(self):
            return self.getTypedRuleContext(BecasParser.OperatorContext,0)

        def value(self):
            return self.getTypedRuleContext(BecasParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpr" ):
                listener.enterSimpleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpr" ):
                listener.exitSimpleExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpr" ):
                return visitor.visitSimpleExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(FilterExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BecasParser.FilterExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def filterExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BecasParser.FilterExprContext)
            else:
                return self.getTypedRuleContext(BecasParser.FilterExprContext,i)

        def AND(self):
            return self.getToken(BecasParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(FilterExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BecasParser.FilterExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def filterExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BecasParser.FilterExprContext)
            else:
                return self.getTypedRuleContext(BecasParser.FilterExprContext,i)

        def OR(self):
            return self.getToken(BecasParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def filterExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BecasParser.FilterExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_filterExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = BecasParser.SimpleExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 40
            self.match(BecasParser.COLUMN)
            self.state = 41
            self.match(BecasParser.STRING)
            self.state = 42
            self.operator()
            self.state = 43
            self.value()
            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = BecasParser.AndExprContext(self, BecasParser.FilterExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_filterExpr)
                        self.state = 45
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 46
                        self.match(BecasParser.AND)
                        self.state = 47
                        self.filterExpr(4)
                        pass

                    elif la_ == 2:
                        localctx = BecasParser.OrExprContext(self, BecasParser.FilterExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_filterExpr)
                        self.state = 48
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 49
                        self.match(BecasParser.OR)
                        self.state = 50
                        self.filterExpr(3)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AggregateInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATE(self):
            return self.getToken(BecasParser.AGGREGATE, 0)

        def aggregateFunc(self):
            return self.getTypedRuleContext(BecasParser.AggregateFuncContext,0)


        def COLUMN(self):
            return self.getToken(BecasParser.COLUMN, 0)

        def STRING(self):
            return self.getToken(BecasParser.STRING, 0)

        def SEMICOLON(self):
            return self.getToken(BecasParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BecasParser.RULE_aggregateInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateInstruction" ):
                listener.enterAggregateInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateInstruction" ):
                listener.exitAggregateInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateInstruction" ):
                return visitor.visitAggregateInstruction(self)
            else:
                return visitor.visitChildren(self)




    def aggregateInstruction(self):

        localctx = BecasParser.AggregateInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aggregateInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(BecasParser.AGGREGATE)
            self.state = 57
            self.aggregateFunc()
            self.state = 58
            self.match(BecasParser.COLUMN)
            self.state = 59
            self.match(BecasParser.STRING)
            self.state = 60
            self.match(BecasParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BecasParser.PRINT, 0)

        def SEMICOLON(self):
            return self.getToken(BecasParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BecasParser.RULE_printInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintInstruction" ):
                listener.enterPrintInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintInstruction" ):
                listener.exitPrintInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintInstruction" ):
                return visitor.visitPrintInstruction(self)
            else:
                return visitor.visitChildren(self)




    def printInstruction(self):

        localctx = BecasParser.PrintInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(BecasParser.PRINT)
            self.state = 63
            self.match(BecasParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(BecasParser.GT, 0)

        def LT(self):
            return self.getToken(BecasParser.LT, 0)

        def GE(self):
            return self.getToken(BecasParser.GE, 0)

        def LE(self):
            return self.getToken(BecasParser.LE, 0)

        def EQ(self):
            return self.getToken(BecasParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BecasParser.NEQ, 0)

        def getRuleIndex(self):
            return BecasParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = BecasParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BecasParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(BecasParser.NUMBER, 0)

        def getRuleIndex(self):
            return BecasParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = BecasParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(BecasParser.COUNT, 0)

        def SUM(self):
            return self.getToken(BecasParser.SUM, 0)

        def AVERAGE(self):
            return self.getToken(BecasParser.AVERAGE, 0)

        def BETWEEN(self):
            return self.getToken(BecasParser.BETWEEN, 0)

        def getRuleIndex(self):
            return BecasParser.RULE_aggregateFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFunc" ):
                listener.enterAggregateFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFunc" ):
                listener.exitAggregateFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFunc" ):
                return visitor.visitAggregateFunc(self)
            else:
                return visitor.visitChildren(self)




    def aggregateFunc(self):

        localctx = BecasParser.AggregateFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_aggregateFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.filterExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def filterExpr_sempred(self, localctx:FilterExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




