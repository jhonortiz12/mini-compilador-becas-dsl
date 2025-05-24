import os
from anytree import Node
from anytree.exporter import DotExporter


def build_visual_tree(tree, parser):
    """Construye un árbol visual a partir del árbol de sintaxis."""
    def create_node(parent, ctx, name=None):
        if ctx is None:
            return None
        if name is None:
            name = parser.ruleNames[ctx.getRuleIndex()]
        # Escapar caracteres especiales
        name = name.replace('"', '\\"').replace('/', '\\/')
        node = Node(name, parent=parent)
        for child in ctx.getChildren():
            if hasattr(child, 'getRuleIndex'):
                create_node(node, child)
            else:
                # Escapar caracteres especiales en los tokens
                child_text = str(child).replace('"', '\\"').replace('/', '\\/')
                Node(child_text, parent=node)
        return node

    root = create_node(None, tree)
    return root


def save_tree_image(tree, output_file, format='png'):
    """Guarda el árbol como una imagen."""
    if tree is None:
        print("Advertencia: No hay árbol para visualizar")
        return

    # Crear directorio si no existe
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Configurar el exportador
    exporter = DotExporter(
        tree,
        nodeattrfunc=lambda node: f'label="{node.name}"',
        edgeattrfunc=lambda parent, child: 'color=blue',
        options=[
            'rankdir=TB',
            'nodesep=0.5',
            'ranksep=0.5',
            'fontname="Arial"',
            'fontsize=12',
            'splines=ortho',
            'charset="UTF-8"'
        ]
    )

    # Generar archivo DOT
    dot_file = output_file.replace('.png', '.dot')
    exporter.to_dotfile(dot_file)

    # Buscar Graphviz en ubicaciones comunes
    dot_paths = [
        os.path.join("C:", os.sep, "Program Files", "Graphviz", "bin", "dot.exe"),
        os.path.join("C:", os.sep, "Program Files (x86)", "Graphviz", "bin", "dot.exe"),
        "/usr/bin/dot",
        "/usr/local/bin/dot"
    ]

    dot_path = None
    for path in dot_paths:
        if os.path.exists(path):
            dot_path = path
            break

    if dot_path is None:
        print("Advertencia: No se encontró Graphviz. La imagen del árbol no se generará.")
        print("Por favor, instale Graphviz desde https://graphviz.org/download/")
        return

    try:
        # Generar imagen
        os.system(f'"{dot_path}" -T{format} {dot_file} -o {output_file}')
        print(f"Árbol sintáctico guardado como: {output_file}")
    except Exception as e:
        print(f"Error al generar la imagen del árbol: {e}")
        print("El archivo DOT se guardó en:", dot_file)
