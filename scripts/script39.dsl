load "data/becas.csv";
filter column "promedio_estudiante" <= 4.14;
filter column "tipo_beca" != "UCC";
aggregate sum column "promedio_estudiante";
aggregate count column "monto_beca";
print;