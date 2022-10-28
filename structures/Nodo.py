# Nodo de direcciones de memoria.
class Nodo():

    """Inicializa un nuevo Nodo de datos.
    @type dato: any
    @param dato: El dato que éste nodo almacenará
    @type siguiente: Nodo || None
    @param siguiente: El nodo siguiente al que apunta éste nodo
    @rtype: Nodo
    @returns: El nodo creado
    """
    def __init__( self, dato, siguiente ):
        self._dato      = dato;
        self._siguiente = siguiente;
