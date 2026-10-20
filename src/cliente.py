'''
Modelar al comprador: encapsular saldo y exponer pagar() y mostrar_info(). 	
Encapsulamiento. Validacion de estado 	feature/cliente

Cliente modela a la persona que compra en la tiendita. 
Su atributo mas sensible es saldo: ningun codigo externo debe modificarlo directamente, porque eso permitiria "regalar" saldo. 
Por eso se encapsula como privado (-) y solo se expone un getter mediante @property.

El metodo pagar(monto) valida que el monto sea positivo y que el cliente tenga saldo suficiente antes de descontar; 
devuelve True/False para que Venta pueda decidir si la transaccion procede. 
Refuerza el encapsulamiento y la responsabilidad unica: el cliente es dueno de su saldo. 

Getter y setter

Cuando un atributo es privado, el código de afuera no lo puede tocar directamente. Por eso se crean métodos "puerta":

- Getter: un metodo para leer el atributo.
- Setter: un método para modificar el atributo.

'''

class Cliente:
    "Cada cliente solo es dueno de su saldo"
    def __init__(self, nombre: str, saldo: float):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self._nombre = nombre
        self.__saldo = saldo

    @property #getter
    def nombre(self) -> str: #-> Anotacion visual de que regresal parametro que regresa el metodo
        return self._nombre

    @property #setter
    def saldo(self) -> float:
        "Solo lectura, no hay setter, el saldo no se modifica desde fuera"
        return self.__saldo
    def pagar(self, monto:float) -> bool:
        "resta el monto si es q es valido"
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False

    def inf_cliente(self) -> str:
        return f"Cliente: {self._nombre} cuenta con un saldo de: ${self.__saldo:.2f}"
        

if __name__ == "__main__":
    c = Cliente("Arath", 100)
    print(c.pagar(30))          # True, saldo = 70
    print(c.pagar(500))         # False, saldo sin cambios, llama al getter ya que modifica el dato
    print(c.pagar(-10))         # False, monto inválido
    print(c.inf_cliente())