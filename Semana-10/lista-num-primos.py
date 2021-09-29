import random

def generar_lista_aleatorios():
    largo_lista = int(input("Ingrese el tamaño de la lista: "))

    while(largo_lista < 5 or largo_lista > 15):
        print("Error, digite nuevamente, sólo valores entre 5 y 15")
        largo_lista = int(input("Ingrese el tamaño de la lista: "))
        
    lista_aleatorios = []

    for i in range(0, largo_lista): 
        lista_aleatorios.append(random.randint(1, 50))

    print(lista_aleatorios)
    return lista_aleatorios

def filtrar_primos(lista_numeros):
    nueva_lista = []

    for elem in lista_numeros:
        if elem != 2 and elem != 3 and elem != 5 and elem != 7 and elem != 11 and elem != 13:
            if elem % 2 == 0 or elem % 3 == 0 or elem % 5 == 0 or elem % 7 == 0 or elem % 11 == 0 or elem % 13 == 0: 
                nueva_lista.append(0)
            else: 
                nueva_lista.append(elem)
        else: 
            nueva_lista.append(elem)

    print(nueva_lista)

filtrar_primos(generar_lista_aleatorios())