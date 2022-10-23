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
        self.name = "Máximo Común Divisor";
        self.module = Constants.Module_Recursividad;

    # Función de ejecución.
    def execute( self, frame ):

        # Labels.
        Label( frame, text = "Primer Número:" ).place( x = 25, y = 25 );
        Label( frame, text = "Sugundo Número:" ).place( x = 25, y = 75 );
        Label( frame, text = "Máximo Común Divisor:" ).place( x = 25, y = 150 );

        # Calcular el máximo común divisor.
        def comun_divisor( num1, num2 ):
            #print( f"Número 1: { num1 }\nNúmero 2: { num2 }\n" );
            if ( num1 == num2 ): return num1;
            if ( num1 < num2 ): return comun_divisor( num1, num2 - num1 );
            return comun_divisor( num1 - num2, num2 );

        # Obtenemos el texto
        def getText():

            # Expresión recibida.
            num1 = safeCast( first_txt.get( "1.0", "end-1c" ).strip(), int );
            num2 = safeCast( second_txt.get( "1.0", "end-1c" ).strip(), int );

            # Si no son números válidos.
            if ( num1 == None or num2 == None ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );

            # Si son valores negativos.
            if ( num1 < 0 ): num1 *= -1;
            if ( num2 < 0 ): num2 *= -1;

            # Expresión invertida
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            result_txt.insert( "1.0" , comun_divisor( num1, num2 ) );
            result_txt.config( state = "disabled" );

        # Cuadros de texto.
        first_txt = Text( frame, height = 1, width = 20 );
        first_txt.place( x = 25, y = 50 );
        second_txt = Text( frame, height = 1, width = 20 );
        second_txt.place( x = 25, y = 100 );
        result_txt = Text( frame, height = 1, width = 20 );
        result_txt.place( x = 25, y = 175 );
        result_txt.config( state = "disabled" );

        # Botón de conversión.
        Button( text = "Calcular", command = getText ).place( x = 285, y = 47.5 );

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
