from structures.NodoArbol import Nodo;
from util.Constants import Constants;

class Arbol:

    def __init__( self ):
        self.__raiz = None;

    def vacio( self ):
        return self.__raiz == None;

    def reiniciar( self ):
        self.__raiz = None;

    def imprimir( self, opcion ):
        texto = "";
        if ( opcion == Constants.Prefijo  ): cadena = self.__prefijo(  self.__raiz );
        if ( opcion == Constants.Postfijo ): cadena = self.__postfijo( self.__raiz );
        if ( opcion == Constants.Infijo   ): cadena = self.__infijo(   self.__raiz );
        return cadena;

    def insertar( self, dato ):
        self.__raiz = self.__insertarNodo( self.__raiz, dato );

    def remover( self, dato ):
        if ( self.vacio() ): raise Exception( "ErrorArbol: No se pueden remover elementos: Árbol vacío." );
        nodo = self.__buscarNodo( dato );
        if ( nodo != None ): self.__raiz = self.__eliminarNodo( self.__raiz, dato );
        # return nodo._dato if nodo != None else None;
        return ( nodo._dato, None )[ nodo != None ];

    def buscar( self, dato ):
        return self.__buscarNodo( dato ) != None;

    def __insertarNodo( self, subarbol, dato ):
        if ( subarbol != None ):
            if ( dato < subarbol._dato ): subarbol._izquierdo = self.__insertarNodo( subarbol._izquierdo, dato );
            else: subarbol._derecho = self.__insertarNodo( subarbol._derecho, dato );
        else: subarbol = Nodo( dato );
        return subarbol;

    def __buscarNodo( self, dato ):
        if ( self.vacio() ): return None;
        actual = self.__raiz;
        while ( actual != None and dato != actual._dato ):
            if ( dato < actual._dato ): actual = actual._izquierdo;
            else: actual = actual._derecho;
        return actual;

    def __eliminarNodo( self, subarbol, dato ):
        if ( subarbol == None ): return None;
        elif ( dato < subarbol._dato ): subarbol._izquierdo = self.__eliminarNodo( subarbol._izquierdo, dato );
        elif ( dato > subarbol._dato ): subarbol._derecho   = self.__eliminarNodo( subarbol._derecho, dato );
        else:
            nodo = subarbol;
            if ( nodo._derecho == None ): subarbol = nodo._izquierdo;
            elif ( nodo._izquierdo == None ): subarbol = nodo._derecho;
            else:
                nodo = self.__cambiarNodo( nodo );
                nodo = None;
        return subarbol;

    def __cambiarNodo( self, cambio ):
        nodo = cambio;
        hijo = nodo._izquierdo;
        while ( hijo._derecho != None ):
            nodo = hijo;
            hijo = hijo._derecho;
        nodo._dato = hijo._dato;
        if ( nodo == cambio ): nodo._izquierdo = hijo._izquierdo;
        else: nodo._derecho = hijo._izquierdo;
        return hijo;

    def __prefijo( self, subarbol ):
        if ( subarbol == None ): return "";
        return subarbol._dato + "\n" + self.__prefijo( subarbol._izquierdo ) + self.__prefijo( subarbol._derecho );

    def __postfijo( self, subarbol ):
        if ( subarbol == None ): return "";
        return self.__postfijo( subarbol._izquierdo ) + self.__postfijo( subarbol._derecho ) + subarbol._dato + '\n';

    def __infijo( self, subarbol ):
        if ( subarbol == None ): return "";
        return self.__infijo( subarbol._izquierdo ) + subarbol._dato + '\n' + self.__infijo( subarbol._derecho );
