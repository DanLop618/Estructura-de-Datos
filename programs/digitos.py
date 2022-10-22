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
