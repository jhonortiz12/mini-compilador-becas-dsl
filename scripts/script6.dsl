load "data/becas.csv";
filter column "tipo_beca" <= "Ingeniería";
filter column "universidad" < "UCC";
aggregate sum column "monto_beca";
aggregate count column "promedio_estudiante";
print;