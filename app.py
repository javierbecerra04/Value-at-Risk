# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:51:49 2019

@author: Javier
"""

#Importar las librerias a usar
from flask import Flask, render_template,url_for
from flask import request
from Funciones import *
from grafica import build_graph

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
	
    if request.method == 'POST':  #Solo entra a esta sentencia si se oprime el botón
        pais = request.form.get('Pais')
        institucion = request.form['Institucion']
        producto = request.form['Producto']
        window = request.form['Window']
        lag = request.form['Lag']
        alpha = request.form['Alpha']
        VaR1,VaR2,resp_final = calculo_VaR([pais,institucion,producto],window,lag,alpha) #Llamado de la Función

        graph1_url = build_graph(resp_final,VaR1,alpha); #Grafica de Histograma
        
        return render_template('results.html',graph1_url=graph1_url,VaR1=VaR1,VaR2=VaR2)
    
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(port = 5000)

