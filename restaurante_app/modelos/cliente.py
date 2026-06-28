class Cliente:

    def __init__(
        self,
        nombre: str,
        correo: str,
        edad: int,
        activo: bool
    ):


        self.nombre = nombre
        self.correo = correo

        self.edad = edad


        self.activo = activo

    def mostrar_informacion(self) -> str:


        return (
            f"{self.nombre} | "
            f"{self.correo}"
        )

    def __str__(self) -> str:


        return (
            f"{self.nombre} "
            f"({self.edad} años)"
        )