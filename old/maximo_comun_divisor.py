from tkinter import messagebox;
from os import path, system;
from tkinter import *;
import sys;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from util.safeCast import safeCast;

# Ventana de interfaz.
window = Tk();
window.config( width = 425, height = 275 );
window.title( "Máximo Común Divisor" );
window.resizable( False, False );

# Labels.
first_lbl = Label( text = "Primer Número:" );
first_lbl.place( x = 25, y = 25 );
second_lbl = Label( text = "Sugundo Número:" );
second_lbl.place( x = 25, y = 75 );
result_lbl = Label( text = "Máximo Común Divisor:" );
result_lbl.place( x = 25, y = 150 );

# Cuadros de texto.
first_txt = Text( window, height = 1, width = 20 );
first_txt.place( x = 25, y = 50 );
second_txt = Text( window, height = 1, width = 20 );
second_txt.place( x = 25, y = 100 );
result_txt = Text( window, height = 1, width = 20 );
result_txt.place( x = 25, y = 175 );
result_txt.config( state = "disabled" );

# Calcular el máximo común divisor.
def comun_divisor( num1, num2 ):
    print( f"Número 1: { num1 }\nNúmero 2: { num2 }\n" );
    if ( num1 == num2 ): return num1;
    if ( num1 < num2 ): return comun_divisor( num1, num2 - num1 );
    return comun_divisor( num1 - num2, num2 );

# Obtenemos el texto
def getText():

    # Expresión recibida.
    num1 = safeCast( first_txt.get( "1.0", "end-1c" ).strip(), int );
    num2 = safeCast( second_txt.get( "1.0", "end-1c" ).strip(), int );

    # Si no son números válidos.
    if ( not num1 or not num2 ): return messagebox.showinfo( message = "¡Expresión Inválida!", title = "Error" );

    # Expresión invertida
    result_txt.config( state = "normal" );
    result_txt.delete( "1.0", END );
    result_txt.insert( "1.0" , comun_divisor( num1, num2 ) );
    result_txt.config( state = "disabled" );

# Botón de conversión.
calculate_btn = Button( text = "Calcular", command = getText );
calculate_btn.place( x = 285, y = 47.5 );

# Loop de interfaz.
window.mainloop();
