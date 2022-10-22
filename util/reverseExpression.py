from os import path;
import sys;
import re;

# Importamos la estrucutra de Pilas.
sys.path.append( path.abspath( "../" ) );
from structures.Pila import Pila;

"""Convierte una expresión a sí misma leída en reversa, respetando los dígitos y variables.
@type expression: string
@param expression: La expresión a convertir
@rtype: string
@returns: La expresión convertida en reversa
"""
def reverseExpression( expression ):
    pila = Pila();
    reversed = "";
    operand  = "";
    for char in expression:
        if ( re.findall( r"[\d\w.,]", char ) ): operand += char;
        else:
            if ( operand != "" ): pila.insertar( operand );
            operand = "";
            if ( char == '(' ): char = ')';
            elif ( char == ')' ): char = '(';
            pila.insertar( char );
    if ( operand != "" ): pila.insertar( operand );
    while ( not pila.vacio() ): reversed += pila.remover();
    return reversed;
