load "data/becas.csv";
filter column "estado_beca" < "suspendida";
filter column "promedio_estudiante" > 4.02;
aggregate count column "monto_beca";
aggregate count column "promedio_estudiante";
print;