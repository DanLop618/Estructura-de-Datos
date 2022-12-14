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
        self.name = "Palíndromos";
        self.module = Constants.Module_Pilas;

    # Función de ejecución.
    def execute( self, frame ):

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Expresión a validar:" ).place( x = 157.5, y = 100 );

        # Validación.
        def validate( expression ):

            # Pilas de almacenamiento.
            pila_1  = Pila();
            pila_2  = Pila();
            pila_3  = Pila();

            # Añadimos las letras a las pilas correspondientes.
            for letter in expression:
                if ( letter == ' ' ): continue;
                pila_1.insertar( letter );
                pila_2.insertar( letter );

            # Movemos los elementos de la pila 2 a la 3.
            while ( not pila_2.vacio() ):
                pila_3.insertar( pila_2.remover() );

            # Verificamos los elementos de la pila.
            while( not pila_1.vacio() ):
                if ( pila_1.remover() != pila_3.remover() ): return False;

            # Retornamos verdadero.
            return True;

        # Obtención del texto.
        def getText():
            expression = input_txt.get( "1.0", "end-1c" ).strip();
            if ( not expression ): return messagebox.showerror( message = "¡Ingresa una expresión válida!", title = "¡Error!" );
            message = "¡La expresión es palíndroma!";
            if ( not validate( expression ) ): message = "¡La expresión NO es palíndroma!";
            messagebox.showinfo( message = message, title = "Validación" );

        # Input de texto.
        input_txt = Text( frame, height = 1, width = 20 );
        input_txt.place( x = 125, y = 125 );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botón de validación.
        Button( frame, text = "Validar", command = getText ).place( x = 187.5, y = 165 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn,
            "Éste programa validará si una expresión es palíndroma o no.\n\nUna expresión palíndroma es aquella " +
            "que es escrita/leída igualmente al derecho y al revés (sin tomar en cuenta los espacios)." );

# Si el programa se ejecuta de manera individual.
if __name__ == '__main__':

    # Ventana.
    window = Tk();
    window.config( width = 425, height = 325 );
    window.resizable( False, False );
    window.iconphoto( False, PhotoImage( file = path.abspath( "../" ) + "\\assets\\logo.png" ) );

    # Ejecución del programa.
    program = Program();
    window.title( f"{ program.name }" );
    program.execute( window );

    # Ciclo de vida de la ventana.
    window.mainloop();
