def escalonamento_graham(m,n,t):
    for j in range(0, len(m)):
        m[j] = 0
    for i in range(0, n):
        for j in range(0, len(m)):
            if min(m) == m[j]:
                m[j] = m[j] + t[i]
                break
    return m, max(m)

m = [0,0,0]
n = 7
t = [4,2,1,5,9,2,6]
print(escalonamento_graham(m,n,t))