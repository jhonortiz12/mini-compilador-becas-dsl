load "data/becas.csv";
filter column "carrera" > "excelencia";
filter column "promedio_estudiante" >= 4.4;
aggregate between column "monto_beca";
print;