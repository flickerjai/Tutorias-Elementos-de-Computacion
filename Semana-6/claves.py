def claves_costos(clave, numin):
    costo = 0
    if clave == 12:
        costo = numin * 2
    elif clave == 15:
        costo = numin * 2.2
    elif clave == 18:
        costo = numin * 4.5
    elif clave == 19:
        costo = numin * 3.5
    elif clave == 23 or clave == 25:
        costo = numin * 6
    elif clave == 29:
        costo = numin * 5
    else:
        print("No hay clave que coincida")
    print("Costo total de la llamado", costo)
