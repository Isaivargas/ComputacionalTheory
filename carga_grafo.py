from collections import defaultdict

class Carga_grafo( ):

    def lectura_Grafo(self ):
          nodos_origen = []
          nodos_destino = []
          numRelaciones: int = 0
          with open('grafo.txt', 'r') as f:
           print("Iniciando carga del grafo...", '\n')
           linea = f.readline()
           numNodos = int(linea)
           print("numero de nodos:", numNodos, '\n')
           for i,linea in enumerate(f):
            if i < numNodos:
              if (linea[0].isalpha()) == True:
                print ("nodo",linea)
            else:
                numRelaciones= 1+numRelaciones
                print("Relacion")
                nodo1,nodo2 = linea.split(',')
                print(nodo1,"->",nodo2)
                nodo2=nodo2.rstrip()
                nodos_origen.append(nodo1)
                nodos_destino.append(nodo2)
           f.close()
          return nodos_origen,nodos_destino
# Busqueda de Nodos ya insertados en la lista de Nodos
# En caso de no estar en la lista agregar dicho nodo
# En caso de que ya este solo considerar dicho nodo una sola vez
    def busqueda_relaciones(self,lectura_Grafo):
         nodos_origen=[]
         nodos_destino=[]
         nodos_origen,nodos_destino =lectura_Grafo
         print('\n', "nodo origen", nodos_origen)
         print(" nodo destino", nodos_destino)
         return nodos_origen,nodos_destino












