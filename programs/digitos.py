from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
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
        Label( frame, bg = "#f0f0f0", text = "Ingrese un número entero:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Cantidad de dígitos:" ).place( x = 25, y = 75 );

        # Validación de digitos recursiva.
        def digitCount( number ):
            if ( number < 10 ): return 1;
            if ( number % 10 ): return digitCount( number - ( number % 10 ) );
            return 1 + digitCount( number / 10 );

        # Obtención y validación de texto.
        def getText():
            number = safeCast( number_txt.get( "1.0", "end-1c" ).strip(), int );
            if ( not number ): return messagebox.showinfo( message = "¡Ingresa un entero válido!", title = "Error" );
            if ( number < 0 ): number *= -1;
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            result_txt.insert( "1.0" , digitCount( number ) );
            result_txt.config( state = "disabled" );

        # Cuadros de texto.
        number_txt = Text( frame, height = 1, width = 20 );
        number_txt.place( x = 25, y = 50 );
        result_txt = Text( frame, height = 1, width = 20 );
        result_txt.place( x = 25, y = 100 );
        result_txt.config( state = "disabled" );

        # Botón de validación.
        Button( frame, text = "Calcular", command = getText ).place( x = 25, y = 135 );

# Si el programa se ejecuta de manera individual.
if __name__ == '__main__':

    # Ventana.
    window = Tk();
    window.config( width = 650, height = 325 );
    window.title( "Menú de prácticas - Estructura de Datos" );
    window.resizable( False, False );

    # Frame Principal.
    program_frame = Frame( width = 425, height = 325, bg = "#f0f0f0" );
    program_frame.place( x = 225, y = 0 );

    # Ejecución del programa.
    program = Program();
    program.execute( program_frame );

    # Ciclo de vida de la ventana.
    window.mainloop();
