import csv
from Producto import *

class Inventario:

    def __init__(self):
        self.ListaProducto=[]
        self.ListaHistorial=[]

        self.ListaProducto = self.Carga_csv()

    def mostrarListaProductos(self):
        print("==============Lista de productos==============")
        print("Producto\t\tCódigo\t\tPrecio\n")
        for producto in self.ListaProducto:
            print(f"{producto.nombre}\t\t{producto.codigo}\t\t${producto.get_precio():.2f}")
        print("==============================================\n")

    def Carga_csv(self)->list:
        """
        Carga un archivo "Producto.csv" y regresa una lista de productos.

        La estructura del archivo debe ser:
            Tipo,Nombre,Precio,Codigo,Marca,Fecha_Caducidad,Peso/Volumen,Cantidad
        """

        productos=[]
        with open("Productos.csv","r") as f:
            archivo=csv.DictReader(f)

            for linea in archivo:
                if linea["Tipo"]=="Bebida":
                    productos.append(
                        Bebida(linea["Nombre"],
                               float(linea["Precio"]),
                               linea["Codigo"],
                               linea["Marca"],
                               linea["Fecha_Caducidad"],
                               linea["Peso/Volumen"],
                               float(linea["Cantidad"])
                        )
                    )
                elif linea["Tipo"]=="Botana":
                    productos.append(
                        Botana(linea["Nombre"],
                               float(linea["Precio"]),
                               linea["Codigo"],
                               linea["Marca"],
                               linea["Fecha_Caducidad"],
                               linea["Peso/Volumen"],
                               float(linea["Cantidad"])
                        )
                    )
            return productos

    def guardarCSV(self):
        """
        Guarda el estado de la lista de archivos en el archivo csv correspondiente

        """
        with open("Productos.csv","w") as f:
            f.write("Tipo,Nombre,Precio,Codigo,Marca,Fecha_Caducidad,Peso/Volumen,Cantidad\n")
            for producto in self.ListaProducto:
                if isinstance(producto, Botana):
                    f.write(f"Botana,{producto.nombre},{producto.get_precio()},{producto.codigo},{producto.marca},{producto.fechacad},{producto.peso},{producto.cantidad}\n")
                elif isinstance(producto, Bebida):
                    f.write(f"Bebida,{producto.nombre},{producto.get_precio()},{producto.codigo},{producto.marca},{producto.fechacad},{producto.volumen},{producto.cantidad}\n")




    def BuscarNombre(self, Codigo):
        """
        Busca un producto con el código dado y devuelve su nombre si lo encuentra

        :param Codigo: Código del producto
        :return: El nombre del producto
        """

        producto = self.BuscarProducto(Codigo)
        if producto:
            return producto.nombre

        return ''

    def BuscarProducto(self, Codigo):
        """
        Busca un producto en la lista

        :param Codigo: Código del producto
        :return: El objeto correspondiente al producto
        """

        for CodeProducto in self.ListaProducto:
            if CodeProducto.codigo == Codigo:
                return CodeProducto

        return None

    def mostrarProducto(self, Codigo):
        """
        Imprime la información del producto si se encuentra en la lista

        :param Codigo: Código del producto
        """

        producto = self.BuscarProducto(Codigo)
        print(producto)
        if not producto:
            return

        print("Codigo: ", producto.codigo)
        print("Nombre: ", producto.nombre)
        print("Cantidad de producto Disponible: ", producto.cantidad)
        print("Costo Por unidad: ", producto.get_precio())
        print("Costo Total de los productos en inventario: ", producto.cantidad * producto.get_precio())

    def ActualizarSaldo(self, Codigo, TipoMovimiento, Cantidad = 1):
        """
        Toma el producto del código dado y actualiza su cantidad dependiendo
        de los valores recibidos, también guarda el movimiento en el historial.

        :param Codigo: Código del producto
        :param TipoMovimiento: El tipo del movimiento ('Ingreso', 'Egreso', 'Compra')
        :param Cantidad: Cantidad de cambio
        """

        producto = self.BuscarProducto(Codigo)
        if not producto:
            return

        if TipoMovimiento == 'Ingreso':
            producto.cantidad += float(Cantidad)
            print('Ingreso', producto.cantidad)
            print('Ingreso', producto.cantidad * producto.get_precio())
        elif TipoMovimiento == 'Egreso':
            if producto.cantidad - float(Cantidad) >= 0:
                producto.cantidad -= float(Cantidad)
                print('Productos Restantes: ', producto.cantidad)
                print('Costo de los productos restantes: ', producto.cantidad * producto.get_precio())
            else:
                print(f'No hay suficiente {producto} para realizar la operación')
                return False
        else:
            if producto.cantidad - float(Cantidad) >= 0:
                producto.cantidad -= float(Cantidad)
            else:
                print(f'Ya no hay {producto} :(')
                return False

        self.guardarCSV()
        return True

    def Ingreso(self):
        """
        Pide los datos para actualizar y agregar cantidad a un producto ya
        existente o crea uno nuevo si todavía no existe.
        """

        Historial = []

        print('\n****** INGRESO DE PRODUCTO ******')
        Codigo = input("Ingrese el Código del Producto: ")

        Nombre = self.BuscarNombre(Codigo)
        if Nombre == '':
            Nombre = input("Ingrese la Descripción del Producto: ")
            marca = input("Ingrese la marca del Producto: ")
            fecha = input("Ingrese la fecha de caducidad del Producto: ")
            tipo = input("Se trata de una botana o de una bebida? (botana, bebida): ").lower().strip()
            volpeso = input("Volumen o peso (500ml, 60g): ")
        else:
            print("Nombre del Producto: ",Nombre)

        Cantidad = None
        Precio = None
        try:
            Cantidad = float(input("Ingrese la Cantidad a ingresar del Producto: "))
            Precio = float(input("Ingrese el Precio Unitario: "))
        except ValueError:
            print("Necesito valores numéricos...")
            return
        Orden = input("Ingrese el Número de Orden de Compra: ")

        if not self.BuscarProducto(Codigo):
            producto = None
            if tipo == 'botana':
                producto = Botana(Nombre, Precio, Codigo, marca, fecha, volpeso, Cantidad)
            else:
                producto = Bebida(Nombre, Precio, Codigo, marca, fecha, volpeso, Cantidad)

            self.ListaProducto.append(producto)
        else:
            self.ActualizarSaldo(Codigo, 'Ingreso', Cantidad)

        Historial.append('Ingreso')
        Historial.append(Codigo)
        Historial.append(Nombre)
        Historial.append(Cantidad)
        Historial.append(Precio)
        Historial.append(Orden)
        self.ListaHistorial.append(Historial)
        print('')

    def Egreso(self):
        """
        Pide los datos para actualizar y quitar cantidad a un producto ya
        existente.
        """

        Historial = []

        print('\n****** RETIRO DE PRODUCTO ******')
        Codigo=input("Ingrese el Código del Producto: ")
        producto = self.BuscarProducto(Codigo)

        if producto:
            print("Nombre del Producto: ", producto.nombre)
            print("Costo del Producto: ", producto.get_precio())
            Cantidad1 = None
            try:
                Cantidad1 = float(input("Ingrese la Cantidad a Retirar: "))
            except ValueError:
                print("Necesito valores numéricos...")
                return
            Orden = input("Ingrese el Número de Factura: ")
            Historial.append("Egreso")
            Historial.append(Codigo)
            Historial.append(producto.nombre)
            Historial.append(Cantidad1)
            Historial.append(producto.get_precio())
            Historial.append(producto.get_precio() * Cantidad1)
            Historial.append(Orden)
            self.ActualizarSaldo(Codigo,'Egreso',Cantidad1)
            self.ListaHistorial.append(Historial)
            print('')

        else:
            print("¡¡El producto no existe en la base de datos!!")

    def Compra_Usuario(self, Codigo):
        """
        Saca un producto del inventario para representar la compra del usuario.
        Se guarda en el historial el movimiento
        """

        producto = self.BuscarProducto(Codigo)

        Historial = []
        if producto:

            Historial.append("Compra")
            Historial.append(Codigo)
            Historial.append(producto.nombre)
            Historial.append(1)
            Historial.append(producto.get_precio())
            Historial.append('')
            self.ListaHistorial.append(Historial)

            if self.ActualizarSaldo(Codigo,'Compra'):
                return producto

        return None


    def Historial(self):
        """
        Imprime el historial de movimientos de un producto
        """
        Historial = []
        Producto = []
        print('\n****** HISTORIAL DEL PRODUCTO ******\n')
        Codigo = input("Ingrese el Código del Producto: ")
        print('\nCODIGO','NOMBRE','TIPO MOVIMIENTO','CANTIDAD','COSTO','DOCUMENTO',sep = "\t")
        if self.BuscarNombre(Codigo) =='':
            print("Código No Existente")
        else:
            for Historial in self.ListaHistorial:
                if Historial[1] == Codigo:
                    print(Historial[1],Historial[2],Historial[0],Historial[3],Historial[4],Historial[5],sep = "\t")
        print('')
