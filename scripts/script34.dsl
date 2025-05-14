load "data/becas.csv";
filter column "monto_beca" >= 728663;
filter column "estado_beca" <= "suspendida";
aggregate count column "monto_beca";
aggregate between column "promedio_estudiante";
aggregate count column "promedio_estudiante";
print;