"""Evalúa el nivel de prioridad de un operador.
@type operator: char
@param operator: El operador a evaluar
@rtype: int
@returns: El nivel de prioridad del operador recibido
"""
def priority( operator ):
    return {
      '+': 1,
      '-': 1,
      '*': 2,
      '/': 2,
      '^': 3
    }.get( operator, 0 );
