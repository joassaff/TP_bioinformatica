from ete3 import Tree, TreeStyle
from Bio import Phylo

# Cargar el árbol desde el archivo
tree = Tree("output_tree.nwk")

ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.show_branch_support = True

# Dibujar el árbol y mostrarlo
tree.render("tree.png", w=500, units="mm", tree_style=ts)  # Ajustar el valor de w según tus preferencias
tree.show()

tree2 = Phylo.read("output_tree.nwk", "newick")

# Define el nodo objetivo
target_node_name = "HomoSap"

# Encuentra el nodo objetivo en el árbol
target_node = next((node for node in tree2.find_clades() if node.name == target_node_name), None)

for clade in tree2.find_clades():
    print(clade.name)
# Verifica si el nodo objetivo se encontró
if target_node is None:
    print(f"No se encontró el nodo con el nombre {target_node_name}")
else:
    # Inicializa la distancia mínima y el nodo correspondiente
    min_distance = float('inf')  # Inicializa con infinito para garantizar que la primera distancia sea menor
    closest_node = None

    # Itera sobre todos los nodos del árbol y calcula la distancia al nodo objetivo
    for clade in tree2.find_clades():
        print("hola")
        if clade != target_node and clade.name is not None:
            distance_to_target = tree2.distance(clade, target_node)
            if distance_to_target < min_distance:
                min_distance = distance_to_target
                closest_node = clade

    # Imprime la distancia mínima y el nodo más cercano
    print(f"Distancia mínima a {target_node_name}: {min_distance}")
    print(f"Nodo más cercano: {closest_node.name if closest_node else 'Ninguno'}")

