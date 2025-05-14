load "data/becas.csv";
filter column "universidad" == "Ingeniería";
aggregate sum column "monto_beca";
print;