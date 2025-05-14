lexer grammar BecasLexer;

LOAD: 'load';
FILTER: 'filter';
COLUMN: 'column';
AGGREGATE: 'aggregate';
COUNT: 'count';
SUM: 'sum';
AVERAGE: 'average';
BETWEEN: 'between';
PRINT: 'print';
AND: 'AND';
OR: 'OR';

GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQ: '==';
NEQ: '!=';

STRING: '"' (~["\r\n])* '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;

SEMICOLON: ';';
WS: [ \t\r\n]+ -> skip;
