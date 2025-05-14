load "data/becas.csv";
filter column "monto_beca" != 990573;
filter column "tipo_beca" >= "Ingeniería";
aggregate sum column "monto_beca";
print;