load "data/becas.csv";
filter column "monto_beca" != 1335610;
filter column "monto_beca" >= 1276935;
aggregate sum column "monto_beca";
aggregate count column "promedio_estudiante";
print;