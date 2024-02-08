import networkx as nx

def rsl_ciclo_hamiltoniano(grafo):
    # Função interna que realiza a busca recursiva utilizando backtracking
    def backtrack(ciclo):
        # Verifica se o ciclo atual contém todos os vértices do grafo
        if len(ciclo) == n_vertices:
            # Verifica se o último vértice do ciclo possui uma aresta de volta para o primeiro vértice
            if grafo.has_edge(ciclo[-1], ciclo[0]):
                # Retorna o ciclo encontrado
                return ciclo
            else:
                # Se não houver uma aresta de volta para o primeiro vértice, o ciclo não é hamiltoniano
                return None
        # Itera sobre os vizinhos do último vértice do ciclo
        for vizinho in grafo.neighbors(ciclo[-1]):
            # Verifica se o vizinho não está no ciclo atual
            if vizinho not in ciclo:
                # Adiciona o vizinho ao ciclo e chama recursivamente a função backtrack
                ciclo.append(vizinho)
                resultado = backtrack(ciclo)
                # Se um ciclo hamiltoniano for encontrado na chamada recursiva, retorna o resultado
                if resultado is not None:
                    return resultado
                # Se não for encontrado, remove o vizinho do ciclo atual e continua a busca
                ciclo.pop()
        # Se nenhum ciclo hamiltoniano for encontrado, retorna None
        return None

    # Número de vértices no grafo
    n_vertices = grafo.number_of_nodes()
    # Vértice inicial para começar a busca
    ciclo_inicial = [0]
    # Chama a função backtrack para encontrar um ciclo hamiltoniano
    ciclo_hamiltoniano = backtrack(ciclo_inicial)
    # Adiciona o primeiro vértice ao final do ciclo para fechar o ciclo
    if ciclo_hamiltoniano is not None:
        ciclo_hamiltoniano.append(ciclo_hamiltoniano[0])
    # Retorna o ciclo hamiltoniano encontrado (ou None se não houver)
    return ciclo_hamiltoniano

# Exemplo de uso
# Criando um grafo de exemplo
grafo = nx.Graph()
grafo.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])

# Encontrando um ciclo hamiltoniano utilizando o algoritmo RSL
ciclo_hamiltoniano = rsl_ciclo_hamiltoniano(grafo)
print("Ciclo Hamiltoniano encontrado:", ciclo_hamiltoniano)