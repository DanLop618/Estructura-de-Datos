from os import path;

class Loader:

    def __init__( self, subfolder ):
        abs = path.abspath( "assets" );
        self.directory = f"{ abs }\\{ subfolder }";
        self.data = {};

    def set( self, *entry ):
        key, value = entry;
        self.data[ key ] = value;

    def get( self, query ):
        return self.data.get( query, None );

    def delete( self, query ):
        data = self.data.get( query, None );
        del self.data[ query ];
        if ( data == None ): return False;
        return True;

    def __iter__( self ):
        self.__keys = list( self.data.keys() );
        self.__current = 0;
        return self;

    def __next__( self ):
        if ( self.__current < len( self.__keys ) ):
            key = self.__keys[ self.__current ];
            value = self.data[ key ];
            self.__current += 1;
            return [ key, value ];
        else:
            raise StopIteration;

    # def loadImages( self ):
    #     images = ImageManager();
    #     images.load();
    #     self.game.images = images;
    #
    # def loadSounds( self ):
    #     sounds = SoundManager();
    #     sounds.load();
    #     self.game.sounds = sounds;
    #
    # def loadEffects( self ):
    #     effects = EffectManager();
    #     effects.load();
    #     self.game.effects = effects;
