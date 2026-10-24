from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio, stock, producto_ID):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__producto_ID = producto_ID

    @abstractmethod
    def reducir_stock(self):
        pass
    
    @abstractmethod
    def mostrar_detalles(self):
        pass
        
class ProductoConcreto(Producto):
    def reducir_stock(self, cantidad):
        # Implementación básica del método abstracto
        pass

    def mostrar_detalles(self):
        # Implementación para mostrar los datos
        print(f"ID: {self.producto_ID} | Nombre: {self._Producto__nombre} | Precio: ${self._Producto__precio} | Stock: {self._Producto__stock}")

class Inventario:
    # Inventario de productos
    def __init__(self, ids):
        self.productos = []
        self.ids = 0

    def agregarProducto(self):
        # Inputs
        print("===== Producto =====")
        input_1 = input("Nombre: ")
        input_2 = int(input("Stock: "))
        input_3 = input("Precio (MXN): ")
        self.ids += 1
        nuevo_producto = ProductoConcreto(self.ids, nombre, precio, stock)
        self.productos.append(nuevo_producto) 

    # Buscar y mostrar el producto
    def buscar_producto_ID(self):
        print("== Buscar producto ID ==")
        input_ID = int(input("ID: "))

        for i in range(len(self.productos)):
            if self.productos[i] == input_ID:
                i.mostrar_detalles(input_ID)

    # Recorrer cada producto
    def mostrar_inventario(self):
        for i in range(len(self.productos)):
            print(i)

    def reducir_stock(self):
        print("== Reducir Stock por ID ==")
        Input_ID = input("Ingrese el ID: ")
        for i in range(len(self.productos)):
            if  self.productos[i] == Id_ingresado:
                self.productos.remove(i) 
                
# class Venta:
#     def __init__(self, id_venta, cliente, productos, total):
#         self.__id_venta = id_venta
#         self.__cliente = cliente
#         self.__productos = tuple[Producto, int]
#         self.__total = total

#     def agregar_item(self):
#         pass

#     def calcular_total(self):
#         pass

#     def procesar_pago(self):
#         pass 

# Instanciar el producto 

# Inicializar inventario instanciando el inventario
Inventarios = Inventario() 
print(Inventarios.productos)
