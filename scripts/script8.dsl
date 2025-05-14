load "data/becas.csv";
filter column "carrera" == "UCC";
aggregate sum column "monto_beca";
print;