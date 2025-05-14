load "data/becas.csv";
filter column "monto_beca" >= 1429807;
aggregate between column "monto_beca";
print;