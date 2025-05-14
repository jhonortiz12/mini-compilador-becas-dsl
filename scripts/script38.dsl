load "data/becas.csv";
filter column "universidad" <= "excelencia";
filter column "monto_beca" < 1585958;
aggregate between column "promedio_estudiante";
aggregate count column "promedio_estudiante";
aggregate sum column "monto_beca";
print;