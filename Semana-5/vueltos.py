def vueltos(mi_pago, saldo_a_cancelar):
    vuelto = mi_pago - saldo_a_cancelar
    print("Su vuelto es: ", vuelto)
    while (vuelto != 0):
        if (vuelto >= 100): 
            vuelto = vuelto - 100
            print("Billete de 100")
        else:
            if (vuelto >= 20): 
                vuelto = vuelto - 20
                print("Billete de 20")
            else: 
                if (vuelto >= 10): 
                    vuelto = vuelto - 10
                    print("Billete de 10")
                else:
                    if (vuelto >= 1):
                        vuelto = vuelto - 1
                        print("Billete de 1")

def pagos_usuario():
    print("Ingrese el total con el que va a pagar: ")
    mi_pago = int(input())
    print("Ingrese el monto que debe cancelar: ")
    saldo_a_cancelar = int(input())
    vueltos(mi_pago, saldo_a_cancelar)

pagos_usuario()