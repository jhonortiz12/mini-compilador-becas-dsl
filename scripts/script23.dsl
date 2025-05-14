load "data/becas.csv";
filter column "monto_beca" > 819473;
aggregate count column "promedio_estudiante";
print;