class Producto:

    def __init__(self, id_producto, color, precio, mes_de_pedido):
        self.id_producto = id_producto
        self.color = color
        self.precio = precio
        self.mes_de_pedido = mes_de_pedido

    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, nuevo_id_producto):
        self.id_producto = nuevo_id_producto

    def get_color(self):
        return self.color

    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def get_precio(self):
        return self.precio

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def get_mes_de_pedido(self):
        return self.mes_de_pedido

    def set_mes_de_pedido(self, nuevo_mes):
        self.mes_de_pedido = nuevo_mes

class Computadora(Producto):

    def __init__(self, id_producto, color, precio, mes_de_pedido, procesador, memoria_ram, almacenamiento):
        #Atributos que vienen de la super clase
        Producto.__init__(self, id_producto, color, precio, mes_de_pedido)

        #Mis nuevos atributos
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento

    def get_procesador(self):
        return self.procesador

    def set_procesador(self, nuevo_procesador):
        self.procesador = nuevo_procesador

    def get_memoria_ram(self):
        return self.memoria_ram

    def set_memoria_ram(self, nuevo_memoria_ram):
        self.memoria_ram = nuevo_memoria_ram

    def get_almacenamiento(self):
        return self.almacenamiento

    def set_almacenamiento(self, nuevo_almacenamiento):
        self.almacenamiento = nuevo_almacenamiento

computadora1 = Computadora(1, "azul", 500000, "mayo", "AMD Ryzen 5", "16 GB", "256 SSD")
print("Memoria de la compu:", computadora1.get_memoria_ram())

computadora1.set_memoria_ram("8 GB")
print("Nueva memoria de la compu:", computadora1.get_memoria_ram())