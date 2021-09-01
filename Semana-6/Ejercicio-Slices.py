hilera = "0123456789ABCDEF"

def slice_bases():
    hilera = "0123456789ABCDEF"
    base_8 = slice(0, 8)
    print("Digitos de base 8: ", hilera[base_8])
    base_16 = slice(2, 16)
    print("Digitos de base 16: ", hilera[base_16])

def slice_base2():
    base_2 = slice(0, 2)
    print("Digitos de base 2: ", hilera[base_2])