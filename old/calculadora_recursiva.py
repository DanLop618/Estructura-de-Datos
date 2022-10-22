from os import path, system;
import sys;

# Estructuras
sys.path.append( path.abspath( "./" ) );
from util.safeCast import safeCast;
from structures.Pila import Pila;

# Potenciación.
def pow( base, exp ):
    return 1 if ( not exp ) else base * pow( base, exp - 1 );

# Datos del programa
system( "cls" );
print( "Éste programa evaluará dos números enteros y potenciará el primero\nen relación al segundo de manera recursiva.\n\n" );
first  = safeCast( input( "Ingrese el número a elevar: " ), int );
second = safeCast( input( "Ingrese el número elevador: " ), int );
print( f"\nEl resultado es: { pow( first, second ) }" );
input( "Presione ENTER para continuar..." );
