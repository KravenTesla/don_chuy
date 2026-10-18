# src/producto.py
from abc import ABC, abstractmethod

class Producto(ABC):
    """Clase abstracta base para todos los productos de la tiendita."""
    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    @property
    def id_producto(self) -> int:
        return self._id_producto

    def reducir_stock(self, cantidad: int) -> bool:
        if 0 <= cantidad <= self._stock:
            self._stock -= cantidad
            return True
        return False

    @abstractmethod
    def mostrar_detalles(self) -> str:
        """Cada subclase define cómo mostrar sus detalles."""
        ...