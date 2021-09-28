import random

def genera_random():
    lista_aleatorios = []

    for i in range(0, 100):
        lista_aleatorios.append(random.randint(1, 100))
    
    print("Lista inicial: ", lista_aleatorios)
    lista_aleatorios.sort()
    print("Lista ordenada: ", lista_aleatorios)

    print("Mayor: ", lista_aleatorios[99])
    print("Menor: ", lista_aleatorios[0])

    promedio = 0
    for elem in lista_aleatorios:
        promedio = promedio + elem
    
    promedio = promedio / 100

    print("Promedio: ", promedio)

    mediana = (lista_aleatorios[49] + lista_aleatorios[50]) / 2

    print("Mediana: ", mediana)

genera_random()