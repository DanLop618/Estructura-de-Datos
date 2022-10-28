# Binodo de direcciones de memoria.
class Nodo():

    """Inicializa un nuevo Binodo de datos.
    @type dato: any
    @param dato: El dato que éste nodo almacenará
    @type siguiente: Nodo || None
    @param siguiente: El binodo siguiete al cual apunta éste binodo
    @type siguiente: Nodo || None
    @param siguiente: El binodo anterior al que apunta éste binodo
    @rtype: Binodo
    @returns: El binodo creado
    """
    def __init__( self, dato, siguiente, anterior ):
        self._dato      = dato;
        self._siguiente = siguiente;
        self._anterior  = anterior;
