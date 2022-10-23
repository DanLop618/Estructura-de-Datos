from structures.Nodo import Nodo;

# Definición de la estructura/clase Cola.
class Cola:

    """Inicializa una nueva Cola Lineal de datos.
    @type datos: array
    @param datos: Los datos iniciales de la cola
    @rtype: Cola
    @returns: La nueva cola lineal
    """
    def __init__( self, datos = [] ):
        self.__count  = 0;
        self.__frente = None;
        self.__final  = None;
        if ( not datos ): return;
        for dato in datos: self.insertar( dato );

    """Inserta un nuevo elemento a la cola.
    @type elemento: any
    @param elemento: El elemento a ingresar
    """
    def insertar( self, elemento ):
        nodo = Nodo( elemento, None );
        if ( self.__final ): self.__final._siguiente = nodo;
        self.__count += 1;
        self.__final = nodo;
        if ( not self.__frente ): self.__frente = nodo;

    """Remueve el elemento frente de la cola y lo devuelve para su manipulación.
    @rtype: any
    @returns: El elemento frente de la cola
    """
    def remover( self ):
        if ( self.vacio() ): raise Exception( "ErrorCola: No se pueden remover elementos: Cola vacía." );
        frente = self.__frente._dato;
        self.__frente = self.__frente._siguiente;
        self.__count -= 1;
        if ( self.__frente == None ): self.__final == None;
        return frente;

    """Verifica si la cola contiene un elemento.
    @type elemento: any
    @param elemento: El elemento a buscar
    @rtype: bool
    @returns: Si la cola contiene el elemento indicado
    """
    def contiene( self, elemento ):
        aux = Cola();
        found = False;
        while ( not self.vacio() and not found ):
            if ( self.__frente._dato == elemento ): found = True;
            aux.insertar( self.remover() );
        while ( not aux.vacio() ): self.insertar( aux.remover() );
        return found;

    """Elimina todos los elementos específicos de la cola que no cumplan con la condicion y devuelve la cola resultante.
    @type filtro: lambda
    @param filtro: El filtro que los elementos deben cumplir para no ser filtrados
    @rtype: Cola
    @returns: La cola resultante después del filtrado
    """
    def filtrar( self, filtro ):
        aux = Cola();
        filtered = Cola();
        while ( not self.vacio() ): aux.insertar( self.remover() );
        while ( not aux.vacio() ):
            dato = aux.remover();
            self.insertar( dato );
            if ( filtro( dato ) ): filtered.insertar( dato );
        return filtered;

    """Convierte la cola en una cadena de texto con los tipos de dato de cada elemento.
    @rtype: string
    @returns: La cadena de texto resultante de los elementos de la cola
    """
    def imprimir( self ):
        aux = Cola();
        cad = "";
        while ( self.__frente != None ):
            cad += f"\t({ type( self.frente() ) }) - " + str( self.frente() ) + "\n";
            aux.insertar( self.remover() );
        while ( not aux.vacio() ): self.insertar( aux.remover() );
        return cad;

    """Devuelve el elemento del frente de la cola.
    @rtype: any
    @returns: El elemento tope de la cola
    """
    def frente( self ): return self.__frente._dato if ( self.__frente != None ) else None;

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
