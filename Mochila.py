from math import floor

def Mochila_PD2(p,v,C,n):
    # p = vetor de pesos
    # v = vetor de valores
    # C = capacidade da mochila
    # n = número de itens
    # m = matriz de memoização
    # vMax = valor máximo
    # vn = n*v é o valor máximo que pode ser obtido com os itens
    vMax = 0
    vn = 0

    for i in v:
        vn += i
    for i in v:
        if i > vMax:
            vMax = i
            
    # Define the matrix "m"
    m = [[0 for x in range(vn+1)] for y in range(n+1)]
    
    #Para Vmax 1 até vn faça m[0][Vmax] = infinito
    for Vmax in range(0,vn+1):
        m[0][Vmax] = float('inf')

    #Para k 0 ate n faça m[k][0] = 0
    for k in range(0,n+1):
        m[k][0] = 0

    #Para k 1 ate n faça
    #Para Vmax 1 ate vn faça
    for k in range(1,n+1):
        for Vmax in range(1,vn+1):
            #Se Vmax < v[k] então m[k][Vmax] = m[k-1][Vmax]
            if Vmax < v[k-1]:
                m[k][Vmax] = m[k-1][Vmax]
            #Senão m[k][Vmax] = min(m[k-1][Vmax], m[k-1][Vmax-v[k]] + p[k])
            else:
                m[k][Vmax] = min(m[k-1][Vmax], m[k-1][Vmax-v[k-1]] + p[k-1])

    #Para Vmax vn até 1 faça
    for Vmax in range(vn,1,-1):
        #Se m[n][Vmax] <= C então
        if m[n][Vmax] <= C:
            #Retorne Vmax
            return Vmax
    
def Mochila_Aprox(p, v, C, n, e):
    # p = vetor de pesos
    # v = vetor de valores
    # C = capacidade da mochila
    # n = número de itens
    # e = erro
    # m = matriz de memoização
    # vMax = valor máximo
    # lamb = constante de aproximação
    vMax = max(v)
    vn = sum(v)
    lamb = floor((e * vn) / vMax)

    for k in range(n):
        v[k] = v[k] // lamb  # Divide os valores por "lamb"

    return Mochila_PD2(p, v, C, n)






# Teste
p = [4, 2, 1, 3]
v = [50,40,30,45]
C = 5
n = len(v)
e = 0.5
print("Valor máximo: ", Mochila_Aprox(p,v,C,n,e))

