from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, producto_ID, nombre, precio, stock):
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
        

class Inventario:
    # Inventario de productos
    def __init__(self, ids):
        self.__productos = []
        self.ids = 0

    def agregarProducto(self):
        # Inputs
        print("===== Producto =====")
        input_1 = input("Nombre: ")
        input_2 = int(input("Stock: "))
        input_3 = input("Precio (MXN): ")
        self.ids += 1
        self.__productos.append(Producto(input_1, input_2, input_3, ids)) 

    # Buscar y mostrar el producto
    def buscar_producto_ID(self):
        print("== Buscar producto ID ==")
        input_ID = int(input("ID: "))

        for i in range(len(self.__productos)):
            if self.__productos[i] == input_ID:
                Producto.mostrar_datos(input_ID)

    # Recorrer cada producto
    def mostrar_inventario(self):
        for i in range(len(self.__productos)):
            print(self.__productos[i])

    def reducir_stock(self):
        print("== Reducir Stock por ID ==")
        Input_ID = input("Ingrese el ID: ")
        for i in range(len(self.__productos)):
            if  self.__productos[i] == Id_ingresado:
                self.__productos.remove(i) 
                
class Venta:
    def __init__(self, id_venta, cliente, productos, total):
        self.__id_venta = id_venta
        self.__cliente = cliente
        self.__productos = tuple[Producto, int]
        self.__total = total

    def agregar_item(self):
        pass

    def calcular_total(self):
        pass

    def procesar_pago(self):
        pass 
