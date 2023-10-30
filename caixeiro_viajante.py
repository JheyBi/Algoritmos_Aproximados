import networkx as nx
from networkx.algorithms import approximation as approx
from networkx.algorithms import matching


def christofides(G, weight='weight'):
    # Passo 1 & 2: Crie uma árvore geradora mínima T de G.
    T = nx.minimum_spanning_tree(G, weight=weight)
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

    # Passo 3: Encontre um acoplamento perfeito M no subgrafo induzido pelos vértices de I.
    M = approx.min_weight_matching(G.subgraph(odd_degree_nodes))

    # Passo 4: Combine as arestas de M e T para formar um multigrafo H em que cada vértice tem grau par.
    H = nx.MultiGraph(T)
    H.add_edges_from(M)

    # Passo 5: Forme um circuito Euleriano em H.
    euler_circuit = list(nx.eulerian_circuit(H))

    # Passo 6: Transforme o circuito encontrado na etapa anterior em um circuito Hamiltoniano
    visited = set()
    hamiltonian_circuit = []

    for u, v in euler_circuit:
        if not v in visited:
            visited.add(v)
            hamiltonian_circuit.append((u, v))
    return hamiltonian_circuit

G = nx.complete_graph(5)

# Suponha que temos a seguinte matriz de distâncias para 5 cidades.
distances = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 15],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 10],
    [25, 15, 20, 10, 0]
]

# Atribua os pesos das arestas de acordo com a matriz de distâncias.
for i in range(5):
    for j in range(i+1, 5):
        G[i][j]['weight'] = distances[i][j]

# Use o algoritmo de Christofides para encontrar um circuito Hamiltoniano.
circuit = christofides(G)

print("Circuito Hamiltoniano: ", circuit)