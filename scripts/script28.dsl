load "data/becas.csv";
filter column "carrera" > "UCC";
filter column "promedio_estudiante" >= 3.3;
aggregate sum column "promedio_estudiante";
aggregate count column "promedio_estudiante";
print;