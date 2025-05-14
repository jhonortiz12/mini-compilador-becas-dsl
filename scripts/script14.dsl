load "data/becas.csv";
filter column "carrera" < "excelencia";
filter column "carrera" > "activa";
aggregate sum column "monto_beca";
aggregate between column "promedio_estudiante";
aggregate count column "promedio_estudiante";
print;