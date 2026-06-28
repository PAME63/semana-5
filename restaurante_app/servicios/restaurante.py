class Restaurante:

    def __init__(self):


        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto) -> None:

        self.productos.append(producto)
        

    def agregar_cliente(self, cliente) -> None:

        self.clientes.append(cliente)

    def mostrar_producto(self) -> None:


        for productos in self.productos:
            print(productos)

    def mostrar_clientes(self) -> None:


        for clientes in self.clientes:
            print(clientes)