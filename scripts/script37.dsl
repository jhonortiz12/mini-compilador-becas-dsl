load "data/becas.csv";
filter column "promedio_estudiante" < 3.14;
aggregate between column "promedio_estudiante";
print;