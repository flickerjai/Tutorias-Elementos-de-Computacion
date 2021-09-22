'''Reciba un texto y emita la cadena espejo.
Entrada: “mami”
Salida: “imam” 
'''

def cadena_espejo(p_frase):
    posicion = len(p_frase) - 1
    nueva_palabra = ""
    while posicion >= 0: 
        nueva_palabra = nueva_palabra + p_frase[posicion]
        posicion = posicion - 1

    print(nueva_palabra)

def mostrar_usuario():
    cadena_espejo(input("Ingrese un texto: "))