 Sistema de Gestión de Restaurante
 
 
 
📚 Descripción del Proyecto
 
Este proyecto corresponde a la Tarea Semana 5: Aplicación de identificadores y tipos de datos en un proyecto Python modular, de la asignatura Programación Orientada a Objetos.
 
El objetivo es desarrollar un sistema básico para gestionar información de un restaurante, aplicando buenas prácticas de programación, convenciones de nombres, tipos de datos adecuados y organización modular del código. El sistema permite registrar y consultar productos disponibles y clientes registrados en el establecimiento.
 
 
 
📂 Estructura del Proyecto
 
plaintext
  
restaurante_app/
├── modelos/
│   ├── _init_.py       # Archivo de inicialización del paquete modelos
│   ├── producto.py       # Clase que representa un producto/plato del restaurante
│   └── cliente.py        # Clase que representa un cliente registrado
├── servicios/
│   └── restaurante.py    # Clase principal que gestiona productos y clientes
├── main.py               # Punto de entrada del programa
└── README.md             # Documentación del proyecto
 
 
 
 
🧩 Entidades y Tipos de Datos
 
1. Clase  Producto 
 
Representa un plato, bebida o artículo disponible en el restaurante:
 
Atributo Tipo de dato Descripción 
 nombre   str  Nombre del producto 
 categoria   str  Clasificación (ej: "Plato fuerte", "Bebida") 
 precio   float  Valor monetario del producto 
 disponible   bool  Indica si el producto está disponible para venta 
 cantidad   int  Número de unidades disponibles en inventario 
 
2. Clase  Cliente 
 
Representa una persona registrada en el sistema:
 
Atributo Tipo de dato Descripción 
 identificacion   str  Documento de identidad del cliente 
 nombre   str  Nombre completo del cliente 
 telefono   str  Número de contacto 
 correo   str  Dirección de correo electrónico 
 
3. Clase  ServicioRestaurante 
 
Gestiona las colecciones del sistema:
 
-  lista_productos :  list  → Almacena objetos de la clase  Producto 
-  lista_clientes :  list  → Almacena objetos de la clase  Cliente 
 
 
 
✅ Requisitos Cumplidos
 
- ✅ Estructura de carpetas y archivos solicitada
- ✅ Uso de convenciones de nombres:
- Clases en formato PascalCase ( Producto ,  Cliente ,  ServicioRestaurante )
- Variables, atributos y métodos en formato snake_case ( lista_productos ,  agregar_producto )
- ✅ Tipos de datos básicos:  str ,  int ,  float ,  bool 
- ✅ Uso de listas como tipo de dato compuesto para almacenar múltiples objetos
- ✅ Implementación del método constructor  _init_  en todas las clases
- ✅ Método especial  _str_  para representar objetos como texto legible
- ✅ Importaciones correctas entre archivos del proyecto
- ✅ Comentarios explicativos en secciones clave del código
- ✅ No se utilizaron nombres genéricos, se evitó el copiado literal del ejemplo de biblioteca
 
 
 
🚀 Cómo Ejecutar el Proyecto
 
1. Asegúrate de tener instalado Python 3.8 o superior
2. Clona o descarga este repositorio
3. Abre la terminal en la carpeta  restaurante_app 
4. Ejecuta el archivo principal:
bash
  
python main.py
 
5. Se mostrará en consola la información de productos y clientes registrados en el sistema.
 
 
 
📌 Funcionalidades Principales
 
- Registrar nuevos productos en el sistema
- Consultar la lista de productos disponibles
- Registrar nuevos clientes
- Consultar la lista de clientes registrados


 