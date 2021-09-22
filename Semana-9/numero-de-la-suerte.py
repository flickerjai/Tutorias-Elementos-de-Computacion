def numero_suerte(p_frase): 
    contador_suerte = 0
    for i in range(0, len(p_frase)):
        if p_frase[i] == "1": 
            contador_suerte = contador_suerte + 1
        elif p_frase[i] == "2":
            contador_suerte = contador_suerte + 2
        elif p_frase[i] == "3":
            contador_suerte = contador_suerte + 3
        elif p_frase[i] == "4":
            contador_suerte = contador_suerte + 4
        elif p_frase[i] == "5":
            contador_suerte = contador_suerte + 5
        elif p_frase[i] == "6":
            contador_suerte = contador_suerte + 6
        elif p_frase[i] == "7":
            contador_suerte = contador_suerte + 7
        elif p_frase[i] == "8":
            contador_suerte = contador_suerte + 8
        elif p_frase[i] == "9":
            contador_suerte = contador_suerte + 9
    return contador_suerte

def mostrar_usuario():
    frase = input("Ingrese una frase: ")
    numero = numero_suerte(frase)
    print("Su número de la suerte es: ", numero)