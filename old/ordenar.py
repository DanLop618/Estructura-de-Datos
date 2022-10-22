from os import path, system;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from util.safeCast import safeCast;
from structures.Pila import Pila;

# Variables del ejercicio.
pila   = Pila();
option = None;

# Añadir un elemento a la pila.
def insertar():
    system( "cls" );
    dato = input( "Ingrese el dato a añadir: " );
    aux = Pila();
    while ( not pila.vacio() and pila.tope() < dato ): aux.insertar( pila.remover() );
    pila.insertar( dato );
    while ( not aux.vacio() ): pila.insertar( aux.remover() );
    print( f"¡El dato << { dato } >> ha sido añadido a la pila!" );

# Imprimir la pila.
def imprimir():
    system( "cls" );
    if ( pila.vacio() ): return print( f"¡No hay elementos en la pila!" );
    print( "A continuación se mostrarán los elementos de la pila.\n" );
    print( pila.imprimir() );

# Menú del ejercicio.
while ( True ):

    # Información.
    system( "cls" );
    print( "Éste programa le permitirá añadir elementos a una pila y las ordenará.\n" );
    print( "\t1.- Añadir" );
    print( "\t2.- Imprimir" );
    print( "\t3.- Salir" );

    # Pedimos la opción deseada.
    option = safeCast( input( "\n\nIngrese la opción deseada: " ), int );
    if ( option == None ): continue;
    if ( option == 3 ): break;

    # Opciones del menú.
    if ( option == 1 ): insertar();
    if ( option == 2 ): imprimir();

    # Pausamos el programa.
    input( "Presione ENTER para continuar..." );
