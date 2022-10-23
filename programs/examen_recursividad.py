from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from structures.Tooltip import Tooltip;
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
        Label( frame, bg = "#f0f0f0", text = "Ingrese un número:" ).place( x = 150, y = 75 );
        Label( frame, bg = "#f0f0f0", text = "Resultado:" ).place( x = 175, y = 125 );

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
            if ( num == None ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );
            if ( num < 0 ): num *= -1;
            result_txt.config( state = "normal" );
            result_txt.delete( "1.0", END );
            result_txt.insert( "1.0", calcularSerie( 1, num ) );
            result_txt.config( state = "disabled" );

        # Comando invertir
        def invertir():
            num = safeCast( getText(), int );
            if ( num == None ): return messagebox.showerror( message = "¡Ingrese un entero válido!", title = "¡Error!" );
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
        number_txt.place( x = 125, y = 100 );
        result_txt = Text( frame, height = 1, width = 20 );
        result_txt.place( x = 125, y = 150 );
        result_txt.config( state = "disabled" );

        # Imagen de información.
        info_img = PhotoImage( file = path.abspath( ( "./", "../" )[ __name__ == "__main__" ] ) + "\\assets\\info.png" );

        # Botón de validación.
        Button( frame, text = "Calcular", command = serie, width = 8 ).place( x = 125, y = 175 );
        Button( frame, text = "Invertir", command = invertir, width = 8 ).place( x = 225, y = 175 );
        info_btn = Button( frame, highlightthickness = 0, bd = 0, image = info_img );
        info_btn.image = info_img; # Referencia para evitar el GarbageCollector
        info_btn.place( x = 5, y = 5 );

        # Tooltips
        Tooltip( info_btn,
            "Éste programa tomará un número entero y calculará la siguiente sumatoria:\n\n\t" +
            "SUM 1 / i | i = 1 -> n\n\nAdemás, el programá podrá invertir el número entero ingresado." );

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
