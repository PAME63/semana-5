from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():  
   Productos1 = Producto(
      "papas",
      "Jenifer Castro",
      "ISBN001",
      5,
      10.99,
      True
   )

   Productos2 = Producto(
      "arroz",
      "Rosa Cepeda",
      "ISBN002",
      400,
      25.55,
      True
   )
    
   Clientes1 = Cliente(
     "Carlos Pineda",
     "carlos@correo.com",
      20,
      True
   )

   restaurante = Restaurante()

   restaurante.agregar_producto(Productos1)
   restaurante.agregar_producto(Productos2)


   restaurante.agregar_cliente(Clientes1)


   print("=== PRODUCTOS REGISTRADOS ===")
   restaurante.mostrar_producto()

   print("\n=== CLIENTES REGISTRADOS ===")
   restaurante.mostrar_clientes()

if __name__ == "__name__":
   main()