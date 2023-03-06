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
        input("\nPresione enter para continuar")
    elif  opcion == '2':
        print("Mantenimiento")

        pw = input("Introduce la contraseña súper secreta: ")
        maquina.acceder(pw)
        if not maquina.sesionIniciada:
            print("Contraseña incorrecta...")

        while maquina.sesionIniciada:
            print('*****INVENTARIO*****\n')
            print('****** Menú Principal ******')
            print('0. SALIR')
            print('1. INGRESO DE PRODUCTO')
            print('2. EGRESO DE PRODUCTO')
            print('3. HISTORIAL DE MOVIMIENTOS')
            print('4. BUSQUEDA DE PRODUCTO')
            opcion = input('Digitar una Opción: ')
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
                maquina.inventario.BuscarProducto2(Codigo)
            else:
                print('Opción no válida. Intente nuevamente')

        maquina.salir()

    elif opcion == '3':
        break
    else:
        print('Opción no válida. Intente nuevamente')

print("\nAdiós!")
