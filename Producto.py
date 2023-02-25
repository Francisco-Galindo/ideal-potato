class Producto:
    """La clase producto crea y define un nuevo producto, recibe:\n
    nombre(str), precio(float), código(str), marca(str) y
    fecha de caducidad(str)"""

    def __init__( self:object, nombre:str="NombreProducto",
                 precio:float=0.0 , codigo:str="CodigoProducto" , 
                 marca:str="MarcaProducto" , fechacad:str="dd/mm/aa" )->object:
        self.nombre=nombre
        self._precio=precio
        self.codigo=codigo
        self.marca=marca
        self.fechacad=fechacad
        
    def set_codigo(self,nuevocodigo):
        self.codigo=nuevocodigo
        print("Se cambió el código a: ",self.codigo)

    def set_precio(self,nuevoprecio):
        print(f"Precio anterior={self._precio}, Nuevo precio={nuevoprecio}")
        self._precio=nuevoprecio

    def get_precio(self)->float:
        return self._precio



class Bebida(Producto):
    """La clase Bebida hereda de la clase Producto, crea y define una nueva bebida, recibe:\n
    nombre(str), precio(float), código(str), marca(str), fecha de caducidad(str) y volumen[ml](str)"""

    def __init__(self:object, nombre:str="NombreProducto",
                 precio:float=0.0 , codigo:str="CodigoProducto" , 
                 marca:str="MarcaProducto" , fechacad:str="dd/mm/aa",
                 volumen:str="000ml")->object:
        super().__init__(nombre,precio,codigo,marca,fechacad)
        self.volumen=volumen



class Botana(Producto):
    """La clase Botana hereda de la clase Producto, crea y define una nueva botana, recibe:\n
    nombre(str), precio(float), código(str), marca(str), fecha de caducidad(str) y peso[g](str)"""

    def __init__(self:object, nombre:str="NombreProducto",
                 precio:float=0.0 , codigo:str="CodigoProducto" , 
                 marca:str="MarcaProducto" , fechacad:str="dd/mm/aa",
                 peso:str="000g")->object:
        super().__init__(nombre,precio,codigo,marca,fechacad)
        self.peso=peso
