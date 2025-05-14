load "data/becas.csv";
filter column "universidad" > "excelencia";
filter column "tipo_beca" >= "suspendida";
aggregate sum column "promedio_estudiante";
aggregate average column "monto_beca";
print;