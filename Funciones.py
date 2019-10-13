# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:56:42 2019

@author: Javier
"""

#Importación de las librerías
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


#Definición de la Función principal
def calculo_VaR(Parametros = ["","",""], Window = 250, Lag = 10, Alpha = 0.01):
  
    Pais = Parametros[0]
    Institucion = Parametros[1]
    Producto = Parametros[2]
    Window = int(Window)
    Lag = int(Lag)
    Alpha = float(Alpha)
    
    #Importe de cada uno de los portafolios    
    ECOPETL = pd.read_excel('Prueba Desarrollo.xlsx', sheet_name='ECOPETL')
    index_fechaEc = ECOPETL[ECOPETL['Fecha'] == '2019-04-08'].index #Tamaño máximo de la ventana
    
    EURUSD = pd.read_excel('Prueba Desarrollo.xlsx', sheet_name='Monedas',usecols = [0,2])
    index_fechaEUR = EURUSD[EURUSD['Fecha'] == '2019-04-08'].index #Tamaño máximo de la ventana

    USDCOP = pd.read_excel('Prueba Desarrollo.xlsx', sheet_name='Monedas',usecols = [0,1])
    index_fechaUSD = USDCOP[USDCOP['Fecha'] == '2019-04-08'].index #Tamaño máximo de la ventana


    #Seleccionando los datos dependiendo de la ventana (Window)
    DatosEc = ECOPETL.loc[len(ECOPETL['ECOPETL'])-Window:,'ECOPETL'] #Ajustar la información a la ventana de Datos
    DatosUSD = USDCOP.loc[index_fechaUSD[0]-Window:index_fechaUSD[0],'USDCOP'] #Ajustar la información a la ventana de Datos
    DatosEUR = EURUSD.loc[index_fechaEUR[0]-Window:index_fechaEUR.values[0],'EURUSD'] #Ajustar la información a la ventana de Datos
    
    
    #Filtrando por los parámetros
    if (Pais=="" and Institucion=="" and Producto==""):
        
        resp1,resp2,VN1 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)
        resp3,resp4,VN2 = calculo_valorenriesgo(DatosUSD,index_fechaUSD,Window,Lag,Alpha,25000000)
        resp5,resp6,VN3 = calculo_valorenriesgo(DatosEUR,index_fechaEUR,Window,Lag,Alpha,5000000,'EUR')
        resp7,resp8,VN4 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)
            
        Valor_Inversion = VN1 + VN2 + VN3 + VN4
        respuesta_final = (resp1+resp3+resp5+resp7)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%')    
            
    elif (Pais=="Colombia" and Institucion=="" and Producto==""):
        
        resp1,resp2,VN1 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)
        resp3,resp4,VN2 = calculo_valorenriesgo(DatosUSD,index_fechaUSD,Window,Lag,Alpha,25000000)
        
        Valor_Inversion = VN1 + VN2
        respuesta_final = (resp1+resp3)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%')
        
    elif (Pais=="Panama" and Institucion=="" and Producto=="") or (Pais=="" and Institucion=="Bancolombia Panama" and Producto=="") or (Pais=="Panama" and Institucion=="Bancolombia Panama" and Producto=="") :
        
        resp5,resp6,VN3 = calculo_valorenriesgo(DatosEUR,index_fechaEUR,Window,Lag,Alpha,5000000,'EUR')
        resp7,resp8,VN4 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)
            
        Valor_Inversion = VN3 + VN4
        respuesta_final = (resp5+resp7)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%')
        
    elif (Pais=="" and Institucion=="Bancolombia" and Producto=="") or (Pais=="" and Institucion=="Bancolombia" and Producto=="Moneda") or (Pais=="Colombia" and Institucion=="Bancolombia" and Producto=="Moneda") or (Pais=="Colombia" and Institucion=="" and Producto=="Moneda"):
        
        resp3,resp4,VN2 = calculo_valorenriesgo(DatosUSD,index_fechaUSD,Window,Lag,Alpha,25000000)
               
        Valor_Inversion = VN2
        respuesta_final = (resp3)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%')
        
    elif (Pais=="" and Institucion=="Bancolombia Panama" and Producto=="Moneda") or (Pais=="Panama" and Institucion=="Bancolombia Panama" and Producto=="Moneda") or (Pais=="Panama" and Institucion=="" and Producto=="Moneda"):
        
        resp5,resp6,VN3 = calculo_valorenriesgo(DatosEUR,index_fechaEUR,Window,Lag,Alpha,5000000,'EUR')
            
        Valor_Inversion = VN3
        respuesta_final = (resp5)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%')
        
    elif (Pais=="" and Institucion=="Bancolombia Panama" and Producto=="Renta Variable") or (Pais=="Panama" and Institucion=="Bancolombia Panama" and Producto=="Renta Variable") or (Pais=="Panama" and Institucion=="" and Producto=="Renta Variable") or (Pais=="Colombia" and Institucion=="" and Producto=="Renta Variable") or (Pais=="" and Institucion=="Valores Bancolombia" and Producto=="Renta Variable") or (Pais=="Colombia" and Institucion=="Valores Bancolombia" and Producto=="") or (Pais=="" and Institucion=="Valores Bancolombia" and Producto==""):
        
        resp1,resp2,VN1 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)    
        
        Valor_Inversion = VN1
        respuesta_final = (resp1)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%')
    
    elif (Pais=="" and Institucion=="" and Producto=="Renta Variable"):
        
        resp1,resp2,VN1 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)
        resp7,resp8,VN4 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)    
        
        Valor_Inversion = VN1 + VN4
        respuesta_final = (resp1 + resp7)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%')
        
    elif (Pais=="" and Institucion=="" and Producto=="Renta Variable"):
        
        resp1,resp2,VN1 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)
        resp7,resp8,VN4 = calculo_valorenriesgo(DatosEc,index_fechaEc,Window,Lag,Alpha,50000)    
        
        Valor_Inversion = VN1 + VN4
        respuesta_final = (resp1 + resp7)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%') 
      
    elif (Pais=="" and Institucion=="" and Producto=="Moneda"):
        
        resp3,resp4,VN2 = calculo_valorenriesgo(DatosUSD,index_fechaUSD,Window,Lag,Alpha,25000000)
        resp5,resp6,VN3 = calculo_valorenriesgo(DatosEUR,index_fechaEUR,Window,Lag,Alpha,5000000,'EUR') 
        
        Valor_Inversion = VN2 + VN3
        respuesta_final = (resp3 + resp5)
        respuesta_final = np.sort(respuesta_final)
        VaRCOP = respuesta_final[math.ceil(Alpha*len(respuesta_final))-1]
        VaRCOP = int(VaRCOP)
        print("Valor en Riesgo","{:,}".format(VaRCOP),'COP')
        VaR = (VaRCOP/Valor_Inversion)*100
        VaR = round(VaR[0],4)
        print("Valor en Riesgo",VaR,'%') 


    #Histograma de retornos (comentar si se va a ejecutar App.py)
    plt.hist(respuesta_final)
    plt.xlabel('Retorno (COP)')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Retornos de Inversión', fontsize=18, fontweight='bold')
    plt.axvline(x=VaRCOP,color='r',linestyle='--',label= str((1-Alpha)*100) + '% de confianza')
    plt.legend(loc='upper rigth',fontsize = 'small')
    plt.show
   
    return VaRCOP,VaR,respuesta_final
    
    
#Funcion para calcular el VaR para cierto Portafolio
def calculo_valorenriesgo(Datos,index_fecha, Window, Lag, Alpha,Nominal,Moneda=''):   
    simulacion = np.zeros(Window-Lag)
    for i in range(0,Window-Lag):    
        simulacion[i] = Datos.loc[index_fecha].values+(Datos.loc[index_fecha-i].values-Datos.loc[index_fecha-i-Lag].values)
    Aux = np.sort(simulacion)
    if Moneda == 'EUR':
        Valor_Nominal = Nominal*Datos.loc[index_fecha].values*3115.22 #Valor de la Inversión realizada para el portafolio
    else:
        Valor_Nominal = Nominal*Datos.loc[index_fecha].values #Valor de la Inversión realizada para el portafolio
#    Valor_Nominal*Datos.loc[index_fecha].values
    ValorenRiesgo = -(1-(Aux/Datos.loc[index_fecha].values))*Valor_Nominal
    ValorenRiesgo = np.sort(ValorenRiesgo) #Vector con el retorno a la inversión de los valores simulados
    return ValorenRiesgo,Aux,Valor_Nominal