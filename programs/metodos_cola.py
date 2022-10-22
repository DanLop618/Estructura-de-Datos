from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
import util.Constants as Constants;
from structures.Cola import Cola;

# Programa
class Program:

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Métodos de Colas";
        self.module = Constants.Module_Colas;

    # Función de ejecución.
    def execute( self, frame ):

        # Pila del ejercicio.
        cola = Cola();

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Dato a Ingresar:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Cola de Datos:" ).place( x = 215, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Búsqueda / Filtro:" ).place( x = 25, y = 125 );
        tope_lbl  = Label( frame, bg = "#f0f0f0", text = "Tope: " );
        tope_lbl.place( x = 25, y = 225 );
        total_lbl = Label( frame, bg = "#f0f0f0", text = "Elementos Totales: 0" );
        total_lbl.place( x = 25, y = 250 );

        # Actualizar labels.
        def update():
            tope = '';
            total = 0;
            if ( cola.frente() ): tope = cola.frente();
            if ( cola.longitud() ): total = cola.longitud();
            tope_lbl[ "text" ] = f"Tope: { tope }";
            total_lbl[ "text" ] = f"Elementos Totales: { total }";

        # Obtención del texto
        def getText( textbox ):
            data = textbox.get("1.0", "end-1c" ).strip();
            return data;

        # Inserción de un dato.
        def insertar():
            data = getText( input_txt );
            if ( not data ): return messagebox.showinfo( message = "¡Expresión Inválida!", title = "¡Error!" );
            cola.insertar( data );
            stack_txt.config( state = "normal" );
            stack_txt.insert( END, f"{ data }\n" );
            stack_txt.config( state = "disabled" );
            update();

        # Remover un dato.
        def remover():
            if ( cola.vacio() ): return messagebox.showinfo( message = "¡Cola Vacía!", title = "¡Error!" );
            cola.remover();
            stack_txt.config( state = "normal" );
            stack_txt.delete( "1.0", "2.0" );
            stack_txt.config( state = "disabled" );
            update();

        # Buscar un dato.
        def buscar():
            data = getText( search_txt );
            if ( not data ): return messagebox.showinfo( message = "¡Expresión Inválida!", title = "¡Error!" );
            if ( not cola.contiene( data ) ): return messagebox.showinfo( message = "¡Dato no encontrado!", title = ":(" );
            messagebox.showinfo( message = "¡Dato encontrado!", title = ":D" );

        # Limpiar cola.
        def limpiar():
            if ( cola.vacio() ): return messagebox.showinfo( message = "¡Cola Vacía!", title = "¡Error!" );
            while( not cola.vacio() ): cola.remover();
            stack_txt.config( state = "normal" );
            stack_txt.delete( "1.0", END );
            stack_txt.config( state = "disabled" );
            update();

        # Filtrar los datos.
        def filtrar():
            filtro = getText( search_txt );
            if ( not filtro ): return messagebox.showinfo( message = "¡Expresión Lambda Inválida!", title = "¡Error!" );
            try:
                filtered = cola.filtrar( lambda el: eval( filtro ) );
                messagebox.showinfo( message = f"La pila resultante es la siguiente:\n\n{ filtered.imprimir() }\nOcurrencias: { filtered.longitud() }", title = "¡Filtrado!" );
            except ( NameError, SyntaxError ):
                messagebox.showinfo( message = "¡Expresión Lambda Inválida!", title = "¡Error!" );

        # Input de texto.
        input_txt = Text( frame, height = 1, width = 20 );
        input_txt.place( x = 25, y = 50 );
        search_txt = Text( frame, height = 1, width = 20 );
        search_txt.place( x = 25, y = 150 );
        stack_txt = Text( frame, height = 15, width = 22 );
        stack_txt.place( x = 215, y = 50 );
        stack_txt.config( state = "disabled" );

        # Botones.
        Button( frame, text = "Insertar", command = insertar, width = 9 ).place( x = 25, y = 75 );
        Button( frame, text = "Remover", command = remover, width  = 9 ).place( x = 115, y = 75 );
        Button( frame, text = "Búsqueda", command = buscar, width = 9 ).place( x = 25, y = 175 );
        Button( frame, text = "Filtrar", command = filtrar, width  = 9 ).place( x = 115, y = 175 );
        Button( frame, text = "Vaciar", command = limpiar, width = 9 ).place( x = 25, y = 275 );
