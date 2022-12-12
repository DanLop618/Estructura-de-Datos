from structures.ListaAdyacencia import ListaAdyacencia;

class Nodo:

    def __init__( self, dato, lista, siguiente = None ):
        self._dato      = dato;
        self._lista     = lista;
        self._siguiente = siguiente;
