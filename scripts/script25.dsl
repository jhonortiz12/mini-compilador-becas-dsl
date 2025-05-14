load "data/becas.csv";
filter column "carrera" != "UCC";
filter column "promedio_estudiante" != 4.58;
aggregate average column "promedio_estudiante";
aggregate count column "monto_beca";
aggregate sum column "promedio_estudiante";
print;