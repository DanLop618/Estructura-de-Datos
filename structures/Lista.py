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

    # ELimina un elemento de la lista.
    def eliminar( self, dato ):
        actual = None;
        anterior = None;
        elemento =None;
        if ( self.vacio() or not self.contiene( dato ) ): return [ False, None ];
        if ( self.__frente == self.__final ):
            elemento = self.__frente._dato;
            self.__frente = None;
            self.__final = None;
        else:
            actual = self.__encuentraPosicion( dato );
            elemento = actual._dato;
            if ( actual == self.__frente ): self.__eliminarFrente();
            elif ( actual == self.__final ): self.__eliminarFinal();
            else: self.__eliminarMedio( dato, actual );
        return [ True, elemento ];

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

    # Encentra posicion de nodo.
    def __encuentraPosicion( self, dato ):
        actual = self.__frente;
        while ( actual != None and actual._dato != dato ): actual = actual._siguiente;
        return actual;

    # Eliminanos el nodo del frente.
    def __eliminarFrente( self ):
        nodo = self.__frente;
        self.__frente = self.__frente._siguiente;
        nodo = None;

    # Eliminanos el nodo del frente.
    def __eliminarFinal( self ):
        anterior = self.__posicionAnteriorDato( self.__final._dato );
        anterior._siguiente = None;
        self.__final = anterior;

    # ELiminamos un nodo de en medio de la lista.
    def __eliminarMedio( self, dato, actual ):
        anterior = self.__posicionAnteriorDato( dato );
        anterior._siguiente = actual._siguiente;
        actual._siguiente = None;

    # Buscamos el dato anterior al que se quiere ingresar.
    def __posicionAnteriorDato( self, dato ):
        actual = self.__frente;
        anterior = None;
        while ( actual != None and dato > actual._dato ):
            anterior = actual;
            actual = actual._siguiente;
        return anterior;

    # Verifica si existe un dato en la lista.
    def contiene( self, dato ):
        for element in self:
            if ( element == dato ): return True;
        return False;

    # Encuentra la posición de un elemento.
    def indice( self, dato ):
        index = 0;
        for element in self:
            if ( element == dato ): return index;
            index += 1;
        return -1;

    # Si la lista está vacía.
    def vacio( self ):
        return self.__frente == None and self.__final == None;

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

    print( f"Contiene << 5 >>: { lista.contiene( 5 ) }" );
    print( f"Índice de << 4 >>: { lista.indice( 4 ) }" );
    print( f"Eliminando << 7 >> y << 9 >>" );
    eliminado, dato = lista.eliminar( 5 );
    print( f"Eliminando << 5 >>: { eliminado }" );
    lista.eliminar( 7 );
    lista.eliminar( 9 );
    index = 1;
    for element in lista:
        print( f"Elemento { index }: { element }" );
        index = index + 1;
