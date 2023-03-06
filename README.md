
# ideal-potato

Proyecto Final del curso de UNICA: Fundamentos de Programación y Generación de Entornos Virtuales Gen. 82

  

## **Carga Inicial de productos:**

  

Al iniciarse el programa carga una lista inicial de productos desde un archivo llamado Productos.csv, la estructura de este archivo debe ser la siguiente:

| Tipo(Botana/Bebida) |Nombre |Precio|Marca|Fecha de caducidad|Peso / Volumen|Cantidad|

|--|--|--|--|--|--|--|

  
  

## **Clases:**

  

-  **Producto:**

	Clase designada para los productos vendidos por la máquina expendedora.

	Atributos:

	- nombre (str): Nombre del producto.

	- precio (float) (privado): Precio del producto.

	- codigo (str): Código alfanumérico del producto.

	- marca (str): Marca del producto.

	- fechacad (str): Fecha de caducidad.

	- cantidad (int): Cantidad del producto en la máquina expendedora.

  

	Métodos:

	- __ init __: Constructor, recibe como argumento:
*nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str) y cantidad (int).

		Crea una instancia de "Producto".

	- set_codigo(str): Modifica el código de un producto, recibe como argumento el código nuevo (str).

	- get_precio(): Regresa el precio de un objeto.

	- set_precio(str): permite modificar el precio de un producto, recibe como argumento el nuevo precio.

	- __ str __: Regresa el nombre del producto al imprimirlo.

	- cantidad (getter): Regresa la cantidad de un objeto que hay en la máquina expendedora.

	- cantidad (setter): Permite modificar la cantidad de un producto en la máquina expendedora.

  

-  **Botana**:

	Hereda de la clase "Producto", describe las botanas almacenadas en la máquina expendedora.

	Atributos:

	- Hereda los atributos de "Producto".

	- peso (str): Peso del producto en gramos (gr).

  

	Métodos:

	- Hereda los métodos de "Producto".

	- __ init __: Constructor, recibe como argumento:
*nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str), cantidad (int), peso(str).

		Crea una instancia de "Botana".

-  **Bebida**

	Hereda de la clase "Producto", describe las bebidas almacenadas en la máquina expendedora.

	Atributos:

	- Hereda los atributos de "Producto".

	- volumen (str): Volumen del producto en mililitros (ml).

  

	Métodos:

	- Hereda los métodos de "Producto"

	- __ init __: Constructor, recibe como argumento:
	*nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str), cantidad (int), peso(str).

		Crea una instancia de "Bebida".

  

-  **Inventario**

	La clase Inventario describe el el contenido de los productos almacenados en la mquina

	Atributos:

	- ListaProducto: Mantiene una lista de los productos almacenados en la maquina.
	- ListaHistorial: Almacena las entradas del historial
  

	Métodos:

  
	- mostrarListaProductos: Muestra en pantalla el nombre, codigo y precio de los productos disponibles.]
	- Carga_csv: Carga la lista de productos desde un archivo csv ("Productos.csv") y regresa una lista de productos.
	- BuscarNombre: Regresa el nombre de un producto, recibe como argumento el codigo del producto(str).
	- BuscarProducto: Regresa una lista con la informacion del producto, recibe como argumento el codigo del producto (str).
	- mostrarProducto: Muestra en pantalla los datos obtenidos por la funcion BuscarProducto, recibe como argumento el codigo del producto (str)
	- Ingreso: Permite al usuario ingresar nuevos productos y actualizar los productos existentes.
	- Egreso: Permite retirar productos.
	- ActualizarSaldo: Actualiza la cantidad que hay de algun producto, es llamada por las funciones Ingreso y Egreso, recibe como argumento codigo (str), TipoMovimiento(str, Ingreso/Egreso), cantidad (int)
	- Compra_Usuario: Actualiza el historial cuando el usuario hace una compra. Recibe como argumento el codigo del producto (str)
	- Historial: Imprime el historial de un producto.

  

-  **Maquina**

	Clase que representa la máquina expendedora, describe las interacciones que una persona puede tener con ésta.

	Atributos:

	- pasword(privado): Contraseña para acceder a las funciones de administrador.

	- dinero(privado): La cantidad de dinero en la máquina expendedora.

	- atascada(privado): Valor booleano; describe si la máquina expendedora está atascada.

	- currPago(privado) : Almacena el valor del pago de la transacción actual.

	- total(privado): Total a pagar de la transacción actual.

	- sesionIniciada(privado): Valor booleano; describe si la sesión de administrador esta activa.

	- listaCodigos(privado): Lista de los códigos de producto.

	- infoTicket(privado): Almacena el código y precio de los productos seleccionados en la transacción actual.

	- inventario: Instancia de la clase inventario.

  

	Métodos:

	- __ init __: Constructor de la clase Maquina, recibe como argumento: 
	dinero(float), password(str). crea una instancia de la clase Maquina.

	- recibirPago: Permite recibir pagos del usuario, verifica que se ingrese la cantidad correcta de dinero.

	- Imprimir_Ticket: Crea un ticket de compra en formato txt <Ticket(Fecha).txt>.

	- darCambio: Calcula el cambio que se le debe al usuario y verifica que la máquina expendedora tenga suficiente dinero.

	- darProductos: Entrega al usuario los productos que se almacenaron en el atributo "listacodigos ", actualiza la información del ticket (infoTicket).

	- guardarEnHistorial: Almacena el historial de compras.

	- hacerTransaccion: Método que se encarga de llevar a cabo la transacción con el usuario, el usuario ingresa los productos que quiere comprar ingresando sus códigos separados por comas, mantiene la cuenta del total a pagar y de la lista de códigos.

	- acceder: Permite al administrador acceder a las funciones del sistema usando su contraseña por defecto es "123"; se recomienda cambiarla.

	- salir: Permite cerrar la sesión del administrador.

	- cambiarContra: recibe como argumento la nueva contraseña (str) y cambia la contraseña del administrador.

	- desatascar: Permite desatascar la máquina expendedora en caso de ser necesario.
