from os import path, system;
from tkinter import *;
import sys;

# Ventana de interfaz.
window = Tk();
window.config( width = 425, height = 275 );
window.title( "Cadena Invertida" );
window.resizable( False, False );

# Labels.
input_lbl = Label( text = "Cadena a Invertir:" );
input_lbl.place( x = 25, y = 25 );
reversed_lbl = Label( text = "Cadena Invertida:" );
reversed_lbl.place( x = 25, y = 140 );

# Cuadros de texto.
input_txt = Text( window, height = 5, width = 35 );
input_txt.place( x = 25, y = 50 );
reversed_txt = Text( window, height = 5, width = 45 );
reversed_txt.place( x = 25, y = 165 );
reversed_txt.config( state = "disabled" );

# Invierte una cadena.
def reverse( expression, index = 0 ):
    if ( index < len( expression ) ): return reverse( expression, index + 1 ) + expression[ index ];
    return '';

# Obtenemos el texto
def getText():

    # Expresión recibida.
    expression = input_txt.get( "1.0", "end-1c" ).strip();

    # Expresión invertida
    reversed_txt.config( state = "normal" );
    reversed_txt.delete( "1.0", END );
    reversed_txt.insert( "1.0" , reverse( expression ) );
    reversed_txt.config( state = "disabled" );

# Botón de conversión.
reverse_btn = Button( text = "Invertir", command = getText );
reverse_btn.place( x = 315, y = 47.5 );

# Loop de interfaz.
window.mainloop();
