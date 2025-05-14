load "data/becas.csv";
filter column "carrera" <= "UCC";
filter column "universidad" <= "UCC";
aggregate average column "monto_beca";
aggregate count column "monto_beca";
print;