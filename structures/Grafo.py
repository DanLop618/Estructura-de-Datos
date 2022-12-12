from structures.ListaAdyacencia import ListaAdyacencia;
from structures.NodoGrafo import Nodo;
from structures.Arco import Arco;

class Grafo:

    """Inicialización de un grafo.
    """
    def __init__( self ):
        self.__primero = None;
        self.__ultimo  = None;

    """
    """
    def vacio( self ):
        return self.__primero == None;

    """
    """
    def existeVertice( self, dato ):
        temporal = self.__primero;
        while ( temporal ):
            if ( temporal._dato == dato ): return True;
            temporal = temporal._siguiente;
        return False;

    """
    """
    def nuevaArista( self, origen, destino, peso = 1 ):
        if ( not self.existeVertice( origen ) or not self.existeVertice( destino ) ): return;
        posicion = self.__primero;
        while ( posicion._dato != origen ): posicion = posicion._siguiente;
        posicion._lista.nuevaAdyacencia( destino, peso );

    """
    """
    def removerArista( self, origen, destino ):
        if ( not self.existeVertice( origen ) or not self.existeVertice( destino ) ): return;
        posicion = self.__primero;
        while ( posicion._dato != origen ): posicion = posicion._siguiente;
        posicion._lista.eliminarAdyacencia( destino );

    """
    """
    def nuevoNodo( self, dato ):
        if ( self.existeVertice( dato ) ): return;
        nodo = Nodo( dato, ListaAdyacencia() );
        if ( self.vacio() ):
            self.__primero = nodo;
            self.__ultimo  = nodo;
        else:
            if ( dato <= self.__primero._dato ):
                nodo._siguiente = self.__primero;
                self.__primero  = nodo;
            elif ( dato >= self.__primero._dato ):
                self.__ultimo._siguiente = nodo;
                self.__ultimo = nodo;
            else:
                anterior = None;
                actual   = self.__primero;
                while ( actual and dato > actual._dato ):
                    anterior = actual;
                    actual   = actual._siguiente;
                nodo._siguiente = actual;
                anterior._siguiente = nodo;

    """
    """
    def imprimir( self, incluirPeso = False ):
        if ( self.vacio() ): return "";
        cadena = "";
        temporal = self.__primero;
        while ( temporal ):
            cadena += f"{ str( temporal._dato ) } -> " + temporal._lista.imprimir( incluirPeso ) + "\n";
            temporal = temporal._siguiente;
        return cadena;
