'''Emule la funcionalidad de “Word”. Reciba un texto e indique:
- Cantidad de palabras.
- Cantidad de caracteres.
Ejemplo:
Entrada:
“Hola familia académica, emulemos el trabajo de Word”
- Cantidad de palabras: 8 palabras
- Cantidad de caracteres: 51 caracteres'''

def contar_palabras(p_frase):
    contador_palabras = 1
    for i in range(0, len(p_frase)):
        if p_frase[i] == " ":
            contador_palabras = contador_palabras + 1
    return contador_palabras

def contar_caracteres(p_frase):
    contador_caracteres = len(p_frase)
    return contador_caracteres

def contar_caracteres_sin_espacio(p_frase):
    contador_caracteres = 0
    for i in range(0, len(p_frase)):
        if p_frase[i] != " ":
            contador_caracteres = contador_caracteres + 1
    return contador_caracteres

def mostrar_usuario(): 
    frase = input("Ingrese una frase: ")
    print("Cantidad de palabras: ", contar_palabras(frase))
    print("Cantidad de caracteres: ", contar_caracteres(frase))
    print("Cantidad de caracteres (sin contar espacios): ",contar_caracteres_sin_espacio(frase))