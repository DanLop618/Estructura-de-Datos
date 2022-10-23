from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from structures.Tooltip import Tooltip;
from util.safeCast import safeCast;
import util.Constants as Constants;

# Programa
class Program:

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Invertir Cadena";
        self.module = Constants.Module_Recursividad;

    # Función de ejecución.
    def execute( self, frame ):

        # Labels
        Label( frame, text = "Cadena a Invertir:" ).place( x = 165, y = 25 );
        Label( frame, text = "Cadena Invertida:" ).place( x = 165, y = 185 );

        # Invierte una cadena.
        def reverse( expression, index = 0 ):
            if ( index < len( expression ) ): return reverse( expression, index + 1 ) + expression[ index ];
            return '';

        # Obtención del texto
        def getText():

            # Expresión recibida.
            expression = input_txt.get( "1.0", "end-1c" ).strip();

            # Expresión invertida
            reversed_txt.config( state = "normal" );
            reversed_txt.delete( "1.0", END );
            reversed_txt.insert( "1.0" , reverse( expression ) );
            reversed_txt.config( state = "disabled" );

        # Cuadros de texto.
        input_txt = Text( frame, height = 5, width = 35 );
        input_txt.place( x = 75, y = 50 );
        reversed_txt = Text( frame, height = 5, width = 35 );
        reversed_txt.place( x = 75, y = 210 );
        reversed_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botón de validación.
        Button( frame, text = "Invertir", command = getText, width = 10 ).place( x = 175, y = 145 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn, "Éste programa invertirá la cadena de texto recibida, incluyendo los saltos de línea." );

# Si el programa se ejecuta de manera individual.
if __name__ == '__main__':

    # Ventana.
    window = Tk();
    window.config( width = 425, height = 325 );
    window.resizable( False, False );
    window.iconphoto( False, PhotoImage( file = path.abspath( "../" ) + "\\logo.png" ) );

    # Ejecución del programa.
    program = Program();
    window.title( f"{ program.name }" );
    program.execute( window );

    # Ciclo de vida de la ventana.
    window.mainloop();
