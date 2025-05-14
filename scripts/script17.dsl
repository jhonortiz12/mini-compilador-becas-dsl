load "data/becas.csv";
filter column "tipo_beca" > "suspendida";
aggregate sum column "monto_beca";
aggregate count column "promedio_estudiante";
aggregate between column "promedio_estudiante";
print;