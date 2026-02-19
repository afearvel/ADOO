from ADOO.prestamo import Prestamo


class Usuario:
    def __init__(self, idUsuario: int, nombre: str, limite_prestamos: int):
        self.__idUsuario: int = idUsuario
        self.__nombre: str = nombre
        self.__limite_prestamos: int = limite_prestamos
        self.__prestamos_activos: list[Prestamo] = []

    @property
    def idUsuario(self) -> int:
        return self.__idUsuario

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def limite_prestamos(self) -> int:
        return self.__limite_prestamos

    @property
    def prestamos_activos(self) -> list:
        return self.__prestamos_activos

    def tiene_cupo(self) -> bool:
        return len(self.__prestamos_activos) < self.__limite_prestamos

    def registrar_prestamo(self, prestamo: Prestamo) -> None:
        self.__prestamos_activos.append(prestamo)

    def quitar_prestamo(self, prestamo: Prestamo) -> None:
        if prestamo in self.__prestamos_activos:
            self.__prestamos_activos.remove(prestamo)
