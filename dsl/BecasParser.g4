parser grammar BecasParser;

options { tokenVocab=BecasLexer; }

program: instruction+ ;

instruction
    : loadInstruction
    | filterInstruction
    | aggregateInstruction
    | printInstruction
    ;

loadInstruction: LOAD STRING SEMICOLON;

filterInstruction: FILTER filterExpr SEMICOLON;

filterExpr
    : filterExpr AND filterExpr     # andExpr
    | filterExpr OR filterExpr      # orExpr
    | COLUMN STRING operator value  # baseExpr
    ;

aggregateInstruction: AGGREGATE aggregateFunc COLUMN STRING SEMICOLON;

printInstruction: PRINT SEMICOLON;

operator: GT | LT | GE | LE | EQ | NEQ;

value: STRING | NUMBER;

aggregateFunc: COUNT | SUM | AVERAGE | BETWEEN;
