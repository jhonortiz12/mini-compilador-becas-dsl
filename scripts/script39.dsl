load "data/becas.csv";

filter column "promedio_estudiante" >= 4.0 AND column "estado_beca" == "activa" 
     OR column "tipo_beca" == "excelencia";

aggregate count column "monto_beca";
aggregate average column "promedio_estudiante";

print;
