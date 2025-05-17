import sys
import os
import pandas as pd
from antlr4 import *
from BecasLexer import BecasLexer
from BecasParser import BecasParser
from BecasParserVisitor import BecasParserVisitor
from tree_visualizer import build_visual_tree, save_tree_image


class DSLVisitor(BecasParserVisitor):
    def __init__(self):
        self.filename = None
        self.filters = []
        self.aggregates = []
        self.data = None

    def visitProgram(self, ctx):
        for instr in ctx.instruction():
            self.visit(instr)

    def visitLoadInstruction(self, ctx):
        self.filename = ctx.STRING().getText().strip('"')
        print(f"📂 Cargando CSV: {self.filename}")
        self.data = pd.read_csv(self.filename)
        print(f"✅ CSV cargado con {len(self.data)} registros")

    def visitFilterInstruction(self, ctx):
        condition = self.visit(ctx.filterExpr())
        print(f"🔎 Condición compuesta acumulada: {condition}")
        self.filters.append(condition)

    def visitFilterExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.filterExpr(0))
            op = ctx.getChild(1).getText().upper()
            right = self.visit(ctx.filterExpr(1))
            if op == "AND":
                return f"({left}) & ({right})"
            elif op == "OR":
                return f"({left}) | ({right})"
        else:
            column = ctx.STRING().getText().strip('"')
            operator = ctx.operator().getText()
            value_token = ctx.value().getText()

            if value_token.replace('.', '', 1).isdigit():
                value = float(value_token) if '.' in value_token else int(value_token)
            else:
                value = f'"{value_token.strip("\"")}"'

            return f"({column} {operator} {value})"

    def visitAggregateInstruction(self, ctx):
        func = ctx.aggregateFunc().getText().lower()
        column = ctx.STRING().getText().strip('"')
        print(f"🧮 Agregación solicitada: {func.upper()} sobre {column}")
        self.aggregates.append((func, column))

    def visitPrintInstruction(self, ctx):
        print("\n🛠️ Ejecutando instrucción PRINT")
        df = self.data

        if self.filters:
            query_str = " & ".join(self.filters)
            print(f"🧪 Aplicando filtros: {query_str}")
            df = df.query(query_str)
            print(f"📊 Registros que cumplen condición: {len(df)}\n")
            print(df.head())

        for func, col in self.aggregates:
            if func == 'count':
                print(f" COUNT of {col}: {df[col].count()}")
            elif func == 'sum':
                print(f" SUM of {col}: {df[col].sum()}")
            elif func == 'average':
                print(f" AVERAGE of {col}: {df[col].mean()}")
            elif func == 'between':
                print(f" {col} min: {df[col].min()}, max: {df[col].max()}")

        print("\n✅ Fin del script\n")


def run_script(script_path):
    print(f"\n▶️ Ejecutando script: {script_path}")

    print("\n📄 Contenido del script:")
    with open(script_path, "r", encoding="utf-8") as f:
        print(f.read())

    input_stream = FileStream(script_path, encoding='utf-8')
    lexer = BecasLexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("\n🔤 Tokens generados:")
    stream.fill()
    for token in stream.tokens:
        if token.type == -1:
            continue
        token_text = token.text.replace("\n", "\\n")
        token_type = lexer.symbolicNames[token.type]
        print(f"Línea {token.line}, Col {token.column}: [{token_text}] -> {token_type}")

    parser = BecasParser(stream)
    tree = parser.program()

    print("\n🌳 Árbol sintáctico (texto con parser.toStringTree()):")
    print(tree.toStringTree(recog=parser))

    name = os.path.basename(script_path).replace(".dsl", "")
    os.makedirs("doc", exist_ok=True)
    visual_tree = build_visual_tree(tree, parser)
    save_tree_image(visual_tree, f"doc/{name}_tree.png")

    print(f"\n🖼️ Árbol exportado como imagen: doc/{name}_tree.png")

    visitor = DSLVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python interpreter.py scripts/scriptX.dsl")
    else:
        run_script(sys.argv[1])
