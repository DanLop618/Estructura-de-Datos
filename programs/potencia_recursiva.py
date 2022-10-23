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
        self.name = "Potencia Recursiva";
        self.module = Constants.Module_Recursividad;

    # Función de ejecución.
    def execute( self, frame ):

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Base:" ).place( x = 145, y = 75 );
        Label( frame, bg = "#f0f0f0", text = "Exponente:" ).place( x = 220, y = 75 );
        Label( frame, bg = "#f0f0f0", text = "Resultado:" ).place( x = 175, y = 175 );

        # Potenciación.
        def pow( base, exp ):
            return 1 if ( not exp ) else base * pow( base, exp - 1 );

        # Obtención del texto
        def getText( textbox ):
            data = safeCast( textbox.get( "1.0", "end-1c" ).strip(), int );
            return data;

        # Elevamos los números ingresados.
        def elevar():
            first  = getText( first_txt );
            second = getText( second_txt );
            if ( first == None or second == None ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            result_txt.insert( "1.0", pow( first, second ) );
            result_txt.config( state = "disabled" );

        # Cuadros de texto.
        first_txt = Text( frame, height = 1, width = 9 );
        first_txt.place( x = 125, y = 100 );
        second_txt = Text( frame, height = 1, width = 9 );
        second_txt.place( x = 215, y = 100 );
        result_txt = Text( frame, height = 1, width = 20 );
        result_txt.place( x = 125, y = 200 );
        result_txt.config( state = "disabled" );

        # Botón de validación.
        Button( frame, text = "Elevar", command = elevar, width = 10 ).place( x = 165, y = 125 );

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
