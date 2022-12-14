from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from structures.Tooltip import Tooltip;
from util.safeCast import safeCast;
import util.Constants as Constants;
from structures.Pila import Pila;
from math import floor;

# Programa
class Program:

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Examen de Pilas";
        self.module = Constants.Module_Pilas;

    # Función de ejecución.
    def execute( self, frame ):

        # Variables del ejercicio.
        pila = Pila();

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Baraja:" ).place( x = 185, y = 25 );

        # Mezclar la baraja.
        def mezclar():
            aux1 = Pila();
            aux2 = Pila();
            loop = 0;
            baraja_txt.config( state = "normal" );
            baraja_txt.delete( "1.0", END );
            for i in range( 0, floor( pila.longitud() / 2 ) ): aux1.insertar( pila.remover() );
            while ( not pila.vacio() ): aux2.insertar( pila.remover() );
            while ( not aux1.vacio() and not aux2.vacio() ):
                if ( loop % 2 ):
                    dato = aux1.remover();
                    pila.insertar( dato );
                    baraja_txt.insert( "1.0", f"{ dato }\n" );
                else:
                    dato = aux2.remover();
                    pila.insertar( dato );
                    baraja_txt.insert( "1.0", f"{ dato }\n" );
                loop += 1;
            baraja_txt.config( state = "disabled" );

        # Cortar la baraja.
        def cortar():
            aux1 = Pila();
            aux2 = Pila();
            baraja_txt.config( state = "normal" );
            baraja_txt.delete( "1.0", END );
            for i in range( 0, floor( pila.longitud() / 2 ) ): aux1.insertar( pila.remover() );
            while ( not pila.vacio() ): aux2.insertar( pila.remover() );
            while ( not aux1.vacio() ):
                dato = aux1.remover();
                pila.insertar( dato );
                baraja_txt.insert( "1.0", f"{ dato }\n" );
            while ( not aux2.vacio() ):
                dato = aux2.remover();
                pila.insertar( dato );
                baraja_txt.insert( "1.0", f"{ dato }\n" );
            baraja_txt.config( state = "disabled" );

        # Reiniciar la baraja.
        def nueva():
            pila.limpiar();
            baraja_txt.config( state = "normal" );
            baraja_txt.delete( "1.0", END );
            for i in range( 1, 49 ):
                pila.insertar( i );
                baraja_txt.insert( "1.0", f"{ i }\n" );
            baraja_txt.config( state = "disabled" );

        # Cuadros de texto.
        baraja_txt = Text( frame, height = 12, width = 20 );
        baraja_txt.place( x = 125, y = 50 );
        baraja_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botón de validación.
        Button( frame, text = "Nueva", command = nueva, width = 8 ).place( x = 100, y = 260 );
        Button( frame, text = "Cortar", command = cortar, width = 8 ).place( x = 175, y = 260 );
        Button( frame, text = "Mezclar", command = mezclar, width = 8 ).place( x = 250, y = 260 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn, "Éste programa simulará un mazo de 48 cartas que podrá cortarse, mezclarse y reiniciarse." );

# Si el programa se ejecuta de manera individual.
if __name__ == '__main__':

    # Ventana.
    window = Tk();
    window.config( width = 425, height = 325 );
    window.resizable( False, False );
    window.iconphoto( False, PhotoImage( file = path.abspath( "../" ) + "\\assets\\logo.png" ) );

    # Ejecución del programa.
    program = Program();
    window.title( f"{ program.name }" );
    program.execute( window );

    # Ciclo de vida de la ventana.
    window.mainloop();
