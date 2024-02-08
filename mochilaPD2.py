

def mochila_PD2(p, v, C, n):
    # Cria a matriz M com n linhas e soma(v) colunas
    soma = sum(v)
    M = [[500 for j in range(soma+1)] for i in range(n+1)]
    # Coloca "infinito" para valores com n = 0
    for i in range(1, sum(v)+1):
        M[0][i] = float('inf')
    # Coloca 0 para a V' = 0
    for i in range(n+1):
        M[i][0] = 0

        
    # Preenche a matriz teste
    for k in range(1, n+1):
        for Vl in range(1, soma+1):
            # Atribuir o valor de cima
            M[k][Vl] = M[k-1][Vl]
            # Se o valor não for valido então se mantém o valor anterior
            if v[k-1] <= Vl:
                # M[k-1][Vl-v[k-1]] é a soma dos pesos anteriores
                # Se o peso com o item atual for menor que o peso anterior
                if M[k][Vl]>(p[k-1] + M[k-1][Vl-v[k-1]]):
                    # Grava o peso minimo
                    M[k][Vl] = p[k-1] + M[k-1][Vl-v[k-1]]
            for i in range(n+1):
                print(M[i])
            input()
    # Encontrar um peso que caiba na mochila
    for i in range(soma, -1, -1):
        if M[n][i] <= C:
            return i


               

p = [4,2,1,2,2]
v = [2,1,3,4,1]
C = 5
n = 5
print(f"Para a capicidade: {C}, o valor maximo é: {mochila_PD2(p, v, C, n)}")