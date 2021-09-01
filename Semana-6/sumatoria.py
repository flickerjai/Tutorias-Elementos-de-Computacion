def sumatoria(n, m):
    contador = n
    total = 0
    while contador <= m:
        total += contador
        contador += 1
    print("Sumatoria total: ", total)

def sumatoria_for(n, m): 
    total = 0
    for i in range(n, m+1):
        total += i
    print("Sumatoria total: ", total)