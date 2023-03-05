import csv
from Producto import *
from datetime import datetime

def Carga_csv(nombre_archivo:str)->list:
    """Recibe el nombre del archivo a cargar como cadena de texto y regresa una lista de productos.\n
La estructura del archivo debe ser: Tipo,Nombre,Precio,Codigo,Marca,Fecha_Caducidad,Peso/Volumen,Cantidad"""

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
    
#TODO incluir los precios de los productos
def Imprimir_Ticket(codigos:list,pago:float,total:float):
    """Imprime el ticket de compra, recibe codigos(list), pago(float), total(float)"""

    fechahora=datetime.now()
    fechahora=fechahora.strftime("%d-%m-%y--%H;%M;%S")

    with open(f"Ticket({fechahora}).txt","w") as ft:
        ft.write("----------------Ticket de compra:----------------\n")
        ft.write(f"Fecha de compra: {fechahora}\n")
        ft.write("CODIGO:\t PRECIO:\n")
        for i in codigos:
            ft.write(f"{i}\t {20}\n")
        ft.write(f"Total= {total}\n")
        ft.write(f"Pago= {pago}\n")
        ft.write(f"Cambio= {pago-total}\n")
        ft.write("---------------------------------------------------")

# print("prueba, borrar esto")
# codigos=["A","B","C","D"]
# Imprimir_Ticket(codigos,120,80)