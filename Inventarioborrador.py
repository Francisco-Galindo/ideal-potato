ListaProducto=[]
ListaHistorial=[]
CantidadProducto=[] 
Cantidad=[] 
 
def Buscar(Codigo): #codigo me ayuda a buscar el codigo del producto
    """
    It returns the length of the list

    
    :param Codigo: The code of the product
    :return: The length of the list.
    """
    Tamaño_Lista = len (ListaProducto) #me retorna la longitud de la lista.
    return Tamaño_Lista
 
#Buscamos el nombre del producto a consultar basandonos en el codigo. 
def BuscarNombre(Codigo): #esta cosa igual puede heredar de clase producto 
    #crear un diccionario de claves y nombres y heredar solo la propiedad de 
    # nombre
    """
    It searches for a product name based on a product code.
    
    :param Codigo: The code of the product
    :return: The name of the product.
    """
    Tamaño_Lista = len(ListaProducto)
    if Tamaño_Lista == 0:
        Nombre = ''
    else:
        for CodeProducto in ListaProducto:
            if CodeProducto[0] == Codigo:
                Nombre = CodeProducto[1]
            else:
                Nombre=''
    return Nombre
 
#Extraemos todos los datos del producto a buscar
def BuscarProducto(Codigo): #AQUI PUEDO PONER LA CLASE PRODUCTO DE LALO 1
    """
    It searches for a product in the list.
    
    :param Codigo: Product code
    :return: A list of the product's information.
    """
    Producto = [] #De hecho puedo intentar colocar un diccionario. con 5 listas
    #adentro que seria nombre, precio, codigo, marca, fecha de caducidad. 
    ##Aqui puedo heredar la clase de lalo y añadirle opciones.
    for CantidadProducto in ListaProducto:
        if CantidadProducto[0] == Codigo:
            Producto.append(CantidadProducto[0])
            Producto.append(CantidadProducto[1])
            Producto.append(CantidadProducto[2])
            Producto.append(CantidadProducto[3])
            Producto.append(CantidadProducto[4])
    return Producto #return diccionario.
 
#Mostramos los datos del producto buscado
def BuscarProducto2(Codigo): #Aqui puedo heredar la clase de lalo y la 
    #funcionalidad de nombre, costo y añadirle opciones como product disponible y
    #costo total de lo que queda 2
    """
    If the first element of the list is equal to the code, then print the elements of the list.
    
    :param Codigo: The code of the product
    """
    Producto = [] #igual lo mejor seria con un diccionario
    for Producto in ListaProducto:
        if Producto[0] == Codigo:
            print("Codigo: ",Producto[0])
            print("Nombre: ",Producto[1])
            print("Cantidad de producto Disponible: ",Producto[2])
            print("Costo Por unidad: ",Producto[3])
            print("Costo Total de los productos en inventario: ",Producto[4])
 
#Actualizamos el Saldo del Producto deacuerdo al movimiento (Ingreso/Retiro)
def ActualizarSaldo(Codigo,TipoMovimiento,Cantidad,Total):
    """
    It removes the product from the list, then adds it back with the updated values.
    
    :param Codigo: Product code
    :param TipoMovimiento: It's a string that can be either "Ingreso" or "Salida"
    :param Cantidad: Quantity
    :param Total: Total amount of the product
    """
   #ESTA FUNCION BASICAMENTE ME HACE LA EL CALCULO/OPERACION DE METER Y SACAR CANTIDADES 
   #DE PRODUCTOS CREO QUE SERIA BUENA IDEA QUE AQUI INCLUYA EL PROCESO DEL USUARIO
   #TENDRIA QUE AGREGAR LA FUNCIONALIDAD DEF DAR PRODUCTO DE LA CLASE DE 
   #FRANCISCO  O MEJOR DICHO QUE EL ACCEDA A REMOVER UN ELEMENTO DEL INVENTARIO.
    Producto=[] 
    for CantidadProducto in ListaProducto:
        if CantidadProducto[0] == Codigo:
            ListaProducto.remove(CantidadProducto)
            CantidadTotal = float(CantidadProducto[2])
            TotalM = float(CantidadProducto[4])
            if TipoMovimiento == 'Ingreso':
                CantidadTotal = CantidadTotal + float(Cantidad)
                TotalM = TotalM + float(Total)
                print('Ingreso',CantidadTotal)
                print('Ingreso',TotalM)
            else:
                CantidadTotal=CantidadTotal-float(Cantidad)
                TotalM =TotalM - float(Total)
                print('Productos Restantes: ',CantidadTotal)
                print('Costo de los productos restantes: ',TotalM)
            if CantidadTotal == 0:
                Costo = 0
            else:
                Costo = TotalM/CantidadTotal
            Producto.append(CantidadProducto[0])
            Producto.append(CantidadProducto[1])
            Producto.append(CantidadTotal)
            Producto.append(Costo)
            Producto.append(TotalM)
            ListaProducto.append(Producto)
 
#Realizamos el Ingreso de Producto

def Ingreso():# DEL ALGUNA MANERA AQUI ES PARA AGREGRAR LOS ELEMENTOS AL
    #DICCIONARIO Y DE ALGUNA MANERA PUES AQUI NO JUEGA EL USUARIO.
    #SE GENERA UN DOCUMENTO PARA LAS ORDENES DE COMPRA
    """
    A function that allows you to enter the product code and description.
    """
    Historial = []
    print('')
    print('****** INGRESO DE PRODUCTO ******')
    Codigo = input("Ingrese el Código del Producto: ")
    Nombre = BuscarNombre(Codigo)
    if Nombre == '':
        Nombre = input("Ingrese la Descripción del Producto: ")
  # It's asking for the product name if it's not in the list.
    else:
        Nombre = BuscarNombre(Codigo)
        print("Nombre del Producto: ",Nombre)
    Cantidad = input("Ingrese la Cantidad a ingresar del Producto: ")
    Precio = input("Ingrese el Precio Unitario: ")
    Total = float(Cantidad)*float(Precio)
    Orden = input("Ingrese el Número de Orden de Compra: ")
   # It's adding the product to the list.
    if Buscar(Codigo) == 0:
        CantidadProducto.append(Codigo)
        CantidadProducto.append(Nombre)
        CantidadProducto.append(Cantidad)
        CantidadProducto.append(Precio)
        CantidadProducto.append(Total)
        ListaProducto.append(CantidadProducto)
   # It's adding the product to the list.
    else:
        ActualizarSaldo(Codigo,'Ingreso',Cantidad,Total)
    Historial.append("Ingreso")
    Historial.append(Codigo)
    Historial.append(Nombre)
    Historial.append(Cantidad)
    Historial.append(Precio)
    Historial.append(Total)
    Historial.append(Orden)
    ListaHistorial.append(Historial)
    print('')
 
#Realizamos el Egreso (Venta)
def Egreso(): #DE ALGUNA MANERA EL OPERADOR RETIRA PRODUCTO CADUCO,
    #ENTONCES UNA NUEVA FUNCION PARA LA FECHA DE EXPIRACION QUE EVALUE QUE PRODUCTOS
    #ESTAN EXPIRADOS Y ASI RETIRARLOS AL MENOS AQUI TAMPOCO ENTRA EL USUARIO
    #PERO SE TIENE QUE ACCEDER AL INVENTARIO QUE TOCA EL USUARIO.
    #DOCUMENTO PARA LA FACTURA.
   # It's asking for the product code and then it's searching for the product in the list.
    Historial = []
    print('')
    print('****** RETIRO DE PRODUCTO ******')
    Codigo=input("Ingrese el Código del Producto: ")
    Cantidad = BuscarProducto(Codigo)
 # It's asking for the product code and then it's searching for the product in the list.
    if len(Cantidad)>0:
        print("Nombre del Producto: ",Cantidad[1])
        print("Costo del Producto: ",Cantidad[3])
        Cantidad1 = float(input("Ingrese la Cantidad a Retirar: "))
        Total = float(Cantidad[3])*Cantidad1
        Orden = input("Ingrese el Número de Factura: ")
        Historial.append("Egreso")
        Historial.append(Codigo)
        Historial.append(Cantidad[1])
        Historial.append(Cantidad1)
        Historial.append(float(Cantidad[3]))
        Historial.append(Total)
        Historial.append(Orden)
        ActualizarSaldo(Codigo,'Egreso',Cantidad1,Total)
        ListaHistorial.append(Historial)
        print('')
   # It's printing a message if the product is not in the list.
    else:
        print("¡¡Producto No existe en la base de datos!!")
 
#Mostramos el Historial de un Producto. QUE IMPRIMA LA HISTORIA DE UN
#PRODUCTO DE ALGUNA MANERA PRINCIPALMENTE EL RETIRO Y EGRESO POR PARTE DEL
#OPERADOR Y LOS USUARIOS Y HACERLO UN DOCUMENTO.
def Historial():
    """
    It prints the history of a product.
    """
    Historial = []
    Producto = []
    print('')
    print('****** HISTORIAL DEL PRODUCTO ******')
    print('')
    Codigo = input("Ingrese el Código del Producto: ")
    print('')
    print('CODIGO','NOMBRE','TIPO MOVIMIENTO','CANTIDAD','COSTO','DOCUMENTO',sep = "\t")
    if BuscarNombre(Codigo) =='':
        print("Código No Existente")
    else:
        for Historial in ListaHistorial:
            if Historial[1] == Codigo:
                print(Historial[1],Historial[2],Historial[0],Historial[3],Historial[4],Historial[6],sep = "\t")
    print('')
 
 
# Menú Principal
# It's a menu that allows you to enter the product code and description.
while (1):
    print('*****INVENTARIO*****')
    print('')
    print('****** Menú Principal ******')
    print('0. SALIR')
    print('1. INGRESO DE PRODUCTO')
    print('2. EGRESO DE PRODUCTO') 
    #PRODUCTOS COMPRADOS POR LOS USUARIOS
    #PRODUCTOS CADUCACADOS
    print('3. HISTORIAL DE MOVIMIENTOS')
    print('4. BUSQUEDA DE PRODUCTO')
    opcion=input('Digitar una Opción: ')
    if opcion =='0':
        print("Gracias por usar nuestro servicio. ¡Hasta luego!")
        break
    elif opcion == '1':
        Ingreso()
    elif opcion == '2':
        Egreso()
    elif opcion == '3':
        Historial()
    elif opcion == '4':
        print('')
        print('****** BUSQUEDA DE PRODUCTO ******')
        Codigo = input("Ingrese el Código del Producto: ")
        BuscarProducto2(Codigo)
    else:
        print('Opción no válida. Intente nuevamente')