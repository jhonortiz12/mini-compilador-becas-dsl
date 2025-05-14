import sys
import pandas as pd
from antlr4 import *
from BecasLexer import BecasLexer
from BecasParser import BecasParser
from BecasParserListener import BecasParserListener

class DSLInterpreter(BecasParserListener):
    def __init__(self):
        self.filename = None
        self.filters = []
        self.aggregates = []
        self.data = None

    def enterLoadInstruction(self, ctx):
        self.filename = ctx.STRING().getText().strip('"')
        print(f"📂 Cargando archivo CSV: {self.filename}")
        self.data = pd.read_csv(self.filename)
        print(f"✅ CSV cargado con {len(self.data)} registros")

    def enterFilterInstruction(self, ctx):
        strings = ctx.getTokens(BecasParser.STRING)
        column = strings[0].getText().strip('"')
        value_token = ctx.value().getText()
        operator = ctx.operator().getText()

        if value_token.replace('.', '', 1).isdigit():
            value = float(value_token) if '.' in value_token else int(value_token)
        else:
            value = f'"{value_token.strip("\"")}"'

        # CORRECTO: sin usar self.data[...] en query
        condition = f"({column} {operator} {value})"
        print(f"🔎 Acumulando filtro: {condition}")
        self.filters.append(condition)

    def enterAggregateInstruction(self, ctx):
        func = ctx.aggregateFunc().getText().lower()
        column = ctx.STRING().getText().strip('"')
        self.aggregates.append((func, column))
        print(f"🧮 Agregación solicitada: {func.upper()} sobre {column}")

    def enterPrintInstruction(self, ctx):
        print("🛠️ Ejecutando instrucción PRINT")
        df = self.data

        if self.filters:
            condition = " & ".join(self.filters)
            print(f"🧪 Aplicando filtros: {condition}")
            df = df.query(condition)
            print(f"✅ Filtrado: {len(df)} registros encontrados")

        for func, col in self.aggregates:
            if func == 'count':
                print(f"COUNT of {col}: {df[col].count()}")
            elif func == 'sum':
                print(f"SUM of {col}: {df[col].sum()}")
            elif func == 'average':
                print(f"AVERAGE of {col}: {df[col].mean()}")
            elif func == 'between':
                print(f"{col} min: {df[col].min()}, max: {df[col].max()}")
        print("\n--- Fin del script ---\n")

def run_script(script_path):
    print(f"▶️ Ejecutando script: {script_path}")
    input_stream = FileStream(script_path, encoding='utf-8')
    lexer = BecasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BecasParser(stream)
    tree = parser.program()

    walker = ParseTreeWalker()
    interpreter = DSLInterpreter()
    walker.walk(interpreter, tree)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python interpreter.py path/al/script.dsl")
    else:
        run_script(sys.argv[1])
