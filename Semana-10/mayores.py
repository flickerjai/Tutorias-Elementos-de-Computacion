nums1 = [8, 7, 6, 45, 4, 3]
nums2 = [1,1,1,1,1,1]

def obtener_elementos_l(lista1, lista2):
    print("El número mayor de lista 1: ", max(lista1))
    print("El número mayor de lista 2: ", max(lista2))

obtener_elementos_l(nums1, nums2)

def obtener_mayor(lista): 
    mayor = lista[0]
    for i in range(0, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]

    print("El mayor de la función que yo cree: ", mayor)

obtener_mayor(nums1)
obtener_mayor(nums2)