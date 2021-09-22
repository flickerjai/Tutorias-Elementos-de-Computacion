import random

def sacar_al_azar(lista):
    random.shuffle(lista)
    print("El primero en exponer es: ", lista[0])
    print(lista)

def mostrar_usuario():
    nombre = ""
    lista_nombres = []
    print(lista_nombres)
    print("Si desea dejar digitar nombres, ingrese un cero")
    while(nombre != "0"):
        nombre = input("Ingrese un nombre: ")
        if nombre != "0":
            lista_nombres.append(nombre)
        print(lista_nombres)
    sacar_al_azar(lista_nombres)

mostrar_usuario()