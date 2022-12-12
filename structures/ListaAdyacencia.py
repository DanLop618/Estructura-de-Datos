from structures.Arco import Arco;

class ListaAdyacencia:

    def __init__( self ):
        self.__primero = None;
        self.__ultimo  = None;

    def vacio( self ):
        return self.__primero == None;

    def adyacente( self, dato ):
        actual = self.__primero;
        while ( actual and dato != actual._destino ): actual = actual._siguiente;
        return actual != None;

    def nuevaAdyacencia( self, destino, peso ):
        if ( self.adyacente( destino ) ): return;
        nodo = Arco( destino, peso );
        self._insertar( nodo, destino );

    def _reiniciar( self ):
        actual   = self.__primero;
        anterior = None;
        while ( actual ):
            anterior = actual;
            actual   = actual._siguiente;
            anterior.siguiente = None;
        self.__primero = None;
        self.__ultimo  = None;

    def _insertar( self, nodo, destino ):
        if ( self.vacio() ):
            self.__primero = nodo;
            self.__ultimo  = nodo;
        else:
            if ( destino <= self.__primero._destino ):
                nodo._siguiente = self.__primero;
                self.__primero  = nodo;
            elif ( destino == self.__ultimo._destino ):
                self.__ultimo._siguiente = nodo;
                self.__ultimo = nodo;
            else:
                anterior = None;
                actual   = self.__primero;
                while ( actual and destino > actual._destino ):
                    anterior = actual;
                    actual   = actual._siguiente;
                nodo._siguiente     = anterior._siguiente;
                anterior._siguiente = nodo;

    def imprimir( self, incluirPeso = False ):
        print( incluirPeso );
        if ( self.vacio() ): return "";
        temporal = self.__primero;
        cadena = "";
        while ( temporal ):
            if ( incluirPeso ): cadena += "{ " + str( temporal._destino ) + ", " + str( temporal._peso ) + " };";
            else: cadena += f"{ str( temporal._destino ) };";
            temporal = temporal._siguiente;
        return cadena;

    def eliminarAdyacencia( self, dato ):
        if ( self.vacio() or not self.adyacente( dato ) ): return;
        if ( self.__primero == self.__ultimo ): return self._reiniciar();
        actual   = self.__primero;
        anterior = None;
        while ( actual and dato >actual._destino ):
            anterior = actual;
            actual   = actual._siguiente;
        if ( actual == self.__primero ): self.__primero = self.__primero._siguiente;
        elif ( actual == self.__ultimo  ):
            anterior._siguiente = None;
            self.__ultimo = anterior;
        else:
            anterior._siguiente = actual._siguiente;
            actual.siguiente    = None;
