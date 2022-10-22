from tkinter import messagebox;
from os import path, system;
from math import floor;
from tkinter import *;
import sys;
import re;

# Estructuras
sys.path.append( path.abspath( "../" ) );
from util.reverseExpression import reverseExpression;
from util.priority import priority;
from util.safeCast import safeCast;
from structures.Pila import Pila;

# Variables del ejercicio.
option = None;

# Ventana de interfaz.
window = Tk();
window.config( width = 425, height = 275 );
window.title( "Prefijo - Postfijo" );
window.resizable( False, False );

# Conversión de una expresión a prefijo.
def prefix( expression ):

    # Creamos la expresión resultante.
    operandos  = Pila();
    operadores = Pila();
    operand = "";

    # Iteramos los caracteres dentro de la expresión.
    for char in expression:

        # Si el caracter es un número o letra, lo añadimos como operando.
        if ( re.search( r"[\d\w.,]", char ) ):

            # Buscamos repeticiones en puntos y comas.
            if ( len( re.findall( r"[.,]", operand ) ) > 1 ): return messagebox.showinfo( message = "¡Expresión Inválida!", title = "Error" );
            operand += char;

        # Si es un operador.
        else:

            # Añadimos el operando completo a la expresión final y reiniciamos el contenedor de operando.
            if ( operand != "" ): operandos.insertar( operand );
            operand = "";

            # Si es un paréntesis que cierra.
            if ( char == ')' ):
                while ( operadores.tope() != '(' ):
                    operando2 = operandos.remover();
                    operando1 = operandos.remover();
                    operador  = operadores.remover();
                    operandos.insertar( f"{ operador } { operando1 } { operando2 }" );
                operadores.remover();
                continue;

            # Si el operador es de mayor jerarquía que el anterior.
            while ( not operadores.vacio() and priority( char ) <= priority( operadores.tope() ) and char != '(' ):
                if ( operadores.tope() == '(' ): break;
                operando2 = operandos.remover();
                operando1 = operandos.remover();
                operador  = operadores.remover();
                operandos.insertar( f"{ operador } { operando1 } { operando2 }" );

            # Añadimos el operador a la pila de operadores.
            operadores.insertar( char );

    # Añadimos el operando final y los operadores restantes.
    if ( operand != "" ): operandos.insertar( operand );
    while ( not operadores.vacio() ):
        operando2 = operandos.remover();
        operando1 = operandos.remover();
        operador  = operadores.remover();
        operandos.insertar( f"{ operador } { operando1 } { operando2 }" );
    return operandos.remover();

# Conversión de una expresión a postfijo.
def postfix( expression ):

    # Creamos la expresión resultante.
    operadores = Pila();
    finalExpression = [];
    operand = "";

    # Iteramos los caracteres dentro de la expresión.
    for char in expression:

        # Si el caracter es un número o letra, lo añadimos como operando.
        if ( re.search( r"[\d\w.,]", char ) ):

            # Buscamos repeticiones en puntos y comas.
            if ( len( re.findall( r"[.,]", operand ) ) > 1 ): return messagebox.showinfo( message = "¡Expresión Inválida!", title = "Error" );
            operand += char;

        # Si es un operador.
        else:

            # Añadimos el operando completo a la expresión final y reiniciamos el contenedor de operando.
            if ( operand != "" ): finalExpression.append( operand );
            operand = "";

            # Si es un paréntesis que cierra.
            if ( char == ')' ):
                while ( operadores.tope() != '(' ): finalExpression.append( operadores.remover() );
                operadores.remover();
                continue;

            # Si el operador es de mayor jerarquía que el anterior.
            while ( not operadores.vacio() and priority( char ) <= priority( operadores.tope() ) and char != '(' ):
                if ( operadores.tope() == '(' ): break;
                finalExpression.append( operadores.remover() );

            # Añadimos el oprador a la pila.
            operadores.insertar( char );

    # Añadimos el operando final y los operadores restantes.
    if ( operand != "" ): finalExpression.append( operand );
    while ( not operadores.vacio() ): finalExpression.append( operadores.remover() );
    return ' '.join( finalExpression );

# Obtención de la expresión.
def getText():

    # Obtenemos el texto del text box.
    incomplete = False;
    expression = input_txt.get( "1.0", "end-1c" ).strip();

    # Buscamos sintáxis inválidas dentro de la expresión recibida.
    invalid = re.findall( r"[(\[{][)\]}]|[+\-/*^.,]{2,}|[+\-/*^(\[{]$|^[+\-/*^)\]}]", expression );
    if ( len( re.findall( r"\(", expression ) ) != len( re.findall( r"\)", expression ) ) ): incomplete = True;
    if ( len( re.findall( r"\[", expression ) ) != len( re.findall( r"\]", expression ) ) ): incomplete = True;
    if ( len( re.findall( r"\{", expression ) ) != len( re.findall( r"\}", expression ) ) ): incomplete = True;
    if ( invalid or incomplete ): return messagebox.showinfo( message = "¡Expresión Inválida!", title = "Error" );

    # Expresión convertida a postfijo
    postfix_txt.config( state = "normal" );
    postfix_txt.delete( "1.0", END );
    postfix_txt.insert( "1.0" , postfix( expression ) );
    postfix_txt.config( state = "disabled" );

    # Prefijo
    #prefix = postfix( reverseExpression( expression ) );
    prefix_txt.config( state = "normal" );
    prefix_txt.delete( "1.0", END );
    prefix_txt.insert( "1.0", prefix( expression ) );
    #prefix_txt.insert( "1.0" , reverseExpression( prefix ) );
    prefix_txt.config( state = "disabled" );


# Labels.
input_lbl = Label( text = "Expresión a Convertir:" );
input_lbl.place( x = 25, y = 25 );
postfix_lbl = Label( text = "Expresión Postfijo:" );
postfix_lbl.place( x = 25, y = 100 );
prefix_lbl = Label( text = "Expresión Prefijo:" );
prefix_lbl.place( x = 25, y = 175 );

# Cuadros de texto.
input_txt = Text( window, height = 1, width = 35 );
input_txt.place( x = 25, y = 50 );
postfix_txt = Text( window, height = 1, width = 45 );
postfix_txt.place( x = 25, y = 125 );
postfix_txt.config( state = "disabled" );
prefix_txt = Text( window, height = 1, width = 45 );
prefix_txt.place( x = 25, y = 200 );
prefix_txt.config( state = "disabled" );

# Botón de conversión.
convert_btn = Button( text = "Convertir", command = getText );
convert_btn.place( x = 315, y = 47.5 );

# Loop de interfaz.
window.mainloop();
