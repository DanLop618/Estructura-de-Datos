from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from util.safeCast import safeCast;
import util.Constants as Constants;
from structures.Pila import Pila;

# Programa
class Program:

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Iteración de Números";
        self.module = Constants.Module_Pilas;

    # Función de ejecución.
    def execute( self, frame ):

        # Pilas.
        pila = Pila();
        auxiliar = Pila();

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Número de Iteraciones:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Pila Ordenada:" ).place( x = 200, y = 25 );

        # Añadimos los elementos.
        def iterate():
            size = safeCast( input_txt.get( "1.0", "end-1c" ).strip(), int );
            if ( size == None ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );
            for number in range( 0, size + 1 ):
                if ( not number % 2 ): pila.insertar( number );
                if ( number % 2 ):
                    while ( not pila.vacio() ): auxiliar.insertar( pila.remover() );
                    pila.insertar( number );
                    while ( not auxiliar.vacio() ): pila.insertar( auxiliar.remover() );
            stack_txt.config( state = "normal" );
            stack_txt.delete( "1.0", END );
            while ( not pila.vacio() ): auxiliar.insertar( pila.remover() );
            while ( not auxiliar.vacio() ):
                dato = auxiliar.remover();
                stack_txt.insert( "1.0", f"{ dato }\n" );
            stack_txt.config( state = "disabled" );

        # Cuadros de texto.
        input_txt = Text( frame, height = 1, width = 20 );
        input_txt.place( x = 25, y = 50 );
        stack_txt = Text( frame, height = 15, width = 20 );
        stack_txt.place( x = 200, y = 50 );
        stack_txt.config( state = "disabled" );

        # Botón de validación.
        Button( frame, text = "Iterar", command = iterate ).place( x = 25, y = 75 );

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
