class Arco:

    """Inicializa un nuevo arco de vértices.
    @type destino: nodo
    @param destino: El nodo de destino
    @type peso: int
    @param peso: El peso del arco
    @type siguiente: nodo
    @param siguiente: El nodo siguiente al actual
    @rtype: Arco
    @returns: El arco
    """
    def __init__( self, destino, peso, siguiente = None ):
        self._destino   = destino;
        self._peso      = peso;
        self._siguiente = siguiente;
