from Producto import *

def Carga_csv(nombre_archivo:str)->list:
    """Recibe el nombre del archivo a cargar como cadena de texto"""
    productos=[]
    with open(nombre_archivo,"r") as f:
        archivo=f.readlines()

        for linea in archivo:
            atributos=linea.split(",")
            if atributos[0]=="Bebida":
                productos.append(Bebida(atributos[1],atributos[2],atributos[3],atributos[4],atributos[5],atributos[6]))
            elif atributos[0]=="Botana":
                productos.append(Botana(atributos[1],atributos[2],atributos[3],atributos[4],atributos[5],atributos[6]))
                # nombre(str), precio(float), código(str), marca(str) y fecha de caducidad(str) y y volumen(str)

        return productos

#TODO INTEGRAR A LA FUNCION "imprimirTicket" DE Maquina.py
def Ticket():
    """PlaceHolder"""
    pass