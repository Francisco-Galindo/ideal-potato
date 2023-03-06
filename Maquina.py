from Inventario import *
from datetime import datetime

class Maquina():

    """ Clase que representa la máquina expendedora, describe las interacciones
    que una persona puede tener con la misma.
    Recibe: dinero(float), password(str)"""


    """
    Constructor de la clase Maquina

    :param dinero: La cantidad de dinero que tiene la máquina al inicio
    :param password: La contraseña para entrar como persona de mantenimiento
    """
    def __init__(self, dinero = 1000, password = '123'):
        self.__pasword = password
        self.__dinero = dinero
        self.__atascada = False
        self.__sesionIniciada = False

        self.__currPago = 0
        self.__total = 0

        self.__listaCodigos = []
        self.__infoTicket = []

        self.inventario = Inventario()

    def recibirPago(self):
        """
        Permite recibir pagos del usuario, verifica que se ingrese la cantidad
        correcta de dinero.
        """
        debePagar = True

        print(f"Son ${self.__total:.2f}")

        while debePagar:

            try:
                pago = float(input("Introduzca su dinero: "))
                self.__currPago += pago
            except ValueError:
                print("Necesito una cantidad válida de dinero...")

            if self.__currPago >= self.__total:
                debePagar = False
            else: print(f"Todavía faltan ${self.__total - self.__currPago:.2f}...")


    def darCambio(self):
        """
        Calcula el cambio que se le debe al usuario y verifica que la máquina
        expendedora tenga suficiente dinero.
        """
        cambio = self.__currPago - self.__total


        if cambio > self.__dinero:
            print("¡La máquina no tiene suficiente dinero para dar cambio!")
            print(f"Te devolvemos tus ${self.__currPago:.2f}")
            return False

        if cambio > 0:
            print(f"Su cambio es de ${cambio:.2f}")

        self.__dinero -= cambio
        self.__dinero += self.__currPago - cambio

        return True

    def darProductos(self):
        """
        Itera sobre los códigos pedidos por el usuario e intenta entregar
        los productos
        """
        while self.__listaCodigos:
            codigo = self.__listaCodigos.pop()

            producto = self.inventario.Compra_Usuario(codigo)
            if producto:
                print(f"Aquí está su {producto}")

                self.__infoTicket.append({
                    "codigo": codigo,
                    "precio": producto.get_precio()
                })

            else:
                print("No se pudo sacar el producto")
                break

    def imprimirTicket(self):
        """Imprime el ticket de compra"""

        print("\nImprimiendo ticket...")

        fechahora=datetime.now().strftime("%d-%m-%y--%H;%M;%S")

        with open(f"Ticket({fechahora}).txt","w") as ft:
            ft.write("----------------Ticket de compra:----------------\n\n")

            ft.write(f"Fecha de compra: {fechahora}\n\n")
            ft.write("CODIGO:\tPRECIO:\n")

            for i in self.__infoTicket:
                ft.write(f"{i['codigo']}\t${i['precio']:.2f}\n")

            ft.write(f"\nTotal\t${self.__total:.2f}\n")
            ft.write(f"Pago\t${self.__currPago:.2f}\n")
            ft.write(f"Cambio\t${self.__currPago - self.__total:.2f}\n")

            ft.write("---------------------------------------------------\n")

        self.__infoTicket = []

    def hacerTransaccion(self):
        """
        Método que se encarga de llevar a cabo la transacción con el usuario,
        el usuario ingresa los productos que quiere comprar ingresando sus
        códigos separados por comas, mantiene la cuenta del total a pagar y de
        la lista de códigos.
        """
        line = input("\nIngrese la lista de productos a comprar (separado por comas: Coca,Pepsi,Sab, ...): ")
        codigos = line.split(',')

        self.__total = 0
        for codigo in codigos:
            codigo = codigo.strip()
            # Falta validar que haya suficientes productos
            if codigo:
                producto = self.inventario.BuscarProducto(codigo)
                if producto:
                    precio = producto.get_precio()

                    self.__total += precio
                    self.__listaCodigos.append(codigo)
                else:
                    print(f"No se encontró el producto {codigo}")

        if self.__total == 0:
            print("No has escrito ningún código válido")
            return

        self.recibirPago()
        if self.__currPago >= self.__total:

            if self.darCambio():
                self.darProductos()
                self.imprimirTicket()

            self.__currPago = 0
        else:
            print("No has pagado lo suficiente...")

    def acceder(self, passwd):
        """
        Permite al administrador acceder a las funciones del sistema usando su
        contraseña por defecto es "123"; se recomienda cambiarla.
        """
        if passwd == self.__pasword:
            self.__sesionIniciada = True
        else:
            self.__sesionIniciada = False

    def salir(self):
        """
        Permite cerrar la sesión del administrador.
        """
        self.__sesionIniciada = False

    def cambiarContra(self, passwd):
        """
        Recibe como argumento la nueva contraseña (str) y cambia la contraseña
        del administrador.
        """
        if self.__sesionIniciada:
            self.__pasword = passwd
        else:
            return

    def sacarDinero(self):
        """
        Permite al administrador retirar todo el dinero de la máquina.
        """
        if self.__sesionIniciada:
            print(f"\nSacaste los ${self.__dinero:.2f} de la máquina\n")
            self.__dinero = 0
        else:
            return

    def agregarDinero(self, dinero: float):
        """
        Permite al administrador agregar dinero a la maquina. recibe como
        argumento la cantidad a agregar (float)
        """

        if self.__sesionIniciada:
            self.__dinero += dinero
            print(f"\nAgregando ${dinero:.2f} a la máquina, ahora tiene ${self.__dinero:.2f}\n")
        else:
            return

    @property
    def sesionIniciada(self):
        """Getter, regresa el estado del inicio de sesión"""
        return self.__sesionIniciada
