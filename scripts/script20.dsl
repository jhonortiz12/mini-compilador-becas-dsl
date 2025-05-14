load "data/becas.csv";
filter column "universidad" < "activa";
filter column "universidad" == "suspendida";
aggregate count column "promedio_estudiante";
print;