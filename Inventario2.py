class Productos:

    def diccionario(self):
        productos = {}
        print (productos)
pass

# It creates a class called Codigos.
class Codigos:

    def funcion(self):
        input ("ingrese el codigo: ")
        #aqui tengo que poner el append para que ingrese a mi dicionario posiblemente
   
# It creates a class called Nombres.
class Nombres:

    def funcion(self):
        input ("ingrese el nombre del producto: \n")

# It creates a class called Marcas.
class Marcas:

    def funcion(self):
        input ("ingrese la marca del producto: \n")
    

# The class Caducidades has a function called funcion that takes no arguments and returns nothing.
class Caducidades:

    def funcion(self):
        input ("ingrese la fecha de caducidad del producto: \n")
      

# It creates a class called Precios.
class Precios:

    def funcion(self):
        input ("ingrese el precio del producto por unidad: \n")

# A class that asks for a volume.
class Volumenes:

    def funcion(self):
        input ("ingrese el volumen (si aplica, sino ingrese cero): \n")
       

# It asks the user to input a weight.
class Pesos:

    def funcion(self):
        input ("ingrese el peso (si aplica, sino ingrese cero): \n")
  

# A class that asks the user to input the number of units to enter.
class Ingresos:

    def funcion(self):
        input ("digite la cantidad de unidades a ingresar: \n")
      
# Creating an instance of each class.
codigo = Codigos()
nombre = Nombres()
marca = Marcas()
caducidad = Caducidades()
precio = Precios()
volumen = Volumenes()
peso = Pesos()
ingreso = Ingresos()
productos = Productos() #de alguna manera debo rellenar el diccionario, ya sea con algun metodo
#clase por clase o todas en una clase, o el diccionario por separado.

# Iterating through the list of classes and calling the function funcion() on each class.
for productos in (codigo, nombre, marca, caducidad, precio, volumen, peso, ingreso):
    productos.funcion()




    
    


