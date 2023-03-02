

#ESTA ES LA PLANTILLA DEL INVENTARIO DE AQUI SURGEN TODAS LAS SIG FUNCIONES:
#Registrar Productos
#Ingresar producto
#Egresar producto
#COMO DIABLOS METO ESTE MALDITO DICCIONARIO DENTRO DE UNA CLASE Y MEJOR AÚN DENTRO DE UNA FUNCION?
#***********************************************

productos = {
            "codigos": [],
            "nombres": [],
            "marcas": [],
            "fechas_caducidad": [],
            "precios": [],
            "volumenes": [],
            "pesos": [],
            "cantidades ingresadas": []
            }    

# Definimos un tamaño para las listas del diccionario.
# Esto es la variedad de productos que puede albergar mi maquina expendedora.
tamaño = 2

# Leemos los datos y los agregamos a el diccionario
for i in range(tamaño):
    print("Ingrese los datos del producto", i + 1)
    codigo = input("Codigo: ")
    nombre = input("nombre: ")
    marca = input("marca: ")
    fechacad = input("fecha de caducidad: ")
    precio = input("precio: ")
    volumen = input("volumen: ")
    peso = input("peso: ")
    ingreso = input("cantidad de unidades a ingresar: ")

    # La primera lista es para los codigos
    productos["codigos"].append(codigo)

    # La segunda lista es para los nombres
    productos["nombres"].append(nombre)
    
    # La tercera lista es para las marcas
    productos["marcas"].append(marca)

    # La cuarta lista es para fechas de caducidad
    productos["fechas_caducidad"].append(fechacad)

    # La quinta lista es para los precios
    productos["precios"].append(precio)

    # La sexta lista es para los volumendes
    productos["volumenes"].append(volumen)

    # La septima lista es para el peso
    productos["pesos"].append(peso)

    # La octava lista es para la cantidad de producto a ingresar
    productos["cantidades ingresadas"].append(ingreso)

# Ahora mostremos los valores en el diccionario
for i in range(tamaño):
    print(f"Mostrando los datos del producto {i+1}: dentro del inventario:")

    print("Codigo:", productos["codigos"][i])
    print("Nombre:", productos["nombres"][i])
    print("Marca:", productos["marcas"][i])
    print("Fecha de caducidad:", productos["fechas_caducidad"][i])
    print("Precio:", productos["precios"][i])
    print("Volumen:", productos["volumenes"][i])
    print("Peso:", productos["pesos"][i])
    print("Cantidades ingresadas:", productos["cantidades ingresadas"][i])

