from os import path, system;
from math import floor;
import sys;

# Estructuras
sys.path.append( path.abspath( "./" ) );
from util.safeCast import safeCast;
from structures.Pila import Pila;

# Variables del ejercicio.
pila   = Pila();
option = None;

# Imprimir la baraja.
def imprimir():
    system( "cls" );
    print( "Orden de baraja actual:\n" );
    print( pila.imprimir() );

# Mezclar la baraja.
def mezclar():
    system( "cls" );
    aux1 = Pila();
    aux2 = Pila();
    loop = 0;
    for i in range( 0, floor( pila.longitud() / 2 ) ): aux1.insertar( pila.remover() );
    while ( not pila.vacio() ): aux2.insertar( pila.remover() );
    while ( not aux1.vacio() and not aux2.vacio() ):
        if ( loop % 2 ): pila.insertar( aux1.remover() );
        else: pila.insertar( aux2.remover() )
        loop += 1;
    print( f"¡La baraja se ha mezclado correctamente!" );

# Cortar la baraja.
def cortar():
    system( "cls" );
    aux1 = Pila();
    aux2 = Pila();
    for i in range( 0, floor( pila.longitud() / 2 ) ): aux1.insertar( pila.remover() );
    while ( not pila.vacio() ): aux2.insertar( pila.remover() );
    while ( not aux1.vacio() ): pila.insertar( aux1.remover() );
    while ( not aux2.vacio() ): pila.insertar( aux2.remover() );
    print( f"¡La baraja se ha cortado correctamente!" );

# Reiniciar la baraja.
def nueva():
    system( "cls" );
    pila.limpiar();
    for i in range( 0, 48 ): pila.insertar( i );
    print( f"¡La baraja se ha reiniciado correctamente!" );

# Menú del ejercicio.
while ( True ):

    # Información.
    system( "cls" );
    print( "Éste programa simulará los cortes y mezclas de una baraja de 48 cartas.\n" );
    print( "\t1.- Nueva Baraja" );
    print( "\t2.- Cortar Baraja" );
    print( "\t3.- Mezclar Baraja" );
    print( "\t4.- Mostrar Baraja\n" );
    print( "\t5.- Salir" );

    # Pedimos la opción deseada.
    option = safeCast( input( "\n\nIngrese la opción deseada: " ), int );
    if ( option == None ): continue;
    if ( option == 5 ): break;

    # Opciones del menú.
    if ( option == 1 ): nueva();
    if ( option == 2 ): cortar();
    if ( option == 3 ): mezclar();
    if ( option == 4 ): imprimir();

    # Pausamos el programa.
    input( "Presione ENTER para continuar..." );
