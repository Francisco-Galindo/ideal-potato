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
        """Carga un archivo "Producto.csv" y regresa una lista de productos.\n
La estructura del archivo debe ser:  Tipo,Nombre,Precio,Codigo,Marca,Fecha_Caducidad,Peso/Volumen,Cantidad"""

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


    def BuscarNombre(self, Codigo):
        """
        It searches for a product name based on a product code.

        :param Codigo: The code of the product
        :return: The name of the product.
        """

        producto = self.BuscarProducto(Codigo)
        if producto:
            return producto.nombre

        return ''

    def BuscarProducto(self, Codigo):
        """
        It searches for a product in the list.

        :param Codigo: Product code
        :return: A list of the product's information.
        """

        for CodeProducto in self.ListaProducto:
            if CodeProducto.codigo == Codigo:
                return CodeProducto

        return None

    def BuscarProducto2(self, Codigo):
        """
        If the first element of the list is equal to the code, then print the elements of the list.

        :param Codigo: The code of the product
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
        It removes the product from the list, then adds it back with the updated values.

        :param Codigo: Product code
        :param TipoMovimiento: It's a string that can be either "Ingreso" or "Salida"
        :param Cantidad: Quantity
        """

        producto = self.BuscarProducto(Codigo)
        if not producto:
            return

        if TipoMovimiento == 'Ingreso':
            producto.cantidad += float(Cantidad)
            print('Ingreso', producto.cantidad)
            print('Ingreso', producto.cantidad * producto.get_precio())
        elif TipoMovimiento == 'Egreso':
            producto.cantidad -= float(Cantidad)
            print('Productos Restantes: ', producto.cantidad)
            print('Costo de los productos restantes: ', producto.cantidad * producto.get_precio())
        else:
            producto.cantidad -= float(Cantidad)


    def Ingreso(self):
        """
        A function that allows you to enter the product code and description.
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

        Cantidad = float(input("Ingrese la Cantidad a ingresar del Producto: "))
        Precio = float(input("Ingrese el Precio Unitario: "))
        Orden = input("Ingrese el Número de Orden de Compra: ")

        if not self.BuscarProducto(Codigo):
            producto = None
            if tipo == 'botana':
                producto = Botana(Nombre, Precio, Codigo, marca, fecha, volpeso, Cantidad)
            else:
                producto = Bebida(Nombre, Precio, Codigo, marca, fecha, volpeso, Cantidad)

            # print(producto)
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
        # It's asking for the product code and then it's searching for the product in the list.
        Historial = []
        print('')
        print('****** RETIRO DE PRODUCTO ******')
        Codigo=input("Ingrese el Código del Producto: ")
        producto = self.BuscarProducto(Codigo)
        # It's asking for the product code and then it's searching for the product in the list.
        if producto:
            print("Nombre del Producto: ", producto.nombre)
            print("Costo del Producto: ", producto.get_precio())
            Cantidad1 = float(input("Ingrese la Cantidad a Retirar: "))
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

        # It's printing a message if the product is not in the list.
        else:
            print("¡¡Producto No existe en la base de datos!!")

    def Compra_Usuario(self, Codigo):
        #aqui para poder ingresar alguna variable para la compra.
        #se relaciona con la linea 195
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

            self.ActualizarSaldo(Codigo,'Compra')

            return producto

        else:
            return None


    def Historial(self):
        """
        It prints the history of a product.
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
