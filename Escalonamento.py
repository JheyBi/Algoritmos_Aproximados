def graham_mathlener(n, m, t):
    M = [[] for _ in range(m)]  # Inicialize um array de máquinas vazias

    def encontrar_menor_carga(M):
        menor_carga = float('inf')
        maquina_menor_carga = 0

        for j in range(m):
            carga_maquina = calcular_carga(M[j])
            if carga_maquina < menor_carga:
                menor_carga = carga_maquina
                maquina_menor_carga = j

        return maquina_menor_carga

    def calcular_carga(maquina):
        carga = 0
        for tarefa in maquina:
            carga += tempo_da_tarefa(tarefa)
        return carga

    # Função para calcular o tempo da tarefa (substitua com sua própria lógica)
    def tempo_da_tarefa(tarefa):
        return t[tarefa - 1]

    for i in range(1, n + 1):
        maquina_menor_carga = encontrar_menor_carga(M)
        M[maquina_menor_carga].append(i)

    return M

# Exemplo de uso do escalonamento
n = 7  # Número de tarefas
m = 3  # Número de máquinas
t = [4, 2, 1, 5, 9,2,6]  # Tempo de execução de cada tarefa

resultado = graham_mathlener(n, m, t)
print("Alocação de tarefas em máquinas:", resultado)
