from importlib.machinery import SourceFileLoader;
from structures.Tooltip import Tooltip;
from util.safeCast import safeCast;
from os import path, system, walk;
from tkinter import messagebox;
from tkinter import ttk;
from tkinter import *;
import util.Constants as Constants;

# Cargamos los módulos de programas.
programs = {};
files = walk( path.abspath( "programs" ) );
for ( root, dir, names ) in files:
    for name in names:
        if ( name[-3:] != ".py" ): continue;
        module = SourceFileLoader( name[:-3], f"programs/{ name }" ).load_module();
        classModule = module.Program();
        programs[ classModule.name ] = classModule;

# Actualiza los valores del combobox de programas.
def setValues( event ):
    values = loadValues();
    program_combo[ "values" ] = values;
    if ( program_combo[ "values" ] ): return program_combo.current( 0 );
    return program_combo.set( '' );

# Carga de valores del combobox de programas.
def loadValues():
    values = [];
    ModuleTypes = {
      "Pilas":        Constants.Module_Pilas,
      "Recursividad": Constants.Module_Recursividad,
      "Colas":        Constants.Module_Colas,
      "Listas":       Constants.Module_Listas,
      "Arboles":      Constants.Module_Arboles,
      "Grafos":       Constants.Module_Grafos
    };
    for program in programs.values():
        if ( program.module != ModuleTypes[ module_combo.get() ] ): continue;
        values.append( program.name );
    return values;

# Ejecutar un programa.
def runProgram():
    if ( not program_combo.get() ): return messagebox.showerror( message = "¡Selecciona un programa!", title = "¡Error!" );
    for widget in program_frame.winfo_children(): widget.destroy();
    programs[ program_combo.get() ].execute( program_frame );

# Ventana.
window = Tk();
window.config( width = 650, height = 325 );
window.title( "Menú de prácticas - Estructura de Datos" );
window.iconphoto( False, PhotoImage( file = "assets\\logo.png" ) );
window.resizable( False, False );

# Frame Principal.
main_frame = Frame( width = 225, height = 325, bg = "#ffffff" );
main_frame.place( x = 0, y = 0 );
program_frame = Frame( width = 425, height = 325, bg = "#f0f0f0" );
program_frame.place( x = 225, y = 0 );

# Labels de texto.
Label( main_frame, bg = "#ffffff", text = "Este menú le permitirá ejecutar\ncualquier programa práctico de\nla materia de Estructura de Datos." ).place( x = 25, y = 25 );
Label( main_frame, bg = "#ffffff", text = "Seleccione un módulo:" ).place( x = 25, y = 110 );
Label( main_frame, bg = "#ffffff", text = "Seleccione un programa:" ).place( x = 25, y = 180 );
Label( program_frame, text = "Desarrollado por\nOscar Daniel López Cerino" ).place( relx = 0.5, rely = 0.65, anchor = CENTER );

# Logotipo de la universidad.
ujat_img = PhotoImage( file = "assets\\ujat.png" );
ujat_lbl = Label( program_frame, image = ujat_img );
ujat_lbl.image = ujat_img;
ujat_lbl.place( relx = 0.5, rely = 0.4, anchor = CENTER );


# ComboBoxes
modules = [ "Pilas", "Recursividad", "Colas" ];
module_combo = ttk.Combobox( state = "readonly", values = modules );
module_combo.place( x = 25, y = 135 );
module_combo.current( 0 );
module_combo.bind( "<<ComboboxSelected>>", setValues );
program_combo = ttk.Combobox( state = "readonly", values = loadValues() );
program_combo.place( x = 25, y = 205 );
program_combo.current( 0 );

# Imagen de información.
info_img = PhotoImage( file = "assets\\info.png" );

# Botón de ejecución.
Button( main_frame, text = "Ejecutar", command = runProgram, width = 23, height = 3 ).place( x = 25, y = 250 );
info_btn = Button( program_frame, highlightthickness = 0, bd = 0, image = info_img );
info_btn.image = info_img; # Referencia para evitar el GarbageCollector
info_btn.place( x = 5, y = 5 );

# Tooltips
Tooltip( info_btn, "Desarrollado para la materia de Estructura de Datos en el ciclo escolar 2022-B." );

# Ciclo de vida de la ventana.
window.mainloop();
