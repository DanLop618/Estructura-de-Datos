import tkinter as tk;

# Clase Tooltip
class Tooltip():

    """Crea un objeto Tooltip que muestra información extra cuando se hace un hover a un widget de Tkinter.
    @type widget: widget
    @param widget: El widget de Tkinter al que se anexará el Tooltip
    @type text: string
    @param text: El texto a mostrar
    @rtype: Tooltip
    @returns: El objeto Tooltip creado
    """
    def __init__( self, widget, text = "Some Text" ):
        self.waittime = 500;
        self.wraplength = 200;
        self.widget = widget;
        self.text = text;
        self.widget.bind( "<Enter>", self.enter );
        self.widget.bind( "<Leave>", self.leave );
        self.widget.bind( "<ButtonPress>", self.leave );
        self.id = None;
        self.tw = None;

    """Función de entrada al widget.
    @type event: event
    @param event: El evento recibido por parte del widget
    """
    def enter( self, event = None ): self.schedule();

    """Función de salida del widget.
    @type event: event
    @param event: El evento recibido por parte del widget
    """
    def leave( self, event = None ):
        self.unschedule();
        self.hidetip();

    """Programa el Tooltip para ser mostrado."""
    def schedule( self ):
        self.unschedule();
        self.id = self.widget.after( self.waittime, self.showtip );

    """Cancela la programación del Tooltip para ya no ser mostrado."""
    def unschedule( self ):
        id = self.id;
        self.id = None;
        if ( not id ): return;
        self.widget.after_cancel( id );

    """Muestra el Tooltip.
    @type event: event
    @param event: El evento recibido por parte del widget
    """
    def showtip( self, event = None ):
        x = y = 0;
        x, y, cx, cy = self.widget.bbox( "insert" );
        x += self.widget.winfo_rootx() + 25;
        y += self.widget.winfo_rooty() + 20;
        self.tw = tk.Toplevel( self.widget );
        self.tw.wm_overrideredirect( True );
        self.tw.wm_geometry( "+%d+%d" % (x, y) );
        label = tk.Label( self.tw, text = self.text, justify = "left", background = "#ffffff", relief = "solid", borderwidth = 1, wraplength = self.wraplength );
        label.pack( ipadx = 1 );

    """Esconde el Tooltip."""
    def hidetip( self ):
        tw = self.tw;
        self.tw = None;
        if ( not tw ): return;
        tw.destroy();
