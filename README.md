# ideal-potato
Proyecto Final del curso de UNICA: Fundamentos de Programación y Generación de Entornos Virtuales Gen. 82

## **Carga Inicial de productos:**

Al iniciarse el programa carga una lista inicial de productos desde un archivo llamado Productos.csv, la estructura de este archivo debe ser la siguiente:
| Tipo(Botana/Bebida) |Nombre |Precio|Marca|Fecha de caducidad|Peso / Volumen|Cantidad|
|--|--|--|--|--|--|--|


## **Clases:**

 - **Producto:**
	Clase para los productos vendidos por la maquina.
	Atributos:
	 - nombre (str): Nombre del producto.
	 - precio (float) (privado): Precio del producto. 
	 - codigo (str): Código alfanumérico del producto.
	 - marca (str): Marca del producto.
	 - fechacad (str): Fecha de caducidad.
	 - cantidad (int): Cantidad del producto en la maquina.

	Métodos:
	 - __ init __: Constructor, recibe como argumento:
	 *nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str) y  cantidad (int). 
	 Crea una instancia de "Producto"
	 - set_codigo(str): Modifica el código de un producto, recibe como argumento el código nuevo (str).
	 - get_precio(): Regresa el precio de un objeto.
	 - set_precio(str): permite modificar el precio de un producto, recibe como argumento el nuevo precio. 
	 - __ str __: Regresa el nombre del producto al imprimirlo. 
	 - cantidad (getter): Regresa la cantidad de un objeto que hay en la maquina
	 - cantidad (setter): Permiet modificar la cantidad de un producto en la mquina

 - **Botana**:
 Hereda de la clase "Producto" ,  describe las botanas almacenadas en la maquina
 Atributos:
	 - Hereda los atributos de "Producto"
	 - peso (str): peso del producto en gramos

	Métodos:
	 - Hereda los metodos de  "Producto"
	 - __ init __: Constructor, recibe como argumento:
	 *nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str),  cantidad (int), peso(str).
	 Crea una instancia de "Botana"
 - **Bebida**
 Hereda de la clase "Producto", describe las bebidas almacenadas en la maquina
 Atributos:
	 - Hereda los atributos de "Producto"
	 - volumen (str): volumen del producto en mililitros

	Métodos:
	 - Hereda los metodos de  "Producto"
	 - __ init __: Constructor, recibe como argumento:
	 *nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str),  cantidad (int), peso(str).
	 Crea una instancia de "Bebida"

#TODO llenar los campos de inventario y maquina

 - **Inventario**
 Descripción:
 Atributos:
	 - List item

	Métodos:
	 - Carga_csv: Carga la lista de productos desde un archivo csv ("Productos.csv") y regresa una lista de productos.

 - **Maquina**
 Descripción:
 Atributos:
	 - List item

	Métodos:
	 - Imprimir_Ticket: Crea un ticket de compra en formato txt <Ticket(Fecha).txt>.
	

	
	
