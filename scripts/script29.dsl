load "data/becas.csv";
filter column "carrera" >= "finalizada";
filter column "monto_beca" != 1858652;
aggregate between column "monto_beca";
aggregate sum column "monto_beca";
print;