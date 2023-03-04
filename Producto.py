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
        
    def set_codigo(self:object,nuevocodigo:str):
        """Cambia el codigo del producto a una cadena de texto ingresada por el usuario"""
        self.codigo=nuevocodigo
        print("Se cambió el código a: ",self.codigo)

    def set_precio(self:object,nuevoprecio:float):
        """Cambia el precio del producto a un valor float ingresado por el usuario"""
        print(f"Precio anterior={self._precio}, Nuevo precio={nuevoprecio}")
        self._precio=nuevoprecio

    def get_precio(self:object)->float:
        """"Recibe un objeto y regresa su precio"""
        return self._precio
    
    def __str__(self:object) -> str:
        """Recibe un objeto y regresa su nombre"""
        return str(self.nombre)



class Bebida(Producto):
    """La clase Bebida hereda de la clase Producto, crea y define una nueva bebida, recibe:\n
    nombre(str), precio(float), código(str), marca(str), fecha de caducidad(str) y volumen(str)"""

    def __init__(self:object, nombre:str="NombreProducto",
                 precio:float=0.0 , codigo:str="CodigoProducto" , 
                 marca:str="MarcaProducto" , fechacad:str="dd/mm/aa",
                 volumen:str="000ml")->object:
        super().__init__(nombre,precio,codigo,marca,fechacad)
        self.volumen=volumen

    def __str__(self) -> str:
        """Recibe un objeto y regresa su nombre"""
        return str(self.nombre)



class Botana(Producto):
    """La clase Botana hereda de la clase Producto, crea y define una nueva botana, recibe:\n
    nombre(str), precio(float), código(str), marca(str), fecha de caducidad(str) y peso(str)"""

    def __init__(self:object, nombre:str="NombreProducto",
                 precio:float=0.0 , codigo:str="CodigoProducto" , 
                 marca:str="MarcaProducto" , fechacad:str="dd/mm/aa",
                 peso:str="000g")->object:
        super().__init__(nombre,precio,codigo,marca,fechacad)
        self.peso=peso

    def __str__(self) -> str:
        """Recibe un objeto y regresa su nombre"""
        return str(self.nombre)
