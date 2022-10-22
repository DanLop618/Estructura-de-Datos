from os import path, system;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from util.safeCast import safeCast;
from structures.Pila import Pila;

# Input del usuario.
size = None;
while ( size == None or size < 0 ):
    system( "cls" );
    print( "Éste programa iterará el orden de las pilas.\n" );
    size = safeCast( input( "\tIngrese el número máximo de iteración (+): " ), int );

# Pilas.
pila = Pila();
auxiliar = Pila();

# Añadimos los elementos.
for number in range( 0, size + 1 ):
    if ( not number % 2 ): pila.insertar( number );
    if ( number % 2 ):
        while ( not pila.vacio() ): auxiliar.insertar( pila.remover() );
        pila.insertar( number );
        while ( not auxiliar.vacio() ): pila.insertar( auxiliar.remover() );

# Imprimimos los datos.
system( "cls" );
print( "Elementos de la pila.\n" );
print( pila.imprimir() );

# Pausamos el programa.
input( "Presione ENTER para continuar..." );
