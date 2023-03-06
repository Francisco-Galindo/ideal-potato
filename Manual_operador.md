# MANUAL PARA EL OPERADOR DE LA MÁQUINA

![image](https://user-images.githubusercontent.com/125548315/223007898-51bf29c4-5e5c-4f41-848a-d266db2d220f.png)

### CARACTERISTICAS TECNICAS:
1. Productos disponibles:
La máquina expendedora puede albergar una gran cantidad de productos comercializados en bolsas de polipropileno, así como de botellas de plástico reutilizable amigables con el medio ambiente, el operador debe cuidar que el orden de compra corresponda con el lote de productos asignados para la máquina así como la revisión de fecha de caducidad de los productos.

2. Capacidad de los productos:
Para productos en bolsas de polipropileno el peso mínimo correspondiente al producto debe ser mínimo de 20 gramos (gr) hasta un máximo de 100 gramos (gr).
Para productos en botellas de plástico el volumen mínimo correspondiente al producto debe ser mínimo de 50 mililitros (ml) hasta un máximo de 1000 mililitros (ml).

Sin embargo, el operador puede ingresar por medio del software el peso y volumen del producto según sea el caso.

## CARACTERÍSTICAS GENERALES:
1. Panel de pulsadores y display.
La pantalla inicial de la máquina debería visualizarse de la siguiente manera:
![image](https://user-images.githubusercontent.com/125548315/223023417-7fcb53a8-cf65-4581-934a-43595b8665fe.png)


A continuación, procederemos a elegir la opción número 2 "Ingreso de mantenimiento" para entrar a la opción de mantenimiento.
Posteriormente el operador ingresará la contraseña super secreta proporcionada en el centro de trabajo o por el fabricante del modelo en cuestión de la máquina.
una vez se accede a la interfaz de mantenimiento se mostrará el siguiente menú:
![image](https://user-images.githubusercontent.com/125548315/223023913-c34d6ec6-f9bd-4ce7-b999-a4f3df41ea77.png)

OPCIONES GENERALES.
El operador tiene que elegir a una opción del menú digitando el digito correspondiente:
0. SALIR: Sale de la interfaz de mantenimiento.
1. INGRESO DE PRODUCTO: Programa el ingreso de productos para la máquina y la creación de su código correspondiente. El operador debe ingresar las características: Descripción, marca, fecha de caducidad, unidades a ingresar, precio unitario y orden de compra del producto.
2. EGRESO DE PRODUCTO: Programa el egreso de productos para la máquina. El operador debe ingresar el código del producto, las unidades a retirar y el número de factura.
3. HISTORIAL DE MOVIMIENTOS: Historial de movimientos. El operador debe ingresar el código de un producto para generar su historial.
4. BÚSQUEDA DE PRODUCTO. Permite la búsqueda de un producto dentro del inventario mediante su código.
5. SACAR DINERO DE LA MÁQUINA: Retira dinero de la máquina.
6. AGREGAR DINERO A LA MÁQUINA: Introduce dinero a la máquina.
 
## PUESTA EN MARCHA:
1. Sproceso para ingresar dinero:
a) Para el ingreso de dinero, dirigirse al menú de mantenimiento, posteriormente a la opción 5. SACAR DINERO DE LA MÁQUINA.
b) Ingrese la cantidad de dinero a ingresar, se recomienda como cantidad mínima mil pesos (1000.00 MXN).
c) Ingrese el dinero.

2. proceso para retirar dinero:
a) Para el ingreso de dinero, diríjase al menú de mantenimiento, posteriormente a la opción 6. AGREGAR DINERO A LA MÁQUINA.
b) Ingrese la cantidad de dinero a ingresar, se recomienda como cantidad mínima mil pesos (1000.00 MXN).
c) Ingrese el dinero.

3. proceso para ingresar productos:
a) Para el ingreso de productos, diríjase al menú de mantenimiento, posteriormente a la opción 1. INGRESO DE PRODUCTO.
b) Siga las instrucciones hasta llegar al campo "Ingrese la Cantidad a ingresar del Producto:".
c) Programe el ingreso de productos.

4. proceso para retirar Productos:
a) Para el ingreso de productos, diríjase al menú de mantenimiento, posteriormente a la opción 2. EGRESO DE PRODUCTO.
b) Introduzca el Código del producto a retirar y la cantidad de unidades a retirar de la máquina.
c) Finalmente introduzca el número de factura.

5. proceso para designar códigos:
a) Para designar un nuevo código, diríjase al menú de mantenimiento, posteriormente a la opción 1. INGRESO DE PRODUCTO.
b) Ingrese el nuevo código para el producto.
c) Siga el llenado de datos para el producto.

# ANOMALIAS NO DETECTADAS POR LA MÁQUINA:
1. Anomalías que dejan a la máquina fuera de servicio:
Introducción de caracteres especiales: El operador debe cuidar la introducción del carácter especial coma (" , ") cuando ingresa datos en cualquier campo del menú ya que es posible que se generen errores en la documentación de archivos de compra.

introducción de códigos repetidos: El operador debe evitar la introducción de códigos repetidos ya que la máquina no permite los códigos duplicados y automáticamente actualiza el producto, para evitar este error se recomienda el uso de la función 4. BUSQUEDA DE PRODUCTO.

2. Indicadores de la necesidad de cambiar algún módulo en la máquina:
No hay un proceso de validación en la fecha de caducidad de los productos, por lo que el operador debe revisar este proceso manualmente.

## UTILIDAD DE LAS FUNCIONES DE PROGRAMACIÓN:

## **Carga Inicial de productos:**

Al iniciarse el programa carga una lista inicial de productos desde un archivo llamado Productos.csv, la estructura de este archivo debe ser la siguiente:
| Tipo(Botana/Bebida) |Nombre |Precio|Marca|Fecha de caducidad|Peso / Volumen|Cantidad|
|--|--|--|--|--|--|--|


## **Clases:**

 - **Producto:**
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
	 *nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str) y  cantidad (int). 
	 Crea una instancia de "Producto".
	 - set_codigo(str): Modifica el código de un producto, recibe como argumento el código nuevo (str).
	 - get_precio(): Regresa el precio de un objeto.
	 - set_precio(str): permite modificar el precio de un producto, recibe como argumento el nuevo precio. 
	 - __ str __: Regresa el nombre del producto al imprimirlo. 
	 - cantidad (getter): Regresa la cantidad de un objeto que hay en la máquina expendedora.
	 - cantidad (setter): Permite modificar la cantidad de un producto en la máquina expendedora.

 - **Botana**:
 Hereda de la clase "Producto", describe las botanas almacenadas en la máquina expendedora.
 Atributos:
	 - Hereda los atributos de "Producto".
	 - peso (str): Peso del producto en gramos (gr).

	Métodos:
	 - Hereda los métodos de  "Producto".
	 - __ init __: Constructor, recibe como argumento:
	 *nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str),  cantidad (int), peso(str).
	 Crea una instancia de "Botana".
 - **Bebida**
 Hereda de la clase "Producto", describe las bebidas almacenadas en la máquina expendedora.
 Atributos:
	 - Hereda los atributos de "Producto".
	 - volumen (str): Volumen del producto en mililitros (ml).

	Métodos:
	 - Hereda los métodos de  "Producto"
	 - __ init __: Constructor, recibe como argumento:
	 *nombre* (str), *precio* (float), *codigo* (str), *marca* (str), *caducidad* (str),  cantidad (int), peso(str).
	 Crea una instancia de "Bebida".

-  **Inventario**

	La clase Inventario describe el contenido de los productos almacenados en la máquina expendedora.

	Atributos:

	- ListaProducto: Mantiene una lista de los productos almacenados en la máquina expendedora.
	- ListaHistorial: Almacena las entradas del historial.

	Métodos:
	- mostrarListaProductos: Muestra en pantalla el nombre, código y precio de los productos disponibles.
	- Carga_csv: Carga la lista de productos desde un archivo csv ("Productos.csv") y regresa una lista de productos.
	- BuscarNombre: Regresa el nombre de un producto; recibe como argumento el código del producto(str).
	- BuscarProducto: Regresa una lista con la información del producto; recibe como argumento el código del producto (str).
	- mostrarProducto: Muestra en pantalla los datos obtenidos por la función BuscarProducto; recibe como argumento el código del producto (str)
	- Ingreso: Permite al usuario ingresar nuevos productos y actualizar los productos existentes.
	- Egreso: Permite retirar productos.
	- ActualizarSaldo: Actualiza la cantidad que hay de algún producto. Es llamada por las funciones Ingreso y Egreso; recibe como argumento código (str), TipoMovimiento(str, Ingreso/Egreso), cantidad (int).
	- Compra_Usuario: Actualiza el historial cuando el usuario hace una compra; recibe como argumento el código del producto (str)
	- Historial: Imprime el historial de un producto.

 - **Maquina**
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
	
