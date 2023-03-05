#!/bin/python

from Maquina import *

maquina = Maquina(1000, "123")

print("Bienvenido!")

while True:
    print("""
          +---+ +---+ +---+ +---+ +---+ +---+
          |   | |   | |   | |   | |   | |   |
          | A | | B | | C | | D | | E | | F |
          |   | |   | |   | |   | |   | |   |
          +---+ +---+ +---+ +---+ +---+ +---+
    """)

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
    elif opcion == '3':
        break

print("\nAdiós!")
