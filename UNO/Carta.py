import Constants;

class Carta:

    # Atributos iniciales de la carta.
    def __init__( self, color, valor ):
        self.color  = color;
        self.valor  = valor;
        self.imagen = None;
        self.label  = None;

    # Destruimos la carta.
    def quemar( self ):
        self.imagen = None;
        if ( not self.label ): return;
        self.label.destroy();
        self.label = None;

    # Si la carta es comodín.
    def esComodin( self ):
        return ( self.valor == Constants.PICK_COLOR or self.valor == Constants.GRAB_FOUR );

    # Si la carta añade cartas al oponente.
    def sumaCartas( self ):
        return ( self.valor == Constants.GRAB_TWO or self.valor == Constants.GRAB_FOUR );

    # si la carta salta turno.
    def saltaTurno( self ):
        return ( self.valor == Constants.SKIP or self.valor == Constants.GRAB_TWO or self.valor == Constants.GRAB_FOUR );

    # Si la carta revierte el sentido del juego.
    def cambiaSentido( self ):
        return self.valor == Constants.REVERSE;
