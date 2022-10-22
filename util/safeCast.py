"""Realiza un casteo seguro de un dato hacia otro tipo de dato.
@type value: any
@param value: El dato a castear
@type type: datatype
@param type: El tipo de dato a realizar el casteo
@returns: El dato casteado o un valor nulo en caso de no poderse realizar.
"""
def safeCast( value, type ):
    try:
        return type( value );
    except ( ValueError, TypeError ):
        return None;
