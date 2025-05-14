load "data/becas.csv";
filter column "carrera" > "Ingeniería";
aggregate count column "monto_beca";
aggregate sum column "monto_beca";
aggregate sum column "monto_beca";
print;