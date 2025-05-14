load "data/becas.csv";
filter column "universidad" > "finalizada";
filter column "universidad" < "Ingeniería";
aggregate count column "monto_beca";
aggregate sum column "promedio_estudiante";
aggregate sum column "monto_beca";
print;