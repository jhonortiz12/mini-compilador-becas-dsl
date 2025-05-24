# Mini Compilador DSL para Becas

Este proyecto implementa un mini compilador para un DSL (Domain Specific Language) diseñado para procesar y analizar datos de becas estudiantiles.

## Características

- Carga de datos desde archivos CSV
- Filtrado de datos usando expresiones lógicas
- Agregación de datos (count, sum, average, between)
- Visualización del árbol sintáctico
- Manejo de errores robusto

## Requisitos

- Python 3.8 o superior
- Graphviz (para visualización del árbol sintáctico)
- Dependencias de Python:
  - pandas
  - antlr4-python3-runtime
  - anytree

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/mini-compilador-becas-dsl.git
cd mini-compilador-becas-dsl
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Instalar Graphviz:
   - Windows: `winget install graphviz`
   - Linux: `sudo apt-get install graphviz`
   - macOS: `brew install graphviz`

## Sintaxis del DSL

### Cargar datos
```
LOAD "ruta/al/archivo.csv"
```

### Filtrar datos
```
FILTER columna operador valor
FILTER (condición1 AND condición2)
FILTER (condición1 OR condición2)
```

Operadores soportados:
- `==` (igual)
- `!=` (diferente)
- `>` (mayor que)
- `<` (menor que)
- `>=` (mayor o igual)
- `<=` (menor o igual)

### Agregar datos
```
AGGREGATE funcion "columna"
```

Funciones soportadas:
- `count`: cuenta registros
- `sum`: suma valores
- `average`: calcula promedio
- `between`: muestra mínimo y máximo

### Imprimir resultados
```
PRINT
```

## Ejemplo de uso

```dsl
LOAD "data/becas.csv"
FILTER (promedio_estudiante >= 4.0 AND estado_beca == "activa") OR tipo_beca == "excelencia"
AGGREGATE count "monto_beca"
AGGREGATE average "promedio_estudiante"
PRINT
```

## Estructura del proyecto

```
mini-compilador-becas-dsl/
├── dsl/
│   ├── interpreter.py      # Intérprete del DSL
│   ├── tree_visualizer.py  # Visualización del árbol sintáctico
│   └── ...                 # Archivos generados por ANTLR
├── scripts/
│   └── *.dsl              # Scripts de ejemplo
├── data/
│   └── becas.csv          # Datos de ejemplo
└── doc/
    └── *_tree.png         # Imágenes del árbol sintáctico
```

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.