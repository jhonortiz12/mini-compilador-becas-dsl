load "data/becas.csv";
filter column "promedio_estudiante" < 3.1;
filter column "universidad" < "Ingeniería";
aggregate average column "promedio_estudiante";
aggregate between column "monto_beca";
print;