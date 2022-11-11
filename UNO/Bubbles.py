from tkinter import *;
import random;
import math;

# Burbuja individual.
class Bubble:

    # Creación de la burbuja.
    def __init__( self, frame, angulo, x, y, speed ):
        self.x = x;
        self.y = y;
        self.frame = frame;
        self.speed = speed;
        self.angulo = angulo;

        # Imagen
        image = PhotoImage( file = "assets\\bubble.png" );
        self.label = Label( self.frame, image = image, anchor = CENTER );
        self.label.image = image;
        self.render();

    # Renderizado de la burbuja.
    def render( self ):
        self.label.place( x = self.x, y = self.y );

# Manager de burbujas.
class Bubbles:

    # Creación del manager.
    def __init__( self, frame, game ):
        self.speeds = [ 0.02, 0.03, 0.04 ];
        self.frame  = frame;
        self.game   = game;
        self.bubbles = [];

    # Spawn de burbujas.
    def spawn( self, cantidad ):
        for i in range( 0, cantidad ):
            angulo = random.randint( 0, 360 );
            x, y = self.posicion( angulo );
            speed = random.choice( self.speeds );
            bubble = Bubble( self.frame, angulo, x, y, speed );
            self.bubbles.append( bubble );

    # Posición de la burbuja en razón del ángulo.
    def posicion( self, angulo ):
        x = math.floor( ( 125 * math.cos( angulo ) ) + 400 );
        y = math.floor( ( 125 * math.sin( angulo ) ) + 200 );
        return [ x, y ];

    # Inicio del movimiento.
    def iniciar( self ):
        while ( True ):
            for bubble in self.bubbles:
                if ( self.game.reversed ): bubble.angulo -= bubble.speed;
                else: bubble.angulo += bubble.speed;
                x, y = self.posicion( bubble.angulo );
                bubble.x = x;
                bubble.y = y;
                bubble.render();
