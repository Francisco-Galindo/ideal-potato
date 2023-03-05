import csv
from Producto import *

def Carga_csv(nombre_archivo:str)->list:
    """Recibe el nombre del archivo a cargar como cadena de texto y regresa una lista de productos"""

    productos=[]
    with open(nombre_archivo,"r") as f:
        archivo=csv.DictReader(f)

        for linea in archivo:
            if linea["Tipo"]=="Bebida":
                productos.append(Bebida(linea["Nombre"],linea["Precio"],linea["Codigo"],linea["Marca"],
                                        linea["Fecha_Caducidad"],linea["Peso/Volumen"],linea["Cantidad"]))
            elif linea["Tipo"]=="Botana":
                productos.append(Botana(linea["Nombre"],linea["Precio"],linea["Codigo"],linea["Marca"],
                                        linea["Fecha_Caducidad"],linea["Peso/Volumen"],linea["Cantidad"]))

        return productos
