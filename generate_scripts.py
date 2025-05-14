import os
import random

# Asegúrate de que la carpeta 'scripts' existe
os.makedirs("scripts", exist_ok=True)

# Campos posibles del CSV
columns = [
    "promedio_estudiante", "monto_beca", "estado_beca",
    "carrera", "tipo_beca", "universidad"
]

aggregate_funcs = ["count", "sum", "average", "between"]
comparisons = [">", "<", ">=", "<=", "==", "!="]
string_values = ["\"activa\"", "\"finalizada\"", "\"suspendida\"", "\"Ingeniería\"", "\"excelencia\"", "\"UCC\""]

def random_value(col):
    if "promedio" in col:
        return str(round(random.uniform(3.0, 5.0), 2))
    if "monto" in col:
        return str(random.randint(500000, 2000000))
    return random.choice(string_values)

# Generar 40 scripts
for i in range(1, 41):
    lines = []
    lines.append('load "data/becas.csv";')

    # Agregar de 1 a 2 filtros
    for _ in range(random.randint(1, 2)):
        col = random.choice(columns)
        comp = random.choice(comparisons)
        val = random_value(col)
        lines.append(f'filter column "{col}" {comp} {val};')

    # Agregar de 1 a 3 agregaciones
    for _ in range(random.randint(1, 3)):
        func = random.choice(aggregate_funcs)
        col = random.choice(["monto_beca", "promedio_estudiante"])
        lines.append(f'aggregate {func} column "{col}";')

    lines.append("print;")

    # Guardar en archivo
    with open(f"scripts/script{i}.dsl", "w") as f:
        f.write("\n".join(lines))

print("✅ Se generaron 40 scripts DSL en la carpeta 'scripts/'")
