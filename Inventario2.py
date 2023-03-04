# It creates a class called Codigos.
class Codigos:

    def funcion(self):
        diccionario["codigos"].append(input ("ingrese el codigo: \n"))
   
# It creates a class called Nombres.
class Nombres:

    def funcion(self):
        diccionario["nombres"].append(input ("ingrese el nombre del producto: \n"))

# It creates a class called Marcas.
class Marcas:

    def funcion(self):
        diccionario["marcas"].append(input ("ingrese la marca del producto: \n"))
    

# The class Caducidades has a function called funcion that takes no arguments and returns nothing
class Caducidades:

    def funcion(self):
        diccionario["fechas_caducidad"].append(input ("ingrese la fecha de caducidad del producto: \n"))
      

# The class Precios has a function called funcion that takes no arguments and returns nothing
class Precios:

    def funcion(self):
        diccionario["precios"].append(input ("ingrese el precio del producto: \n"))

# It's a class that has a function that takes user input and appends it to a dictionary
class Volumenes:

    def funcion(self):
        diccionario["volumenes"].append(input ("ingrese el volumen en ml del producto (en caso de que no aplique ingresar 0): \n"))
       

# The class Pesos is a class that has a function that asks the user to input the weight of the product
# in grams
class Pesos:

    def funcion(self):
        diccionario["pesos"].append(input ("ingrese el peso en gr del producto (en caso de que no aplique ingresar 0): \n"))
  

# It creates a class called Ingresos.
class Ingresos:

    def funcion(self):
        diccionario["cantidades ingresadas"].append(input ("ingrese las unidades del producto a ingresar: \n"))

# The class Iteraciones has a method funcion that prints the data of the new product (product i+1) in
# the inventory.
class Iteraciones:

    def funcion(self):

            print(f"Mostrando los datos del nuevo producto (producto {i+1}) dentro del inventario:\n")
            for key, value in diccionario.items():
                print(f'{key}, {value}')
                        

# It's a dictionary that has a list of keys and values.
diccionario = {
            "codigos": [],
            "nombres": [],
            "marcas": [],
            "fechas_caducidad": [],
            "precios": [],
            "volumenes": [],
            "pesos": [],
            "cantidades ingresadas": []
        }  

# It's creating an instance of each class.
tamaño = 2      
codigo = Codigos()
nombre = Nombres()
marca = Marcas()
caducidad = Caducidades()
precio = Precios()
volumen = Volumenes()
peso = Pesos()
ingreso = Ingresos()
iteracion = Iteraciones()

# It's a for loop that iterates through the list of classes and calls the function funcion() of each
# class.
for i in range(tamaño):
    for productos in (codigo, nombre, marca, caducidad, precio, volumen, peso, ingreso, iteracion):
        productos.funcion()

print("--------------imprimiendo todo el diccionario-----------------------") 
#esta parte aun falta por desarrollarse pongo mientras una impresion de todo para acordarme.  
print(diccionario.items())

    
    


