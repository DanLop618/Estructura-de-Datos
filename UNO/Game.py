from structures.Bicola import Bicola;
from structures.Pila import Pila;
from PIL import ImageTk as itk;
from Bubbles import Bubbles;
from Player import Player;
from pygame import mixer;
from Carta import Carta;
from PIL import Image;
import tkinter as tk;
import threading;
import Constants;
import random;

class Game:

    # Variables internas del juego.
    jugadores = Bicola();
    usadas = Pila();
    bubbles = None;
    mazo = Pila();
    reversed = False;

    # Inicialización del juego.
    def __init__( self, frame ):

        # Burbujas
        self.bubbles = Bubbles( frame, self );
        self.bubbles.spawn( 12 );

        # Ventana del juego
        self.mixer = mixer;
        self.frame = frame;
        self.imagenes = {};
        self.sounds = {};
        self.cargarImagenes();
        self.cargarSonidos();

        # Revolver las cartas.
        aux1 = Pila();
        aux2 = Pila();
        for i in range( 0, 4 ):
            self.mazo.insertar( Carta( i, 0 ) );
            for j in range( 1, 10 ): self.mazo.insertar( Carta( i, j ) );
            for j in range( 1, 10 ): self.mazo.insertar( Carta( i, j ) );
            for j in range( 0, 2 ): self.mazo.insertar( Carta( i, 10 ) );
            for j in range( 0, 2 ): self.mazo.insertar( Carta( i, 11 ) );
            for j in range( 0, 2 ): self.mazo.insertar( Carta( i, 12 ) );
        for i in range( 0, 4 ): self.mazo.insertar( Carta( None, 13 ) );
        for i in range( 0, 4 ): self.mazo.insertar( Carta( None, 14 ) );
        totalAcciones = random.randint( 10, 25 );
        for i in range( 0, totalAcciones ):
            accion = random.randint( 0, 4 );
            if ( accion == Constants.CORTAR ): self.mazo.cortar();
            if ( accion == Constants.MEZCLAR ): self.mazo.mezclar();
            if ( accion == Constants.CORTAR_MEZCLAR ):
                self.mazo.cortar();
                self.mazo.mezclar();
            if ( accion == Constants.MEZCLAR_CORTAR ):
                self.mazo.mezclar();
                self.mazo.cortar();
            if ( accion == Constants.MEZCLAR_MEZCLAR ):
                self.mazo.mezclar();
                self.mazo.mezclar();

        # Empezamos el juego.
        self.usadas.insertar( self.mazo.remover() );
        while ( self.usadas.tope().color == None or self.usadas.tope().valor > 9 ): self.usadas.insertar( self.mazo.remover() );

        # Labels
        self.deck_lbl = tk.Label( frame, image = self.imagenes[ "reverse" ] );
        self.deck_lbl.place( x = 345, rely = 0.35 );
        self.old_lbl = tk.Label( frame );
        self.old_lbl.place( x = 435, rely = 0.35 );

    # Carga de imágenes.
    def cargarImagenes( self ):
        for i in range( 0, 4 ):
            for j in range( 0, 13 ):
                image = Image.open( f"assets\\{ i }_{ j }.png" );
                image = image.resize( ( 70, 105 ) );
                self.imagenes[ f"{ i }_{ j }" ] = itk.PhotoImage( image );
        self.imagenes[ "13" ] = itk.PhotoImage( Image.open( "assets\\13.png" ).resize( ( 70, 105 ) ) );
        self.imagenes[ "14" ] = itk.PhotoImage( Image.open( "assets\\14.png" ).resize( ( 70, 105 ) ) );
        self.imagenes[ "reverse" ] = itk.PhotoImage( Image.open( "assets\\reverse.png" ).resize( ( 70, 105 ) ) );
        self.imagenes[ "reverse-small" ] = itk.PhotoImage( Image.open( "assets\\reverse.png" ).resize( ( 20, 30 ) ) );
        self.imagenes[ "IA" ] = itk.PhotoImage( Image.open( "assets\\IA.png" ).resize( ( 35, 35 ) ) );
        self.imagenes[ "clock" ] = itk.PhotoImage( Image.open( "assets\\clock.png" ).resize( ( 50, 50 ) ) );
        self.imagenes[ "clock-small" ] = itk.PhotoImage( Image.open( "assets\\clock.png" ).resize( ( 25, 25 ) ) );

    # Sonidos del juego
    def cargarSonidos( self ):
        self.mixer.init();
        self.mixer.music.load( "assets\\sounds\\background.mp3" );
        self.sounds[ "turn" ] = self.mixer.Sound( "assets\\sounds\\turn.wav" );
        self.sounds[ "grab" ] = self.mixer.Sound( "assets\\sounds\\grab.wav" );
        self.sounds[ "release" ] = self.mixer.Sound( "assets\\sounds\\release.wav" );
        self.sounds[ "reverse" ] = self.mixer.Sound( "assets\\sounds\\reverse.mp3" );
        self.sounds[ "skip" ] = self.mixer.Sound( "assets\\sounds\\skip.wav" );

    # Actualizar la GUI
    def actualizarGUI( self ):
        tope = self.usadas.tope();
        color = tope.color;
        valor = tope.valor;
        if ( valor < 13 ): self.old_lbl[ "image" ] = self.imagenes[ f"{ color }_{ valor }" ];
        else: self.old_lbl[ "image" ] = self.imagenes[ f"{ valor }" ];
        colors = [ "#e6564c", "#6ea662", "#faf575", "#4287f5" ];
        if ( color != None ): self.frame[ "bg" ] = colors[ color ];
        for widget in self.frame.winfo_children(): widget.config( bg = self.frame[ "bg" ] );
        if ( not self.mazo.vacio() ): return;
        self.deck_lbl[ "image" ] = None;
        self.deck_lbl.unbind( "<Button-1>" );

    # Añadir un jugador.
    def agregarJugador( self, player ):
        if ( player.state == Constants.IA ):
            pos = [ [ 50, 175 ], [ 425, 75 ], [ 725, 225 ] ];
            player.posicion( pos[ self.jugadores.longitud() - 1 ] );
            for i in range( 0, 7 ): player.agregarCarta( None, self.mazo.remover() );
        else:
            player.posicion( [ None, None ] );
            for i in range( 0, 7 ): player.agregarCarta( None, self.mazo.remover() );
            self.deck_lbl.bind( "<Button-1>", lambda event: player.agregarCarta( event, self.mazo.remover() ) );
        self.jugadores.insertarFinal( player );

    # Verifica se la carta es jugable.
    def verificar( self, carta ):
        tope = self.usadas.tope();
        color = carta.color;
        valor = carta.valor;
        if ( color != None and color == tope.color ): return True;
        if ( valor == tope.valor ): return True;
        if ( valor == 13 or valor == 14 ): return True;
        return False;

    # Cuando una carta se quema.
    def cartaQuemada( self, player, carta ):
        self.sounds[ "release" ].play();
        if ( carta.cambiaSentido() ): self.cambiarSentido();
        self.siguiente();
        if ( carta.sumaCartas() ): self.jugadores.frente().tomar( carta.valor - 10 );
        if ( carta.saltaTurno() ):
            self.sounds[ "skip" ].play();
            self.siguiente();
        if ( carta.esComodin() ): return self.elegirColor( player );
        self.actualizarGUI();
        self.iniciarTurno();

    # Siguiente jugador.
    def siguiente( self ):
        if ( not self.reversed ): self.jugadores.avanzar();
        else: self.jugadores.retroceder();

    # Actualizamos el sentido del juego.
    def cambiarSentido( self ):
        self.sounds[ "reverse" ].play();
        self.reversed = not self.reversed;

    # Elegir un color del comodín.
    def elegirColor( self, player ):
        tope = self.usadas.tope();
        if ( player.state == Constants.HUMAN ):
            botones = [
                tk.Button( self.frame, width = 15, height = 3, text = "Rojo",     command = lambda: continuar( 0 ) ),
                tk.Button( self.frame, width = 15, height = 3, text = "Verde",    command = lambda: continuar( 1 ) ),
                tk.Button( self.frame, width = 15, height = 3, text = "Amarillo", command = lambda: continuar( 2 ) ),
                tk.Button( self.frame, width = 15, height = 3, text = "Azul",     command = lambda: continuar( 3 ) ),
            ];
            def continuar( color ):
                tope.color = color;
                self.actualizarGUI();
                self.iniciarTurno();
                for boton in botones: boton.destroy();
            botones[ 0 ].place( x = 300, y = 175 );
            botones[ 1 ].place( x = 450, y = 175 );
            botones[ 2 ].place( x = 300, y = 250 );
            botones[ 3 ].place( x = 450, y = 250 );
        else:
            index = random.randint( 0, 3 );
            tope.color = index;
            self.actualizarGUI();
            self.iniciarTurno();

    # Inicia el turno
    def iniciarTurno( self ):
        self.jugadores.frente().jugar();

    # Comenzar el juego:
    def comenzar( self ):
        self.mixer.music.set_volume( 0.15 );
        self.mixer.music.play( -1 );
        self.actualizarGUI();
        self.iniciarTurno();
        threading.Thread( target = self.bubbles.iniciar ).start();
