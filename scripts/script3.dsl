load "data/becas.csv";
filter column "promedio_estudiante" == 3.89;
aggregate average column "monto_beca";
print;