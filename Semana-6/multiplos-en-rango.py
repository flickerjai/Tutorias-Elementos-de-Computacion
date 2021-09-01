def multiplos(n, m):
    contador = 1
    while(contador <= m - n):
        print("Multiplo ", n, "*", contador ," = " ,(n * contador))
        contador+= 1

def multiplos_variacion(n, m):
    contador = n
    while(contador <= m - n):
        print("Multiplo ", n, "*", contador ," = " ,(n * contador))
        contador+= 1