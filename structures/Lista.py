from Nodo import Nodo;

class Lista:

    # Inicialización de la lista.
    def __init__( self, *datos ):
        self.__count  = 0;
        self.__frente = None;
        self.__final  = None;
        if ( not datos ): return;
        for dato in datos: self.insertar( dato );

    # Insertar un dato.
    def insertar( self, dato ):
        nodo = Nodo( dato, None );
        if ( self.__count == 0 ):
            self.__frente = nodo;
            self.__final  = nodo;
        elif ( dato <= self.__frente._dato ): self.__insertarPrincipio( nodo );
        elif ( dato > self.__final._dato ): self.__insertarFinal( nodo );
        else: self.__insertarMedio( nodo );
        self.__count = self.__count + 1;

    # Insertar un dato al inicio.
    def __insertarPrincipio( self, nodo ):
        nodo._siguiente = self.__frente;
        self.__frente = nodo;

    # Insertar un dato al final.
    def __insertarFinal( self, nodo ):
        self.__final._siguiente = nodo;
        self.__final = nodo;

    # Insertar un dato al medio.
    def __insertarMedio( self, nodo ):
        posicion = self.__posicionAnteriorDato( nodo._dato );
        if ( posicion == None ): return;
        nodo._siguiente = posicion._siguiente;
        posicion._siguiente = nodo;

    # Buscamos el dato anterior al que se quiere ingresar.
    def __posicionAnteriorDato( self, dato ):
        actual = self.__frente;
        anterior = None;
        while ( actual != None and dato > actual._dato ):
            anterior = actual;
            actual = actual._siguiente;
        return anterior;

    # Iterador.
    def __iter__( self ):
        self.__actual = None;
        return self;

    # Iterador.
    def __next__( self ):
        if ( not self.__actual ):
            self.__actual = self.__frente;
            return self.__actual._dato;
        elif ( self.__actual._siguiente != None ):
            self.__actual = self.__actual._siguiente;
            return self.__actual._dato;
        else:
            raise StopIteration;

if __name__ == "__main__":

    lista = Lista( 2, 1, 7, 9, 3, 4 );
    index = 1;
    for element in lista:
        print( f"Elemento { index }: { element }" );
        index = index + 1;
