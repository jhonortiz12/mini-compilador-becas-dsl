load "data/becas.csv";
filter column "promedio_estudiante" >= 3.31;
aggregate sum column "promedio_estudiante";
aggregate sum column "monto_beca";
print;