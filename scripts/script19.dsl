load "data/becas.csv";
filter column "universidad" >= "suspendida";
aggregate sum column "promedio_estudiante";
aggregate between column "promedio_estudiante";
aggregate sum column "monto_beca";
print;