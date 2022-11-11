# Dependencias necesarias.
import subprocess;
try:
    from PIL import ImageTk as itk;
    from PIL import Image;
    import pygame;
except ( ImportError, ModuleNotFoundError ):
    command = "Python -m pip install image pygame";
    process = subprocess.Popen( command.split(), stdout = subprocess.PIPE );
    print( "Descargando dependencias..." );
    process.communicate();

# Dependencias locales.
from Player import Player;
from Game import Game;
import tkinter as tk;
import Constants;

# GUI del usuario.
if __name__ == "__main__":

    # Colores.
    colors = [ "#e6564c", "#6ea662", "#faf575", "#4287f5" ];

    # Ventana.
    window = tk.Tk();
    window.config( width = 850, height = 475, bg = colors[ 0 ] );
    window.resizable( False, False );
    window.title( "UNO" );

    # Juego.
    game = Game( window );
    game.agregarJugador( Player( game, Constants.HUMAN ) );
    game.agregarJugador( Player( game, Constants.IA ) );
    game.agregarJugador( Player( game, Constants.IA ) );
    game.agregarJugador( Player( game, Constants.IA ) );

    # Inicializamos el juego.
    game.comenzar();
    window.mainloop();
