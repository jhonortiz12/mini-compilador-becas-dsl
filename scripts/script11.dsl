load "data/becas.csv";
filter column "promedio_estudiante" < 4.75;
aggregate count column "promedio_estudiante";
print;