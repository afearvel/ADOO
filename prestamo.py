from datetime import datetime
from copia import Copia
from ADOO.usuario import Usuario


class Prestamo:
    def __init__(self, copia: Copia, usuario: Usuario, fecha_inicio: datetime, fecha_vencimiento: datetime):
        self.__copia: Copia = copia
        self.__usuario: Usuario = usuario
        self.__fecha_inicio: datetime = fecha_inicio
        self.__fecha_vencimiento: datetime = fecha_vencimiento
        self.__fecha_devolucion: datetime | None = None

    @property
    def copia(self) -> Copia:
        return self.__copia

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def fecha_inicio(self) -> datetime:
        return self.__fecha_inicio

    @property
    def fecha_vencimiento(self) -> datetime:
        return self.__fecha_vencimiento

    @property
    def fecha_devolucion(self) -> datetime | None:
        return self.__fecha_devolucion

    def ejecutar_prestamo(self) -> bool:
        if self.__usuario.tiene_cupo():
            if self.__copia.prestar():
                self.__usuario.registrar_prestamo(self)
                return True
        return False

    def finalizar_devolucion(self) -> None:
        self.__fecha_devolucion = datetime.now()
        self.__copia.devolver()
        self.__usuario.quitar_prestamo(self)
