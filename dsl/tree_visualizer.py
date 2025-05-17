from anytree import Node
from anytree.exporter import DotExporter
import os

def build_visual_tree(antlr_tree, parser):
    def build(node, parent=None):
        label = parser.ruleNames[node.getRuleIndex()] if node.getChildCount() > 0 else node.getText()
        label = label.replace('"', '\\"')
        current = Node(label, parent=parent)
        for i in range(node.getChildCount()):
            build(node.getChild(i), current)
        return current

    return build(antlr_tree)

def save_tree_image(root, output_file):
    dot_file = output_file.replace('.png', '.dot')
    DotExporter(root).to_dotfile(dot_file)
    os.system(f"dot -Tpng {dot_file} -o {output_file}")
