# Binodo de direcciones de memoria.
class Binodo():

    """Inicializa un nuevo Binodo de datos.
    @type dato: any
    @param dato: El dato que éste nodo almacenará
    @rtype: Binodo
    @returns: El binodo creado
    """
    def __init__( self, dato ):
        self._dato      = dato;
        self._siguiente = None;
        self._anterior  = None;
