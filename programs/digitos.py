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
        self.name = "Contador de Digitos";
        self.module = Constants.Module_Recursividad;

    # Función de ejecución.
    def execute( self, frame ):

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Ingrese un número entero:" ).place( x = 130, y = 75 );
        Label( frame, bg = "#f0f0f0", text = "Cantidad de dígitos:" ).place( x = 150, y = 150 );

        # Validación de digitos recursiva.
        def digitCount( number ):
            if ( number < 10 ): return 1;
            if ( number % 10 ): return digitCount( number - ( number % 10 ) );
            return 1 + digitCount( number / 10 );

        # Obtención y validación de texto.
        def getText():
            number = safeCast( number_txt.get( "1.0", "end-1c" ).strip(), int );
            if ( number == None ): return messagebox.showerror( message = "¡Ingresa un entero válido!", title = "¡Error!" );
            if ( number < 0 ): number *= -1;
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            result_txt.insert( "1.0" , digitCount( number ) );
            result_txt.config( state = "disabled" );

        # Cuadros de texto.
        number_txt = Text( frame, height = 1, width = 20 );
        number_txt.place( x = 125, y = 100 );
        result_txt = Text( frame, height = 1, width = 20 );
        result_txt.place( x = 125, y = 175 );
        result_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botón de validación.
        Button( frame, text = "Calcular", command = getText ).place( x = 175, y = 210 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn, "Éste programa tomará un número entero y determinará el número de dígitos del mismo." );

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
