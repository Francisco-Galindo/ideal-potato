class Maquina():

    def __init__(self, dinero, password):
        self.__pasword = password
        self.__dinero = dinero
        self.__atascada = False
        self.__sesionIniciada = False

        self.__currPago = 0
        self.__total = 0

        self.inventario = None
        self.seleccion = None
        self.charola = None

    def recibirPago(self):
        debePagar = True

        while debePagar:

            try:
                pago = float(input("Introduzca su dinero: "))
                self.__currPago += pago
            except ValueError:
                print("Necesito una cantidad válida de dinero...")

            if self.__currPago >= self.__total:
                debePagar = False
            else:
                print("Todavía faltan ${self.__total - self.currPago}...")


    def darCambio(self):
        # TODO: Obtener precio total de los productos que se solicitan

        cambio = self.__currPago - self.__total

        print(f"Su cambio es de {cambio}")

    def darProductos(self):
        # TODO: Obtener producto del inventario conforme a pila de productos
        while True:
            codigo = self.__listaProductosPop()
            if codigo:
                producto = self.inventario.obtenerProducto(codigo)
                if producto:
                    print(f"Aquí está su {producto}")
                else:
                    break
            else:
                break

    def imprimirTicket(self):
        print("Imprimiendo ticket...")
        # TODO: Imprimir el ticket

    # TODO
    def guardarEnHistorial(self):
        pass

    def hacerTransaccion(self):
        # TODO Leer opciones
        line = input("Ingrese la lista de productos a comprar (separado por comas: A,B,C): ")
        codigos = line.split(',')
        # TODO Calcular total y agregar productos a la pila de productos
        # Va a fallar eventualmente cuando se pidan más de un producto de los que hay
        self.__total = 0
        for codigo in codigos:
            self.__total += self.inventario.buscarProducto().getPrecio()
            self.__listaProductosPush(codigo)

        self.recibirPago()
        if self.currPago >= self.__total:

            self.darCambio()

            # Entregar productos
            self.darProductos():

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
