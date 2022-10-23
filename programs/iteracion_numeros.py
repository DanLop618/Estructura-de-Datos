from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from structures.Tooltip import Tooltip;
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
        Label( frame, bg = "#f0f0f0", text = "Número de Iteraciones:" ).place( x = 140, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Pila Ordenada:" ).place( x = 165, y = 110 );

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
        input_txt.place( x = 125, y = 50 );
        stack_txt = Text( frame, height = 10, width = 20 );
        stack_txt.place( x = 125, y = 135 );
        stack_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botón de validación.
        Button( frame, text = "Iterar", command = iterate, width = 10 ).place( x = 165, y = 75 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn,
            "Éste programa tomará un número entero y rellenará la pila de datos con todos los números desde el 0 " +
            "hasta él mismo, ordenando los números pares por encima del 0 y los impares por debajo.\n\nEjemplo:" +
            "\n\n\t..., 4, 2, 0, 1, 3, ..." );

# Si el programa se ejecuta de manera individual.
if __name__ == '__main__':

    # Ventana.
    window = Tk();
    window.config( width = 425, height = 325 );
    window.resizable( False, False );
    window.iconphoto( False, PhotoImage( file = path.abspath( "../" ) + "\\logo.png" ) );

    # Ejecución del programa.
    program = Program();
    window.title( f"{ program.name }" );
    program.execute( window );

    # Ciclo de vida de la ventana.
    window.mainloop();
