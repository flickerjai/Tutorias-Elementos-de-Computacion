def suma(numero_1, numero_2):
    total = numero_1 + numero_2
    return total

def resta(numero_1, numero_2):
    total = numero_1 - numero_2
    return total

def multiplicacion(numero_1, numero_2):
    total = numero_1 * numero_2
    return total

def solicitud_a_usuario():
    print("Bienvenid@, este programa devuelve los resultados de las operaciones básicas de dos números")
    print("Ingrese el primer número: ")
    primer_numero = int(input())
    print("Ingrese el segundo número: ")
    segundo_numero = int(input())
    total_suma = suma(primer_numero, segundo_numero)
    total_resta = resta(primer_numero, segundo_numero)
    total_multiplicacion = multiplicacion(primer_numero, segundo_numero)
    print("Total de la suma: ", total_suma)
    print("Total de la resta: ", total_resta)
    print("Total de la multiplicacion: ", total_multiplicacion)

solicitud_a_usuario()