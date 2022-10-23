from structures.Nodo import Nodo;

# Definición de la estructura/clase Pila..
class Pila:

    """Inicializa una nueva Pila de datos.
    @type datos: array
    @param datos: Los datos iniciales de la pila
    @rtype: Pila
    @returns: La pila creada
    """
    def __init__( self, datos = [] ):
        self.__count = 0;
        self.__tope  = None;
        if ( not datos ): return;
        for dato in datos: self.insertar( dato );

    """Inserta un nuevo elemento a la pila.
    @type elemento: any
    @param elemento: El elemento a ingresar
    """
    def insertar( self, elemento ):
        nodo = Nodo( elemento, self.__tope );
        self.__count += 1;
        self.__tope = nodo;

    """Remueve el elemento tope de la pila y lo devuelve para su manipulación.
    @rtype: any
    @returns: El elemento tope de la pila
    """
    def remover( self ):
        if ( self.__tope == None ): raise Exception( "ErrorPila: No se pueden remover elementos: Pila vacía." );
        tope = self.__tope._dato;
        self.__tope = self.__tope._siguiente;
        self.__count -= 1;
        return tope;

    """Verifica si la pila contiene un elemento.
    @type elemento: any
    @param elemento: El elemento a buscar
    @rtype: bool
    @returns: Si la pila contiene el elemento indicado
    """
    def contiene( self, elemento ):
        aux = Pila();
        found = False;
        while ( self.__tope != None and not found ):
            if ( self.__tope._dato == elemento ): found = True;
            aux.insertar( self.remover() );
        while ( not aux.vacio() ): self.insertar( aux.remover() );
        return found;

    """Encuentra la posición del primer elemento que sea igual al elemtno indicado.
    @type elemento: any
    @param elemento: El elemento a buscar
    @rtype: int || None
    @returns: La posición del elemento indicado, o un valor nulo
    """
    def indice( self, elemento ):
        if ( self.__tope == None or not self.contiene( elemento ) ): return None;
        aux = Pila();
        index = 0;
        while ( self.__tope != None and self.__tope._dato != elemento ): aux.insertar( self.remover() );
        while ( not aux.vacio() ):
            self.insertar( aux.remover() );
            index += 1;
        return index;

    """Elimina todos los elementos específicos de la pila que no cumplan con la condicion y devuelve la pila resultante.
    @type filtro: lambda
    @param filtro: El filtro que los elementos deben cumplir para no ser filtrados
    @rtype: Pila
    @returns: La pila resultante después del filtrado
    """
    def filtrar( self, filtro ):
        aux = Pila();
        filtered = Pila();
        while ( self.__tope != None ): aux.insertar( self.remover() );
        while ( not aux.vacio() ):
            dato = aux.remover();
            self.insertar( dato );
            if ( filtro( dato ) ): filtered.insertar( dato );
        return filtered;

    """Convierte la pila en una cadena de texto con los tipos de dato de cada elemento.
    @rtype: string
    @returns: La cadena de texto resultante de los elementos de la pila
    """
    def imprimir( self ):
        aux = Pila();
        cad = "";
        while ( self.__tope != None ):
            cad += f"\t({ type( self.tope() ) }) - " + str( self.tope() ) + "\n";
            aux.insertar( self.remover() );
        while ( aux.__tope != None ): self.insertar( aux.remover() );
        return cad;

    """Devuelve la cantidad de elementos dentro de la pila.
    @rtype: int
    @returns: El número de elementos totales dentro de la pila
    """
    def longitud( self ): return self.__count;

    """Devuelve el elemento tope de la pila.
    @rtype: any
    @returns: El elemento tope de la pila
    """
    def tope( self ): return self.__tope._dato if ( self.__tope != None ) else None;

    """Verifica si la pila se encuentra vacía.
    @rtype: bool
    @returns: Si la pila está vacía o no
    """
    def vacio( self ): return self.__tope == None;

    """Elimina todos los elementos de la pila."""
    def limpiar( self ):
        self.__count = 0;
        self.__tope = None;
