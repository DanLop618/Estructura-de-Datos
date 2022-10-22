from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
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
        Label( frame, bg = "#f0f0f0", text = "Número a Evaluar:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Resultado:" ).place( x = 25, y = 75 );

        # Calcular el máximo común divisor.
        def collatz( num ):
            result_txt.insert( END, f"{ int( num ) }\n" );
            if ( num == 1 ): return num;
            if ( num % 2 ): return collatz( ( num * 3 ) + 1 );
            return collatz( num / 2 );

        # Obtenemos el texto
        def getText():
            num = safeCast( number_txt.get( "1.0", "end-1c" ).strip(), int );
            if ( not num ): return messagebox.showinfo( message = "¡Expresión Inválida!", title = "Error" );
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            collatz( num );
            result_txt.config( state = "disabled" );

        # Cuadros de texto.
        number_txt = Text( frame, height = 1, width = 20 );
        number_txt.place( x = 25, y = 50 );
        result_txt = Text( frame, height = 12, width = 20 );
        result_txt.place( x = 25, y = 100 );
        result_txt.config( state = "disabled" );

        # Botón de conversión.
        Button( frame, text = "Calcular", command = getText ).place( x = 285, y = 48 );

# Si el programa se ejecuta de manera individual.
if __name__ == '__main__':

    # Ventana.
    window = Tk();
    window.config( width = 425, height = 325 );
    window.title( "Menú de prácticas - Estructura de Datos" );
    window.resizable( False, False );

    # Frame Principal.
    program_frame = Frame( width = 425, height = 325, bg = "#f0f0f0" );
    program_frame.place( x = 0, y = 0 );

    # Ejecución del programa.
    program = Program();
    program.execute( program_frame );

    # Ciclo de vida de la ventana.
    window.mainloop();
