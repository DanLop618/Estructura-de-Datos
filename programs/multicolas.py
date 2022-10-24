from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from structures.Tooltip import Tooltip;
from util.safeCast import safeCast;
import util.Constants as Constants;
from structures.Cola import Cola;

# Programa
class Program:

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Multicolas";
        self.module = Constants.Module_Colas;

    # Función de ejecución.
    def execute( self, frame ):

        # Variables del ejercicio
        cola1   = Cola();
        cola2   = Cola();
        cola3   = Cola();
        general = Cola();

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Entrada:" ).place( relx = 0.5, rely = 0.1, anchor = CENTER );

        # Insertar en la primera cola.
        def insertar1():
            data = getText();
            if ( not data ): return messagebox.showerror( message = "¡Ingrese un dato!", title = "¡Error!" );
            cola1.insertar( data );
            cola1_txt.config( state = "normal" );
            cola1_txt.insert( END, f"{ data }\n" );
            cola1_txt.config( state = "disabled" );

        # Insertar en la primera cola.
        def insertar2():
            data = getText();
            if ( not data ): return messagebox.showerror( message = "¡Ingrese un dato!", title = "¡Error!" );
            cola2.insertar( data );
            cola2_txt.config( state = "normal" );
            cola2_txt.insert( END, f"{ data }\n" );
            cola2_txt.config( state = "disabled" );

        # Insertar en la primera cola.
        def insertar3():
            data = getText();
            if ( not data ): return messagebox.showerror( message = "¡Ingrese un dato!", title = "¡Error!" );
            cola3.insertar( data );
            cola3_txt.config( state = "normal" );
            cola3_txt.insert( END, f"{ data }\n" );
            cola3_txt.config( state = "disabled" );

        # Unir colas.
        def unir():
            aux = Cola();
            general_txt.config( state = "normal" );
            general_txt.delete( "1.0", END );
            while ( not cola1.vacio() or not cola2.vacio() or not cola3.vacio() ):
                if ( not cola1.vacio() ): general.insertar( cola1.remover() );
                if ( not cola2.vacio() ): general.insertar( cola2.remover() );
                if ( not cola3.vacio() ): general.insertar( cola3.remover() );
            while ( not general.vacio() ):
                data = general.remover();
                aux.insertar( data );
                general_txt.insert( END, f"{ data }\n" );
            while ( not aux.vacio() ): general.insertar( aux.remover() );
            general_txt.config( state = "disabled" );
            cola1_txt.config( state = "normal" );
            cola1_txt.delete( "1.0", END );
            cola1_txt.config( state = "disabled" );
            cola2_txt.config( state = "normal" );
            cola2_txt.delete( "1.0", END );
            cola2_txt.config( state = "disabled" );
            cola3_txt.config( state = "normal" );
            cola3_txt.delete( "1.0", END );
            cola3_txt.config( state = "disabled" );

        # Obtención del texto
        def getText():
            data = input_txt.get( "1.0", "end-1c" ).strip();
            input_txt.delete( "1.0", END );
            return data;

        # Cuadros de texto.
        input_txt = Text( frame, height = 1, width = 20 );
        input_txt.place( relx = 0.5, rely = 0.2, anchor = CENTER );
        cola1_txt = Text( frame, height = 10, width = 10 );
        cola1_txt.place( relx = 0.0725, rely = 0.4, anchor = NW );
        cola1_txt.config( state = "disabled" );
        cola2_txt = Text( frame, height = 10, width = 10 );
        cola2_txt.place( relx = 0.3, rely = 0.4, anchor = NW );
        cola2_txt.config( state = "disabled" );
        cola3_txt = Text( frame, height = 10, width = 10 );
        cola3_txt.place( relx = 0.525, rely = 0.4, anchor = NW );
        cola3_txt.config( state = "disabled" );
        general_txt = Text( frame, height = 10, width = 10 );
        general_txt.place( relx = 0.75, rely = 0.4, anchor = NW );
        general_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botón de validación.
        Button( frame, text = "Cola 1", command = insertar1 ).place( relx = 0.175, rely = 0.35, anchor = CENTER );
        Button( frame, text = "Cola 2", command = insertar2 ).place( relx = 0.3875, rely = 0.35, anchor = CENTER );
        Button( frame, text = "Cola 3", command = insertar3 ).place( relx = 0.625, rely = 0.35, anchor = CENTER );
        Button( frame, text = "Unir", command = unir ).place( relx = 0.865, rely = 0.35, anchor = CENTER );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn,
            "Éste programa le permitirá añadir elementos a diferentes colas de manera opcional. De la misma manera, " +
            "las colas se podrán unificar tomando n elementos de cada cola para enviarlos a una cola unificada." );

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
