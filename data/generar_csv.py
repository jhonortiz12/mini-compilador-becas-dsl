import pandas as pd
from faker import Faker
import random

fake = Faker()
tipos_beca = ["alimentación", "excelencia", "transporte", "manutención"]
estados = ["activa", "suspendida", "finalizada"]
carreras = ["Ingeniería", "Medicina", "Derecho", "Psicología", "Contaduría"]
universidades = ["UCC", "Nacional", "Andes", "Javeriana", "ICESI"]

datos = []

for i in range(300):
    datos.append({
        "id_beca": f"B{i+1:04}",
        "id_estudiante": f"E{i+1:04}",
        "tipo_beca": random.choice(tipos_beca),
        "monto_beca": round(random.uniform(500000, 2000000), 2),
        "fecha_inicio": fake.date_between(start_date='-2y', end_date='-6m'),
        "fecha_fin": fake.date_between(start_date='-6m', end_date='today'),
        "promedio_estudiante": round(random.uniform(3.0, 5.0), 2),
        "estado_beca": random.choice(estados),
        "carrera": random.choice(carreras),
        "universidad": random.choice(universidades),
    })

df = pd.DataFrame(datos)
df.to_csv("data/becas.csv", index=False)
