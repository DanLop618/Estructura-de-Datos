from structures.Binodo import Binodo;

# Definición de la estructura/clase Cola.
class Bicola:

    """Inicializa una nueva Bicola de datos.
    @type datos: tuple
    @param datos: Los datos iniciales de la cola
    @rtype: Bicola
    @returns: La nueva bicola de datos
    """
    def __init__( self, *datos ):
        self.__count  = 0;
        self.__frente = None;
        self.__final  = None;
        if ( not datos ): return;
        for dato in datos: self.insertar( dato );

    """Inserta un nuevo elemento a la bicola.
    @type elemento: any
    @param elemento: El elemento a ingresar
    """
    def insertarFrente( self, elemento ):
        nodo = Binodo( elemento );
        self.__count += 1;
        if ( self.vacio() ):
            self.__frente = nodo;
            self.__final  = nodo;
            self.__frente._siguiente = self.__final;
            self.__final._anterior = self.__frente;
        else:
            nodo._siguiente = self.__frente;
            nodo._anterior = self.__final;
            self.__frente._anterior = nodo;
            self.__final._siguiente = nodo;
            self.__frente = nodo;

    """Inserta un nuevo elemento a la bicola.
    @type elemento: any
    @param elemento: El elemento a ingresar
    """
    def insertarFinal( self, elemento ):
        nodo = Binodo( elemento );
        self.__count += 1;
        if ( self.vacio() ):
            self.__frente = nodo;
            self.__final  = nodo;
            self.__frente._siguiente = self.__final;
            self.__final._anterior = self.__frente;
        else:
            self.__final._siguiente = nodo;
            nodo._anterior = self.__final;
            nodo._siguiente = self.__frente;
            self.__frente._anterior = nodo;
            self.__final = nodo;

    """Remueve el elemento frente de la bicola y lo devuelve para su manipulación.
    @rtype: any
    @returns: El elemento frente de la bicola
    """
    def removerFrente( self ):
        if ( self.vacio() ): raise Exception( "ErrorBicola: No se pueden remover elementos: Bicola vacía." );
        self.__count -= 1;
        frente = self.__frente._dato;
        if ( self.__frente == self.__final ):
            self.__frente = None;
            self.__final = None;
        else:
            self.__frente = self.__frente._siguiente;
            self.__frente._anterior = self.__final;
        return frente;

    """Remueve el elemento final de la bicola y lo devuelve para su manipulación.
    @rtype: any
    @returns: El elemento final de la bicola
    """
    def removerFinal( self ):
        if ( self.vacio() ): raise Exception( "ErrorBicola: No se pueden remover elementos: Bicola vacía." );
        self.__count -= 1;
        final = self.__final._dato;
        if ( self.__frente == self.__final ):
            self.__frente = None;
            self.__final = None;
        else:
            self.__final = self.__final._anterior;
            self.__final._siguiente = self.__frente;
        return final;

    """Avanzamos en un nodo en la bicola."""
    def avanzar( self ):
        if ( self.vacio() ): raise Exception( "ErrorBicola: No se puede avanzar: Bicola vacía." );
        self.insertarFinal( self.removerFrente() );
        # self.__frente = self.__frente._siguiente;
        # self.__final = self.__final._siguiente;

    """Retrocedemos un nodo en la bicola."""
    def retroceder( self ):
        if ( self.vacio() ): raise Exception( "ErrorBicola: No se puede avanzar: Bicola vacía." );
        self.insertarFrente( self.removerFinal() );
        # self.__frente = self.__frente._anterior;
        # self.__final = self.__final._anterior;

    """Verifica si la bicola contiene un elemento.
    @type elemento: any
    @param elemento: El elemento a buscar
    @rtype: bool
    @returns: Si la bicola contiene el elemento indicado
    """
    def contiene( self, elemento ):
        aux = Bicola();
        found = False;
        while ( not self.vacio() and not found ):
            if ( self.__frente._dato == elemento ): found = True;
            aux.insertar( self.remover() );
        while ( not aux.vacio() ): self.insertar( aux.remover() );
        return found;

    """Elimina todos los elementos específicos de la bicola que no cumplan con la condicion y devuelve la bicola resultante.
    @type filtro: lambda
    @param filtro: El filtro que los elementos deben cumplir para no ser filtrados
    @rtype: Biola
    @returns: La bicola resultante después del filtrado
    """
    def filtrar( self, filtro ):
        aux = Bicola();
        filtered = Bicola();
        while ( not self.vacio() ): aux.insertar( self.remover() );
        while ( not aux.vacio() ):
            dato = aux.remover();
            self.insertar( dato );
            if ( filtro( dato ) ): filtered.insertar( dato );
        return filtered;

    """Convierte la bicola en una cadena de texto con los tipos de dato de cada elemento.
    @rtype: string
    @returns: La cadena de texto resultante de los elementos de la bicola
    """
    def imprimir( self, principio = True ):
        aux = Bicola();
        cad = "";
        if ( principio ):
            while ( not self.vacio() ):
                cad += f"\t({ type( self.frente() ) }) - " + str( self.frente() ) + "\n";
                aux.insertar( self.avanzar() );
            while ( not aux.vacio() ): self.insertar( aux.avanzar() );
        else:
            while ( not self.vacio() ):
                cad += f"\t({ type( self.final() ) }) - " + str( self.final() ) + "\n";
                aux.insertar( self.retroceder() );
            while ( not aux.vacio() ): self.insertar( aux.retroceder() );
        return cad;

    """Devuelve el elemento del frente de la bicola.
    @rtype: any
    @returns: El elemento tope de la bicola
    """
    def frente( self ): return self.__frente._dato if ( self.__frente != None ) else None;

    """Devuelve el elemento del final de la bicola.
    @rtype: any
    @returns: El elemento final de la bicola
    """
    def final( self ): return self.__final._dato if ( self.__final != None ) else None;

    """Verifica si la cola se encuentra vacía.
    @rtype: bool
    @returns: Si la cola está vacía o no
    """
    def vacio( self ): return self.__frente == None;

    """Devuelve la cantidad de elementos dentro de la cola.
    @rtype: int
    @returns: El número de elementos totales dentro de la cola
    """
    def longitud( self ): return self.__count;
