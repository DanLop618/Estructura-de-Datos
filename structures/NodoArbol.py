# Binodo de direcciones de memoria.
class Nodo():

    """Inicializa un nuevo Nodo de datos.
    @type dato: any
    @param dato: El dato que éste nodo almacenará
    @rtype: Nodo
    @returns: El Nodo creado
    """
    def __init__( self, dato ):
        self._dato      = dato;
        self._izquierdo = None;
        self._derecho   = None;
