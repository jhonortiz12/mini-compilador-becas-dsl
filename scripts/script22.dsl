load "data/becas.csv";
filter column "carrera" != "UCC";
filter column "tipo_beca" <= "Ingeniería";
aggregate between column "promedio_estudiante";
aggregate sum column "promedio_estudiante";
print;