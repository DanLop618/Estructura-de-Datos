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
        self.name = "Examen de Recursividad";
        self.module = Constants.Module_Recursividad;

    # Función de ejecución.
    def execute( self, frame ):

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Ingrese un número:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Resultado:" ).place( x = 25, y = 75 );

        # Validación de digitos recursiva.
        def digitos( numero ):
            if ( numero < 10 ): return 1;
            if ( numero % 10 ): return digitos( numero - ( numero % 10 ) );
            return 1 + digitos( numero / 10 );

        # Calcular serie.
        def calcularSerie( index, n ):
            if ( index < n ): return ( 1 / index ) + calcularSerie( index + 1, n );
            return 1 / index;

        # Invertir número
        def invertirNumero( numero ):
            if ( numero < 10 ): return numero;
            residuo = numero % 10;
            return residuo * 10 ** ( digitos( numero ) - 1 ) + invertirNumero( ( numero - residuo ) / 10 );

        # Comando serie.
        def serie():
            num = safeCast( getText(), int );
            if ( num == None ): return messagebox.showinfo( message = "¡Ingrese un Entero Válido!", title = "¡Error!" );
            if ( num < 0 ): num *= -1;
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            result_txt.insert( "1.0", calcularSerie( 1, num ) );
            result_txt.config( state = "disabled" );

        # Comando invertir
        def invertir():
            num = safeCast( getText(), int );
            if ( num == None ): return messagebox.showinfo( message = "¡Ingrese un Entero Válido!", title = "¡Error!" );
            if ( num < 0 ): num *= -1;
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            result_txt.insert( "1.0", int( invertirNumero( num ) ) );
            result_txt.config( state = "disabled" );

        # Obtención del texto
        def getText():
            return number_txt.get( "1.0", "end-1c" ).strip();

        # Cuadros de texto.
        number_txt = Text( frame, height = 1, width = 20 );
        number_txt.place( x = 25, y = 50 );
        result_txt = Text( frame, height = 1, width = 20 );
        result_txt.place( x = 25, y = 100 );
        result_txt.config( state = "disabled" );

        # Botón de validación.
        Button( frame, text = "Calcular", command = serie ).place( x = 25, y = 125 );
        Button( frame, text = "Invertir", command = invertir ).place( x = 85, y = 125 );

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
