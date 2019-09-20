from collections import defaultdict

import numpy as np
from self import self

from carga_grafo import Carga_grafo
import pandas as pd


class Grafo(  ):


 grafoInicial = Carga_grafo()
 nodosOrigen=[]
 nodosDestino=[]
 edges=[]
 caminos=[]
 nodosOrigen,nodosDestino = grafoInicial.busqueda_relaciones(grafoInicial.lectura_Grafo())
 grafo = defaultdict(list)



 def agregar_arista(grafo,nodosOrigen,nodosDestino):
     grafo1 = defaultdict(list)
     for nodos_origen, nodos_destino in zip(nodosOrigen,nodosDestino):
         grafo1[nodos_origen].append(nodos_destino)
     return grafo1

 grafo=agregar_arista(grafo,nodosOrigen,nodosDestino)
 print("\n",grafo)



 def generar_arista(self,grafo):
     grafo1=grafo
     edges = []
     # for each node in graph
     for node in grafo1:
         # for each neighbour node of a single node
         for neighbour in grafo1[node]:
             # if edge exists then append
            edges.append((node, neighbour))

     return edges

 edges=generar_arista(self,grafo)


 def busqueda_camino(self,grafo, start, end,camino=[]):
     camino = camino + [start]
     node:int
     if start == end:
         return camino
     for node in grafo[start]:
         if node not in camino:
             newpath = self.busqueda_camino(grafo, node, end, camino)
             if newpath:
                 return newpath



 def busqueda_caminos(self,grafo, start, end, camino=[]):
     camino = camino + [start]
     nuevoscaminos=[]
     if start == end:
         return [camino]
     caminos = []
     for node in grafo[start]:
         if node not in camino:
             nuevoscaminos = self.busqueda_caminos(grafo, node, end, camino)
         for nuevoscamino in nuevoscaminos:
             caminos.append(nuevoscamino)
     self.caminos=caminos
     return caminos



 def ruta_corta(self):
     minList = min(self.caminos, key=len)
     minLength = min(map(len, self.caminos))

     return minList, minLength















