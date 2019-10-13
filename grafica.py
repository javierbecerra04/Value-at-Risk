# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:33:00 2019

@author: Javier
"""

import matplotlib.pyplot as plt
import io
import base64
 
def build_graph(respuesta_final, VaRCOP,Alpha):
    VaRCOP = float(VaRCOP)
    Alpha = float(Alpha)
    img = io.BytesIO()
    plt.hist(respuesta_final)
    plt.xlabel('Retorno (COP)')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Retornos de Inversión', fontsize=18, fontweight='bold')
    plt.axvline(x=VaRCOP,color='r',linestyle='--',label= str((1-Alpha)*100) + '% de confianza')
    plt.legend(loc='upper rigth',fontsize = 'small')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)
