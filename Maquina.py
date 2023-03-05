from Producto import *

class Maquina():

    """ Clase que representa la máquina expendedora, describe las interacciones
    que una persona puede tener con la misma.
    Recibe: dinero(float), password(str)"""

    def __init__(self, dinero, password):
        self.__pasword = password
        self.__dinero = dinero
        self.__atascada = False
        self.__sesionIniciada = False

        self.__currPago = 0
        self.__total = 0

        self.__listaCodigos = []

        self.inventario = None
        self.seleccion = None
        self.charola = None

    def recibirPago(self):
        debePagar = True

        print(f"Son ${self.__total}")

        while debePagar:

            try:
                pago = float(input("Introduzca su dinero: "))
                self.__currPago += pago
            except ValueError:
                print("Necesito una cantidad válida de dinero...")

            if self.__currPago >= self.__total:
                debePagar = False
            else:
                print(f"Todavía faltan ${self.__total - self.__currPago}...")


    def darCambio(self):
        # TODO: Obtener precio total de los productos que se solicitan

        cambio = self.__currPago - self.__total

        if cambio > 0:
            print(f"Su cambio es de ${cambio}")

    def darProductos(self):
        # TODO: Obtener producto del inventario conforme a pila de productos
        while self.__listaCodigos:
            codigo = self.__listaCodigos.pop()

            # producto = self.inventario.obtenerProducto(codigo)
            producto = codigo
            if producto:
                print(f"Aquí está su {producto}")
            else:
                print("No se pudo sacar el producto")
                break

    def imprimirTicket(self):
        print("\nImprimiendo ticket...")
        # TODO: Imprimir el ticket

    # TODO
    def guardarEnHistorial(self):
        pass

    def hacerTransaccion(self):
        # TODO Leer opciones
        line = input("Ingrese la lista de productos a comprar (separado por comas: A,B,C,...): ")
        codigos = line.split(',')
        # TODO Calcular total y agregar productos a la pila de productos
        # Va a fallar eventualmente cuando se pidan más de un producto de los que hay
        self.__total = 0
        for codigo in codigos:
            codigo = codigo.strip()
            if codigo:
                # self.__total += self.inventario.buscarProducto().getPrecio()
                self.__total += 20
                self.__listaCodigos.append(codigo)

        self.recibirPago()
        if self.__currPago >= self.__total:

            self.darCambio()

            # Entregar productos
            self.darProductos()

            self.imprimirTicket()
        else:
            print("No has pagado lo suficiente...")

    def acceder(self, passwd):
        if passwd == self.__pasword:
            self.__sesionIniciada = True
        else:
            self.__sesionIniciada = False

    def cambiarContra(self, passwd):
        if self.__sesionIniciada:
            self.__pasword = passwd
        else:
            return

    def desatascar(self):
        if self.__sesionIniciada:
            print("Desatascando...")
            if self.__atascada:
                self.__atascada = False
            else:
                print("La máquina no está atascada...")
