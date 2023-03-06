#!/bin/python

from Maquina import *

maquina = Maquina(1000, "123")

print("Bienvenido!")

while True:
    maquina.inventario.mostrarListaProductos()

    print("Acciones a realizar")
    print("1. Comprar productos")
    print("2. Ingreso de mantenimiento")
    print("3. Salir")

    opcion = input("¿Qué quieres hacer?: ").strip()

    if opcion == '1':
        maquina.hacerTransaccion()
        input("\nPresione enter para continuar").strip()
    elif  opcion == '2':

        pw = input("Introduce la contraseña súper secreta: ")
        maquina.acceder(pw)
        if not maquina.sesionIniciada:
            print("Contraseña incorrecta...")

        while maquina.sesionIniciada:
            print('*****INVENTARIO*****\n')
            print('****** Menú Principal ******')
            print('0. Salir')
            print('1. Ingreso de productos')
            print('2. Egreso de producto')
            print('3. Historial de movimientos')
            print('4. Búsqueda de producto')
            print('5. Sacar dinero de la máquina')
            print('6. Agregar dinero a la máquina')
            opcion = input('\nDigitar una Opción: ')
            if opcion =='0':
                print("Gracias por usar nuestro servicio. ¡Hasta luego!")
                break
            elif opcion == '1':
                maquina.inventario.Ingreso()
            elif opcion == '2':
                maquina.inventario.Egreso()
            elif opcion == '3':
                maquina.inventario.Historial()
            elif opcion == '4':
                print('')
                print('****** BUSQUEDA DE PRODUCTO ******')
                Codigo = input("Ingrese el Código del Producto: ")
                maquina.inventario.mostrarProducto(Codigo)
            elif opcion == '5':
                maquina.sacarDinero()
            elif opcion == '6':
                try:
                    dinero = float(input("Dinero a agregar: "))
                    maquina.agregarDinero(dinero)
                except ValueError:
                    print("Se necesitan valores numéricos...")
            else:
                print('Opción no válida. Intente nuevamente')

        maquina.salir()

    elif opcion == '3':
        break
    else:
        print('Opción no válida. Intente nuevamente')

print("\nAdiós!")
