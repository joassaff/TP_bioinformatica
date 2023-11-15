from ete3 import Tree, TreeStyle
from Bio import Phylo

tree = Tree("output_tree.nwk")

ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.show_branch_support = True

tree.render("tree.png", w=500, units="mm", tree_style=ts)  
tree.show()

tree2 = Phylo.read("output_tree.nwk", "newick")

target_node_name = "HomoSap"

target_node = next((node for node in tree2.find_clades() if node.name == target_node_name), None)

for clade in tree2.find_clades():
    print(clade.name)
if target_node is None:
    print(f"No se encontró el nodo con el nombre {target_node_name}")
else:
    min_distance = float('inf')
    closest_node = None

    for clade in tree2.find_clades():
        print("hola")
        if clade != target_node and clade.name is not None:
            distance_to_target = tree2.distance(clade, target_node)
            if distance_to_target < min_distance:
                min_distance = distance_to_target
                closest_node = clade

    print(f"Distancia mínima a {target_node_name}: {min_distance}")
    print(f"Nodo más cercano: {closest_node.name if closest_node else 'Ninguno'}")

