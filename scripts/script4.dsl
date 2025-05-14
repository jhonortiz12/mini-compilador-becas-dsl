load "data/becas.csv";
filter column "monto_beca" < 1737283;
filter column "tipo_beca" == "excelencia";
aggregate sum column "promedio_estudiante";
aggregate average column "monto_beca";
print;