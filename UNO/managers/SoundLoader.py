from managers.Loader import Loader;
from pygame import mixer;
from os import walk;

class SoundLoader( Loader ):

    def __init__( self ):
        self.mixer = mixer;
        self.subfolder = "sounds";
        super( SoundLoader, self ).__init__( self.subfolder );
        self.load();
        self.mixer.music.play( -1 );

    def load( self ):
        files = None;
        self.mixer.init();
        directory = walk( self.directory );
        for ( root, dir, sounds ) in directory: files = sounds;
        for file in files:
            name = file[ :-4 ];
            if ( name == "background" ):
                self.mixer.music.load( f"{ self.directory }\\{ file }" );
                self.set( name, self.mixer.music );
            else:
                sound = self.mixer.Sound( f"{ self.directory }\\{ file }" );
                self.set( name, sound );

    def changeBackground( self, song ):
        self.mixer.fadeout( 2500 );
        self.mixer.music.load( f"{ self.directory }\\{ file }.mp3" );
        self.mixer.music.set_volume( 0.15 );
        self.mixer.music.play( -1 );
