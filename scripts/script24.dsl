load "data/becas.csv";
filter column "promedio_estudiante" <= 4.31;
filter column "estado_beca" != "Ingeniería";
aggregate count column "monto_beca";
print;