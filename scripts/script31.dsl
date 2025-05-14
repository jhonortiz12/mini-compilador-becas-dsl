load "data/becas.csv";
filter column "promedio_estudiante" >= 4.05;
aggregate between column "promedio_estudiante";
aggregate between column "monto_beca";
aggregate count column "promedio_estudiante";
print;