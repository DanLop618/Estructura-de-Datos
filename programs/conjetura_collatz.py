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
class Program():

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Cojetura de Collatz";
        self.module = Constants.Module_Recursividad;

    # Función de ejecución.
    def execute( self, frame ):

        # Labels.
        Label( frame, bg = "#f0f0f0", text = "Número a Evaluar:" ).place( x = 150, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Resultado:" ).place( x = 175, y = 125 );

        # Calcular el máximo común divisor.
        def collatz( num ):
            result_txt.insert( END, f"{ int( num ) }\n" );
            if ( num == 1 ): return num;
            if ( num % 2 ): return collatz( ( num * 3 ) + 1 );
            return collatz( num / 2 );

        # Obtenemos el texto
        def getText():
            num = safeCast( number_txt.get( "1.0", "end-1c" ).strip(), int );
            if ( not num ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            collatz( num );
            result_txt.config( state = "disabled" );

        # Cuadros de texto.
        number_txt = Text( frame, height = 1, width = 20 );
        number_txt.place( x = 125, y = 50 );
        result_txt = Text( frame, height = 9, width = 20 );
        result_txt.place( x = 125, y = 150 );
        result_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botones.
        Button( frame, text = "Calcular", command = getText ).place( x = 175, y = 75 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn, "Éste programa tomará un número entero y ejecutará la conjetura de Collatz respectiva." );

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
