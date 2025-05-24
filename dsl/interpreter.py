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
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"El archivo {self.filename} no existe")
        print(f"\nCargando CSV: {self.filename}")
        try:
            self.data = pd.read_csv(self.filename)
            print(f"CSV cargado exitosamente")
            print(f"Total de registros: {len(self.data):,}")
            print(f"Columnas disponibles: {', '.join(self.data.columns)}")
        except Exception as e:
            raise Exception(f"Error al cargar el archivo CSV: {str(e)}")

    def visitFilterInstruction(self, ctx):
        condition = self.visit(ctx.filterExpr())
        if condition:
            print(f"\nAplicando filtro: {condition}")
            self.filters.append(condition)
        else:
            print("\nAdvertencia: condición de filtro vacía o inválida.")

    def visitFilterExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.filterExpr(0))
            op = ctx.getChild(1).getText().upper()
            right = self.visit(ctx.filterExpr(1))
            if left and right:
                if op == "AND":
                    return f"({left}) & ({right})"
                elif op == "OR":
                    return f"({left}) | ({right})"
            return None
        else:
            try:
                column = ctx.getChild(1).getText().strip('"')
                if column not in self.data.columns:
                    raise ValueError(f"La columna '{column}' no existe en el DataFrame")
                operator = ctx.getChild(2).getText()
                value_token = ctx.getChild(3).getText()
                if value_token.replace('.', '', 1).isdigit():
                    value = float(value_token) if '.' in value_token else int(value_token)
                else:
                    value = f'"{value_token.strip("\"")}"'
                return f"{column} {operator} {value}"
            except Exception as e:
                print(f"Error al construir la condición base del filtro: {e}")
                return None

    def visitAggregateInstruction(self, ctx):
        func = ctx.aggregateFunc().getText().lower()
        column = ctx.STRING().getText().strip('"')
        if column not in self.data.columns:
            raise ValueError(f"La columna '{column}' no existe en el DataFrame")
        print(f"\nAgregación solicitada: {func.upper()} sobre {column}")
        self.aggregates.append((func, column))

    def visitPrintInstruction(self, ctx):
        print("\nEjecutando instrucción PRINT")
        df = self.data
        total_inicial = len(df)

        if self.filters:
            query_str = " & ".join([f for f in self.filters if f])
            print(f"\nAplicando filtros: {query_str}")
            try:
                df = df.query(query_str)
                registros_filtrados = len(df)
                porcentaje = (registros_filtrados / total_inicial) * 100
                print(f"\nResultados del filtrado:")
                print(f"   • Registros totales: {total_inicial:,}")
                print(f"   • Registros filtrados: {registros_filtrados:,}")
                print(f"   • Porcentaje: {porcentaje:.1f}%")
                print("\nMuestra de registros filtrados:")
                print(df.head().to_string())
            except Exception as e:
                print(f"\nError al aplicar filtros: {e}")
                print("Detalles del error:", str(e))
                try:
                    mask = pd.Series(True, index=df.index)
                    for filter_expr in self.filters:
                        if filter_expr:
                            mask &= df.eval(filter_expr)
                    df = df[mask]
                    registros_filtrados = len(df)
                    porcentaje = (registros_filtrados / total_inicial) * 100
                    print(f"\nResultados del filtrado (método alternativo):")
                    print(f"   • Registros totales: {total_inicial:,}")
                    print(f"   • Registros filtrados: {registros_filtrados:,}")
                    print(f"   • Porcentaje: {porcentaje:.1f}%")
                    print("\nMuestra de registros filtrados:")
                    print(df.head().to_string())
                except Exception as e2:
                    print(f"\nError al aplicar filtro alternativo: {e2}")
                return
        else:
            print("\nℹNo se aplicaron filtros.")
            print("\nMuestra de registros:")
            print(df.head().to_string())

        print("\nResultados de las agregaciones:")
        for func, col in self.aggregates:
            try:
                if func == 'count':
                    valor = df[col].count()
                    print(f"   • COUNT de {col}: {valor:,}")
                elif func == 'sum':
                    valor = df[col].sum()
                    print(f"   • SUM de {col}: {valor:,.2f}")
                elif func == 'average':
                    valor = df[col].mean()
                    print(f"   • AVERAGE de {col}: {valor:.2f}")
                elif func == 'between':
                    min_val = df[col].min()
                    max_val = df[col].max()
                    print(f"   • {col} - Mínimo: {min_val:.2f}, Máximo: {max_val:.2f}")
            except Exception as e:
                print(f"Error al calcular {func} sobre {col}: {e}")

        print("\nFin del script\n")

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.filterExpr(0))
        right = self.visit(ctx.filterExpr(1))
        if left and right:
            return f"({left}) & ({right})"
        return None

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.filterExpr(0))
        right = self.visit(ctx.filterExpr(1))
        if left and right:
            return f"({left}) | ({right})"
        return None

    def visitBaseExpr(self, ctx):
        try:
            column = ctx.getChild(1).getText().strip('"')
            if column not in self.data.columns:
                raise ValueError(f"La columna '{column}' no existe en el DataFrame")
            operator = ctx.getChild(2).getText()
            value_token = ctx.getChild(3).getText()
            if value_token.replace('.', '', 1).isdigit():
                value = float(value_token) if '.' in value_token else int(value_token)
            else:
                value = f'"{value_token.strip("\"")}"'
            return f"{column} {operator} {value}"
        except Exception as e:
            print(f"Error en visitBaseExpr: {e}")
            return None


def run_script(script_path):
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"El archivo {script_path} no existe")

    print(f"\nEjecutando script: {script_path}\n")

    print("Contenido del script:")
    with open(script_path, "r", encoding="utf-8") as f:
        print(f.read())

    input_stream = FileStream(script_path, encoding='utf-8')
    lexer = BecasLexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("\nTokens generados:")
    stream.fill()
    for token in stream.tokens:
        if token.type == -1:
            continue
        token_text = token.text.replace("\n", "\\n")
        token_type = lexer.symbolicNames[token.type]
        print(f"   Línea {token.line}, Col {token.column}: [{token_text}] -> {token_type}")

    parser = BecasParser(stream)
    tree = parser.program()

    print("\nÁrbol sintáctico (parser.toStringTree()):")
    print(tree.toStringTree(recog=parser))

    name = os.path.basename(script_path).replace(".dsl", "")
    os.makedirs("doc", exist_ok=True)
    visual_tree = build_visual_tree(tree, parser)
    save_tree_image(visual_tree, f"doc/{name}_tree.png")

    print(f"\nÁrbol exportado como imagen: doc/{name}_tree.png")

    visitor = DSLVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python interpreter.py scripts/scriptX.dsl")
    else:
        try:
            run_script(sys.argv[1])
        except Exception as e:
            print(f"Error: {str(e)}")
            sys.exit(1)
