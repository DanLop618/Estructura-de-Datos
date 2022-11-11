from structures.Pila import Pila;
from threading import Timer;
import tkinter as tk;
from os import path;
import Constants;
import random;

# Jugador.
class Player:

    # Inicialización del jugador.
    def __init__( self, game, state ):
        self.cartas = [];
        self.state = state;
        self.game = game;
        self.x = None;
        self.y = None;

        # Imagen del reloj.
        image = None;
        if ( state == Constants.IA ): image = game.imagenes[ "clock-small" ];
        else: image = game.imagenes[ "clock" ];
        self.clock = tk.Label( game.frame, image = image );

        # Imagen de personaje.
        if ( state == Constants.HUMAN ): return;
        self.icon = tk.Label( game.frame, image = game.imagenes[ "IA" ] );

    # Asignamos la posición de las cartas.
    def posicion( self, pos ):
        self.x = pos[ 0 ];
        self.y = pos[ 1 ];
        if ( pos[ 0 ] == None ): return;
        self.icon.place( x = self.x, y = self.y - 45 );

    # Agrega una carta y crea los elementos necesarios para visualizarla.
    def agregarCarta( self, event, carta ):
        if ( self.state == Constants.HUMAN ):
            if ( event != None and self.game.jugadores.frente() != self ): return;
            self.game.sounds[ "grab" ].play();
            if ( carta.color != None ): carta.imagen = self.game.imagenes[ f"{ carta.color }_{ carta.valor }" ];
            else: carta.imagen = self.game.imagenes[ f"{ carta.valor }" ];
            carta.label = tk.Label( self.game.frame, image = carta.imagen );
            carta.label.bind( "<Button-1>", lambda event: self.soltarCarta( event, carta ) );
        else:
            carta.imagen = self.game.imagenes[ "reverse-small" ];
            carta.label = tk.Label( self.game.frame, image = carta.imagen );
        self.cartas.append( carta );
        self.actualizarGUI();
        self.game.actualizarGUI();
        puede, useless = self.puede();
        if ( not puede and event != None ):
            self.game.siguiente();
            self.game.iniciarTurno();
            self.actualizarGUI();

    # Actualiza el GUI de las cartas.
    def actualizarGUI( self ):
        if ( self != self.game.jugadores.frente() ): self.clock.place_forget();
        if ( self.state == Constants.HUMAN ):
            divisiones = len( self.cartas ) + 1;
            index = 1;
            for carta in self.cartas:
                relx = 0.15 + ( 0.6 / divisiones ) * index;
                carta.label.place( relx = relx, rely = 0.7 );
                index += 1;
        else:
            x = self.x;
            for carta in self.cartas:
                carta.label.place( x = x, y = self.y );
                x += 10;

    # si el jugador contiene una crata específica.
    def tiene( self, data ):
        return self.cartas.contiene( data );

    # Si el jugador contiene una carta para poder jugar.
    def puede( self ):
        color = self.game.usadas.tope().color;
        valor = self.game.usadas.tope().valor;
        carta = None;
        for carta in self.cartas:
            if ( carta.color == color or carta.valor == valor ): return [ True, carta ];
            if ( carta.valor == 13 or carta.valor == 14 ): return [ True, carta ];
        return [ False, None ];

    # Tomar una carta.
    def tomar( self, cantidad = 1 ):
        self.game.sounds[ "grab" ].play();
        for i in range( 0, cantidad ): self.agregarCarta( None, self.game.mazo.remover() );

    # Dejar una carta.
    def soltarCarta( self, event, carta ):
        if ( self.game.jugadores.frente() != self ): return;
        if ( not self.game.verificar( carta ) ): return;
        index = self.cartas.index( carta );
        carta.quemar();
        self.game.usadas.insertar( carta );
        del self.cartas[ index ];
        self.game.cartaQuemada( self, carta );
        self.actualizarGUI();

    # Juega automáticamente.
    def jugar( self ):
        if ( self.state == Constants.HUMAN ):
            self.game.sounds[ "turn" ].play();
            self.clock.place( x = 50, y = 375 );
            return;
        else:
            self.clock.place( x = self.x + 35, y = self.y - 35 );
            def iniciar():
                puede, carta = self.puede();
                if ( not puede ): self.tomar( 1 );
                puede, carta = self.puede();
                if ( not puede ):
                    self.game.siguiente();
                    self.game.iniciarTurno();
                    self.actualizarGUI();
                else:
                    self.soltarCarta( None, carta );
            Timer( random.randint( 2, 5 ), iniciar ).start();
