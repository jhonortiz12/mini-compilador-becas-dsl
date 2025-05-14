load "data/becas.csv";
filter column "monto_beca" >= 1959544;
filter column "estado_beca" == "activa";
aggregate count column "monto_beca";
aggregate count column "promedio_estudiante";
aggregate between column "monto_beca";
print;

