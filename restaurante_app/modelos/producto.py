class Producto:

    def __init__(self,
        arroz: str,
        papas: str,
        isbn: str,
        paginas: int,
        precio: float,
        disponible: bool
    ):

        self.arroz = arroz
        self.papas = papas
        self.isbn = isbn
        self.paginas = paginas
        self.precio = precio

        self.disponible = disponible

    def mostrar_informacion(self) -> str:

        return (
            f"Arroz: {self.arroz} | "
            f"Papas: {self.papas} | "
            f"Páginas: {self.paginas}"
        )

    def __str__(self) -> str:

        return (
            f"{self.arroz} | "
            f"{self.papas} | "
            f"${self.precio}"
        )