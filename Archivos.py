import csv
from Producto import *

def Carga_csv(nombre_archivo:str)->list:
    """Recibe el nombre del archivo .csv a cargar como cadena de texto y regresa una lista de diccionarios de productos{"codigo": producto}\n
El archivo debe tener la siguiente estructura: Tipo,Nombre,Precio,Codigo,Marca,Fecha_Caducidad,Peso/Volumen,Cantidad"""

    productos=[]
    with open(nombre_archivo,"r") as f:
        archivo=csv.DictReader(f)

        for linea in archivo:
            if linea["Tipo"]=="Bebida":
                diccionario={linea["Codigo"]: Bebida(linea["Nombre"],linea["Precio"],linea["Codigo"],linea["Marca"],
                                                linea["Fecha_Caducidad"],linea["Peso/Volumen"],linea["Cantidad"]) }
                productos.append(diccionario)
            elif linea["Tipo"]=="Botana":
                diccionario={linea["Codigo"]: Botana(linea["Nombre"],linea["Precio"],linea["Codigo"],linea["Marca"],
                                                linea["Fecha_Caducidad"],linea["Peso/Volumen"],linea["Cantidad"])}
                productos.append(diccionario)


        return productos

prod=Carga_csv("prueba.csv")
for i in prod:
    print(i)