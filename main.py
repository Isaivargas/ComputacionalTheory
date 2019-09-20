from grafo import Grafo


class main( ):
    pass
    def main():
        grafo=Grafo()
        grafo.agregar_arista(grafo.nodosOrigen,grafo.nodosDestino)
        print("\n Grafo:",grafo.generar_arista(grafo.grafo))
        nodoOrigen=input("\n Introduce el nodoOrigen:")
        nodoDestino=input(" Introduce el nodoDestino:")
        print("\n","La ruta es:",grafo.busqueda_camino(grafo.grafo, nodoOrigen, nodoDestino))
        print("\n","Los posibles caminos son :",grafo.busqueda_caminos(grafo.grafo,nodoOrigen,nodoDestino))
        print("\n La ruta más corta es: ",grafo.ruta_corta())



    if __name__ == "__main__":
       Main=main( )
       Main

