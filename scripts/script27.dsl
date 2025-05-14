load "data/becas.csv";
filter column "monto_beca" != 890649;
filter column "promedio_estudiante" == 4.76;
aggregate average column "monto_beca";
aggregate between column "monto_beca";
aggregate between column "promedio_estudiante";
print;