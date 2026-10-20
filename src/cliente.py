'''
Modelar al comprador: encapsular saldo y exponer pagar() y mostrar_info(). 	
Encapsulamiento. Validacion de estado 	feature/cliente

Cliente modela a la persona que compra en la tiendita. 
Su atributo mas sensible es saldo: ningun codigo externo debe modificarlo directamente, porque eso permitiria "regalar" saldo. 
Por eso se encapsula como privado (-) y solo se expone un getter mediante @property.

El metodo pagar(monto) valida que el monto sea positivo y que el cliente tenga saldo suficiente antes de descontar; 
devuelve True/False para que Venta pueda decidir si la transaccion procede. 
Refuerza el encapsulamiento y la responsabilidad unica: el cliente es dueno de su saldo. 

'''