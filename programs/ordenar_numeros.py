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
        self.name = "Ordenamiento de Números";
        self.module = Constants.Module_Pilas;

    # Función de ejecución.
    def execute( self, frame ):

        # Variables del ejercicio.
        pila = Pila();
        aux  = Pila();

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Dato a Ingresar:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Pila Ordenada:" ).place( x = 200, y = 25 );

        # Insertar dato.
        def insertar():
            data = safeCast( input_txt.get( "1.0", "end-1c" ).strip(), int );
            if ( data == None ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );
            while ( not pila.vacio() and pila.tope() < data ): aux.insertar( pila.remover() );
            pila.insertar( data );
            while ( not aux.vacio() ): pila.insertar( aux.remover() );
            while ( not pila.vacio() ): aux.insertar( pila.remover() );
            stack_txt.config( state = "normal" );
            stack_txt.delete( "1.0", END );
            while ( not aux.vacio() ):
                element = aux.remover();
                stack_txt.insert( "1.0", f"{ element }\n" );
                pila.insertar( element );
            stack_txt.config( state = "disabled" );

        # Limpiar pila.
        def limpiar():
            pila.limpiar();
            stack_txt.config( state = "normal" );
            stack_txt.delete( "1.0", END );
            stack_txt.config( state = "disabled" );

        # Cuadros de texto.
        input_txt = Text( frame, height = 1, width = 20 );
        input_txt.place( x = 25, y = 50 );
        stack_txt = Text( frame, height = 15, width = 20 );
        stack_txt.place( x = 200, y = 50 );
        stack_txt.config( state = "disabled" );

        # Botón de validación.
        Button( frame, text = "Insertar", command = insertar ).place( x = 25, y = 75 );
        Button( frame, text = "Limpiar", command = limpiar ).place( x = 85, y = 75 );

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
