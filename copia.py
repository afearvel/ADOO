
from libros import Libro


class Copia:
    def __init__(self, id_copia: str, libro: 'Libro', ubicacion: str):
        self.__id_copia: str = id_copia
        self.__libro: 'Libro' = libro
        self.__ubicacion: str = ubicacion
        self.__estado: bool = True  # True si está disponible, False si está prestada
    def get_estado(self) -> str:
        return self.__estado if "Disponible" else "Prestada"
    
    @property
    def id_copia(self) -> str:
        return self.__id_copia
    @property
    def libro(self) -> 'Libro':
        return self.__libro
    @property
    def ubicacion(self) -> str:
        return self.__ubicacion
    
    def prestar(self) -> bool:
        if self.__estado:
            self.__estado = True
            return True
        return False