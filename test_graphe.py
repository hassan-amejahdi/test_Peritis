"""Pour définir la structure du graphe et le parcourir en Python,
 vous pouvez utiliser la bibliothèque NetworkX.
 Voici comment vous pouvez le faire :"""
 
import networkx as nx

# Créez un graphe dirigé
G = nx.DiGraph()

# Ajoutez les nœuds au graphe
nodes = [0, 1, 3, 4, 7, 8, 15, 16, 17, 18]
G.add_nodes_from(nodes)

# Ajoutez les arêtes au graphe
edges = [(0, 1), (1, 3), (1, 7), (3, 15), (3, 16), (4, 0), (7, 8), (15, 1), (16, 4), (17, 18)]
G.add_edges_from(edges)

# Parcourez le graphe de haut en bas de la gauche vers la droite
path = list(nx.topological_sort(G))

# Affichez le chemin
print(" - ".join(map(str, path)))


