load "data/becas.csv";
filter column "universidad" > "Ingeniería";
filter column "estado_beca" > "finalizada";
aggregate average column "promedio_estudiante";
aggregate average column "monto_beca";
aggregate average column "monto_beca";
print;