def verificar_tripleta(lado_1, lado_2, lado_3):
    if (lado_1 ** 2 == (lado_2 ** 2 + lado_3 ** 2)):
        return True
    elif (lado_2 ** 2 == (lado_1 ** 2 + lado_3 ** 2)):
        return True
    elif (lado_3 ** 2 == (lado_1 ** 2 + lado_2 ** 2)):
        return True
    else:
        return False

def encontrar_tripletas(): 
    hipotenusa = 1
    while hipotenusa <= 500: 
        cateto_a = 1
        while cateto_a <= hipotenusa: 
            cateto_b = 1
            while cateto_b <= hipotenusa:
                es_tripleta = verificar_tripleta(hipotenusa, cateto_a, cateto_b)
                if es_tripleta: 
                    print("Valores de la tripleta: ", hipotenusa, ", ", cateto_a, ", ", cateto_b)
                    cateto_b += 1
                else: 
                    cateto_b += 1
            cateto_a += 1
        hipotenusa += 1