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

// Filtro extendido para permitir expresiones booleanas con AND y OR
filterInstruction: FILTER filterExpr SEMICOLON;

filterExpr
    : filterExpr AND filterExpr      # AndExpr
    | filterExpr OR filterExpr       # OrExpr
    | COLUMN STRING operator value   # SimpleExpr
    ;

aggregateInstruction: AGGREGATE aggregateFunc COLUMN STRING SEMICOLON;

printInstruction: PRINT SEMICOLON;

operator: GT | LT | GE | LE | EQ | NEQ;

value: STRING | NUMBER;

aggregateFunc: COUNT | SUM | AVERAGE | BETWEEN;
