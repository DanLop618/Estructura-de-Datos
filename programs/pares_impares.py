from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
import util.Constants as Constants;
from util.safeCast import safeCast;
from structures.Cola import Cola;

# Programa
class Program:

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Números Pares e Impares";
        self.module = Constants.Module_Colas;

    # Función de ejecución.
    def execute( self, frame ):

        # Pila del ejercicio.
        cola = Cola();

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Dato a Ingresar:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Cola Original:" ).place( x = 25, y = 125 );
        Label( frame, bg = "#f0f0f0", text = "Cola Pares:" ).place( x = 150, y = 125 );
        Label( frame, bg = "#f0f0f0", text = "Cola Impares:" ).place( x = 275, y = 125 );

        # Actualizar labels.
        def update():
            impares = cola.filtrar( lambda el: int( el ) % 2 );
            pares = cola.filtrar( lambda el: not ( int( el ) % 2 ) );
            pares_txt.config( state = "normal" );
            pares_txt.delete( "1.0", END );
            impares_txt.config( state = "normal" );
            impares_txt.delete( "1.0", END );
            while ( not impares.vacio() ): impares_txt.insert( END, f"{ impares.remover() }\n" );
            while ( not pares.vacio() ): pares_txt.insert( END, f"{ pares.remover() }\n" );
            pares_txt.config( state = "disabled" );
            impares_txt.config( state = "disabled" );

        # Inserción de un dato.
        def insertar():
            data = safeCast( input_txt.get("1.0", "end-1c" ).strip(), int );
            if ( data == None ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );
            cola.insertar( data );
            queue_txt.config( state = "normal" );
            queue_txt.insert( END, f"{ data }\n" );
            queue_txt.config( state = "disabled" );
            update();

        # Remover un dato.
        def remover():
            if ( cola.vacio() ): return messagebox.showerror( message = "¡Cola vacía!", title = "¡Error!" );
            cola.remover();
            queue_txt.config( state = "normal" );
            queue_txt.delete( "1.0", "2.0" );
            queue_txt.config( state = "disabled" );
            update();

        # Input de texto.
        input_txt = Text( frame, height = 1, width = 20 );
        input_txt.place( x = 25, y = 50 );
        queue_txt = Text( frame, height = 10, width = 12 );
        queue_txt.place( x = 25, y = 150 );
        queue_txt.config( state = "disabled" );
        pares_txt = Text( frame, height = 10, width = 12 );
        pares_txt.place( x = 150, y = 150 );
        pares_txt.config( state = "disabled" );
        impares_txt = Text( frame, height = 10, width = 12 );
        impares_txt.place( x = 275, y = 150 );
        impares_txt.config( state = "disabled" );

        # Botones.
        Button( frame, text = "Insertar", command = insertar, width = 9 ).place( x = 25, y = 75 );
        Button( frame, text = "Remover", command = remover, width  = 9 ).place( x = 115, y = 75 );

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
