load "data/becas.csv";
filter column "monto_beca" == 1118597;
filter column "carrera" == "Ingeniería";
aggregate between column "monto_beca";
aggregate between column "monto_beca";
print;