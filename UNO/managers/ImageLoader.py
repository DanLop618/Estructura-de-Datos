from managers.Loader import Loader;
from PIL import ImageTk as itk;
from math import floor;
from PIL import Image;
import tkinter as tk;
from os import walk;

class ImageLoader( Loader ):

    def __init__( self ):
        self.subfolder = "images";
        super( ImageLoader, self ).__init__( self.subfolder );
        self.load();

    def load( self ):
        for folder in [ "cards", "gui", "misc" ]:
            files = None;
            directory = walk( f"{ self.directory }\\{ folder }" );
            for ( root, dir, images ) in directory: files = images;
            for file in files:
                name   = file[ :-4 ];
                width  = 850;
                height = 475;
                image  = Image.open( f"{ self.directory }\\{ folder }\\{ file }" );
                if ( name == "reverse" ):
                    normal = image.resize( ( floor( 0.08 * width ), floor( 0.22 * height ) ) );
                    small  = image.resize( ( floor( 0.02 * width ), floor( 0.06 * height ) ) );
                    self.set( f"{ name }", itk.PhotoImage( normal ) );
                    self.set( f"{ name }-small", itk.PhotoImage( small ) );
                elif ( name == "clock" ):
                    normal = image.resize( ( floor( 0.06 * width ), floor( 0.11 * height ) ) );
                    small = image.resize( ( floor( 0.03 * width ), floor( 0.05 * height ) ) );
                    self.set( f"{ name }", itk.PhotoImage( normal ) );
                    self.set( f"{ name }-small", itk.PhotoImage( small ) );
                elif ( name == "IA" ):
                    image = image.resize( ( floor( 0.04 * width ), floor( 0.07 * height ) ) );
                    self.set( f"{ name }", itk.PhotoImage( image ) );
                else:
                    image = image.resize( ( floor( 0.08 * width ), floor( 0.22 * height ) ) );
                    self.set( name, itk.PhotoImage( image ) );
