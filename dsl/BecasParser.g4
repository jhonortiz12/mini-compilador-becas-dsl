parser grammar BecasParser;

options { tokenVocab=BecasLexer; }

program: instruction+;

instruction
    : loadInstruction
    | filterInstruction
    | aggregateInstruction
    | printInstruction
    ;

loadInstruction: LOAD STRING SEMICOLON;

filterInstruction: FILTER COLUMN STRING operator value (logicalOperator filterInstruction)?;

aggregateInstruction: AGGREGATE aggregateFunc COLUMN STRING SEMICOLON;

printInstruction: PRINT SEMICOLON;

operator: GT | LT | GE | LE | EQ | NEQ;

value: STRING | NUMBER;

aggregateFunc: COUNT | SUM | AVERAGE | BETWEEN;

logicalOperator: AND | OR;
