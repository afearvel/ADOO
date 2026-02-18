from types import list, opcional

class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__copias: list[Copia] = []

        @property
        def isbn(self) -> str:
            return self.__isbn
        @property
        def titulo(self) -> str:
            return self.__titulo
        @property
        def autor(self) -> str:
            return self.__autor
        

    def agregar_copia(self, id_copia: str, ubicacion: str) -> Copia:
        copia = Copia(id_copia, self, ubicacion)
        self.__copias.append(copia)
        return copia
    
    def obtener_disponibles(self) -> list[Copia]:
        return self.__copias
    
    