from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from structures.Tooltip import Tooltip;
from structures.Bicola import Bicola;
import util.Constants as Constants;

# Programa
class Program:

    # Inicializador del programa.
    def __init__( self ):
        self.name = "Métodos de Colas";
        self.module = Constants.Module_Colas;

    # Función de ejecución.
    def execute( self, frame ):

        # Pila del ejercicio.
        cola = Bicola();

        # Labels
        Label( frame, bg = "#f0f0f0", text = "Dato a Ingresar:" ).place( x = 25, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Cola de Datos:" ).place( x = 215, y = 25 );
        Label( frame, bg = "#f0f0f0", text = "Búsqueda / Filtro:" ).place( x = 25, y = 150 );
        frente_lbl  = Label( frame, bg = "#f0f0f0", text = "Tope: " );
        frente_lbl.place( x = 25, y = 250 );
        final_lbl  = Label( frame, bg = "#f0f0f0", text = "Tope: " );
        final_lbl.place( x = 25, y = 275 );
        total_lbl = Label( frame, bg = "#f0f0f0", text = "Elementos Totales: 0" );
        total_lbl.place( x = 25, y = 300 );

        # Actualizar labels.
        def update():
            frente = '';
            final = '';
            total = 0;
            if ( cola.frente() ): frente = cola.frente();
            if ( cola.final() ): final = cola.final();
            if ( cola.longitud() ): total = cola.longitud();
            frente_lbl[ "text" ] = f"Frente: { frente }";
            final_lbl[ "text" ] = f"Final: { final }";
            total_lbl[ "text" ] = f"Elementos Totales: { total }";

        # Obtención del texto
        def getText( textbox ):
            data = textbox.get( "1.0", "end-1c" ).strip();
            textbox.delete( "1.0", END );
            return data;

        # Inserción de un dato.
        def insertar( frente = False ):
            data = getText( input_txt );
            if ( not data ): return messagebox.showerror( message = "¡Ingrese un dato!", title = "¡Error!" );
            cola.insertar( data, frente );
            queue_txt.config( state = "normal" );
            if ( frente ): queue_txt.insert( "1.0", f"{ data }\n" );
            else: queue_txt.insert( END, f"{ data }\n" );
            queue_txt.config( state = "disabled" );
            update();

        # Remover un dato.
        def remover( frente = True ):
            if ( cola.vacio() ): return messagebox.showerror( message = "¡Cola vacía!", title = "¡Error!" );
            queue_txt.config( state = "normal" );
            if ( frente ):
                cola.avanzar();
                queue_txt.delete( "1.0", "2.0" );
            else:
                queue_txt.delete( f"{ cola.longitud() }.0", END );
                cola.retroceder();
            queue_txt.config( state = "disabled" );
            update();

        # Buscar un dato.
        def buscar():
            data = getText( search_txt );
            if ( not data ): return messagebox.showerror( message = "¡Ingrese un dato a buscar!", title = "¡Error!" );
            if ( not cola.contiene( data ) ): return messagebox.showerror( message = "¡Dato no encontrado!", title = "¡Error!" );
            messagebox.showinfo( message = "¡El dato se encontró con éxito!", title = "¡Éxito!" );

        # Limpiar cola.
        def limpiar():
            if ( cola.vacio() ): return messagebox.showerror( message = "¡Cola vacía!", title = "¡Error!" );
            while( not cola.vacio() ): cola.avanzar();
            queue_txt.config( state = "normal" );
            queue_txt.delete( "1.0", END );
            queue_txt.config( state = "disabled" );
            update();

        # Filtrar los datos.
        def filtrar():
            filtro = getText( search_txt );
            if ( not filtro ): return messagebox.showerror( message = "¡Expresión lambda inválida!", title = "¡Error!" );
            try:
                filtered = cola.filtrar( lambda el: eval( filtro ) );
                messagebox.showinfo( message = f"La cola resultante es la siguiente:\n\n{ filtered.imprimir() }\nOcurrencias: { filtered.longitud() }", title = "¡Filtrado!" );
            except ( NameError, SyntaxError ):
                messagebox.showerror( message = "¡Expresión lambda inválida!", title = "¡Error!" );

        # Input de texto.
        input_txt = Text( frame, height = 1, width = 20 );
        input_txt.place( x = 25, y = 50 );
        search_txt = Text( frame, height = 1, width = 20 );
        search_txt.place( x = 25, y = 175 );
        queue_txt = Text( frame, height = 15, width = 22 );
        queue_txt.place( x = 215, y = 50 );
        queue_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botones.
        Button( frame, text = "Insertar Frente", command = lambda: insertar( True ), width = 9 ).place( x = 25, y = 75 );
        Button( frame, text = "Insertar Final", command = lambda: insertar(), width  = 9 ).place( x = 115, y = 75 );
        Button( frame, text = "Remover Frente", command = lambda: remover(), width = 9 ).place( x = 25, y = 105 );
        Button( frame, text = "Remover Final", command = lambda: remover( False ), width  = 9 ).place( x = 115, y = 105 );
        Button( frame, text = "Búsqueda", command = buscar, width = 9 ).place( x = 25, y = 200 );
        Button( frame, text = "Vaciar", command = limpiar, width = 9 ).place( x = 115, y = 230 );
        filter_btn = Button( frame, text = "Filtrar", command = filtrar, width  = 9 );
        filter_btn.place( x = 115, y = 200 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn, "Éste programa le permitirá manipular una cola lineal de datos mediante sus métodos." );
        Tooltip( filter_btn,
            "Convierte la expresión recibida en una función LAMBDA e itera todos los elementos de la cola, filtrando " +
            "los elementos que no cumplan con la condición de la función.\n\nEjemplo:\n\n\tint( el ) > 0\n\nDevuelve " +
            "la cola resultante de todos los elementos convertidos a enteros que sean mayores a 0." );

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
