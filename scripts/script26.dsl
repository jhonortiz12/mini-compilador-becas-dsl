load "data/becas.csv";
filter column "tipo_beca" == "finalizada";
aggregate between column "monto_beca";
print;