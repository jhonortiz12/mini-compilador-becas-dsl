load "data/becas.csv";
filter column "promedio_estudiante" <= 4.09;
filter column "promedio_estudiante" < 4.31;
aggregate sum column "promedio_estudiante";
aggregate sum column "monto_beca";
print;