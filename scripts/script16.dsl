load "data/becas.csv";
filter column "tipo_beca" != "finalizada";
aggregate count column "promedio_estudiante";
aggregate sum column "monto_beca";
aggregate average column "promedio_estudiante";
print;