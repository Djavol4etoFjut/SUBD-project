import sys
import sqlite3

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

class Toplevel1:
    def __init__(self, top=None):

        self.conn = sqlite3.connect('subd.db')
        
        _bgcolor = '#d9d9d9' 
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 

        top.geometry("1321x738+428+152")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.create_entry = tk.Button(top,command=self.create_table)
        self.create_entry.place(relx=0.031, rely=0.027, height=24, width=47)
        self.create_entry.configure(activebackground="#ececec")
        self.create_entry.configure(activeforeground="#000000")
        self.create_entry.configure(background="#d9d9d9")
        self.create_entry.configure(disabledforeground="#a3a3a3")
        self.create_entry.configure(foreground="#000000")
        self.create_entry.configure(highlightbackground="#d9d9d9")
        self.create_entry.configure(highlightcolor="black")
        self.create_entry.configure(pady="0")
        self.create_entry.configure(text='''Button''')

        self.create_label = tk.Label(top)
        self.create_label.place(relx=0.083, rely=0.027, height=21, width=34)
        self.create_label.configure(activebackground="#f9f9f9")
        self.create_label.configure(activeforeground="black")
        self.create_label.configure(background="#d9d9d9")
        self.create_label.configure(disabledforeground="#a3a3a3")
        self.create_label.configure(foreground="#000000")
        self.create_label.configure(highlightbackground="#d9d9d9")
        self.create_label.configure(highlightcolor="black")
        self.create_label.configure(text='create DB')

        self.size_entry = tk.Entry(top)
        self.size_entry.place(relx=0.015, rely=0.176,height=20, relwidth=0.064)
        self.size_entry.configure(background="white")
        self.size_entry.configure(disabledforeground="#a3a3a3")
        self.size_entry.configure(font="TkFixedFont")
        self.size_entry.configure(foreground="#000000")
        self.size_entry.configure(highlightbackground="#d9d9d9")
        self.size_entry.configure(highlightcolor="black")
        self.size_entry.configure(insertbackground="black")
        self.size_entry.configure(selectbackground="#c4c4c4")
        self.size_entry.configure(selectforeground="black")

        self.lat_entry = tk.Entry(top)
        self.lat_entry.place(relx=0.015, rely=0.217,height=20, relwidth=0.064)
        self.lat_entry.configure(background="white")
        self.lat_entry.configure(disabledforeground="#a3a3a3")
        self.lat_entry.configure(font="TkFixedFont")
        self.lat_entry.configure(foreground="#000000")
        self.lat_entry.configure(highlightbackground="#d9d9d9")
        self.lat_entry.configure(highlightcolor="black")
        self.lat_entry.configure(insertbackground="black")
        self.lat_entry.configure(selectbackground="#c4c4c4")
        self.lat_entry.configure(selectforeground="black")

        self.len_entry = tk.Entry(top)
        self.len_entry.place(relx=0.015, rely=0.257,height=20, relwidth=0.064)
        self.len_entry.configure(background="white")
        self.len_entry.configure(disabledforeground="#a3a3a3")
        self.len_entry.configure(font="TkFixedFont")
        self.len_entry.configure(foreground="#000000")
        self.len_entry.configure(highlightbackground="#d9d9d9")
        self.len_entry.configure(highlightcolor="black")
        self.len_entry.configure(insertbackground="black")
        self.len_entry.configure(selectbackground="#c4c4c4")
        self.len_entry.configure(selectforeground="black")

        self.country_entry = tk.Entry(top)
        self.country_entry.place(relx=0.015, rely=0.298,height=20, relwidth=0.064)
        self.country_entry.configure(background="white")
        self.country_entry.configure(disabledforeground="#a3a3a3")
        self.country_entry.configure(font="TkFixedFont")
        self.country_entry.configure(foreground="#000000")
        self.country_entry.configure(highlightbackground="#d9d9d9")
        self.country_entry.configure(highlightcolor="black")
        self.country_entry.configure(insertbackground="black")
        self.country_entry.configure(selectbackground="#c4c4c4")
        self.country_entry.configure(selectforeground="black")

        self.forest_type_entry = tk.Entry(top)
        self.forest_type_entry.place(relx=0.015, rely=0.339,height=20, relwidth=0.064)
        self.forest_type_entry.configure(background="white")
        self.forest_type_entry.configure(disabledforeground="#a3a3a3")
        self.forest_type_entry.configure(font="TkFixedFont")
        self.forest_type_entry.configure(foreground="#000000")
        self.forest_type_entry.configure(highlightbackground="#d9d9d9")
        self.forest_type_entry.configure(highlightcolor="black")
        self.forest_type_entry.configure(insertbackground="black")
        self.forest_type_entry.configure(selectbackground="#c4c4c4")
        self.forest_type_entry.configure(selectforeground="black")

        self.size = tk.Label(top)
        self.size.place(relx=0.098, rely=0.176, height=21, width=35)
        self.size.configure(activebackground="#f9f9f9")
        self.size.configure(activeforeground="black")
        self.size.configure(background="#d9d9d9")
        self.size.configure(disabledforeground="#a3a3a3")
        self.size.configure(foreground="#000000")
        self.size.configure(highlightbackground="#d9d9d9")
        self.size.configure(highlightcolor="black")
        self.size.configure(text='size')

        self.lat = tk.Label(top)
        self.lat.place(relx=0.098, rely=0.217, height=20, width=35)
        self.lat.configure(activebackground="#f9f9f9")
        self.lat.configure(activeforeground="black")
        self.lat.configure(background="#d9d9d9")
        self.lat.configure(disabledforeground="#a3a3a3")
        self.lat.configure(foreground="#000000")
        self.lat.configure(highlightbackground="#d9d9d9")
        self.lat.configure(highlightcolor="black")
        self.lat.configure(text='lat')

        self.len = tk.Label(top)
        self.len.place(relx=0.098, rely=0.298, height=21, width=35)
        self.len.configure(activebackground="#f9f9f9")
        self.len.configure(activeforeground="black")
        self.len.configure(background="#d9d9d9")
        self.len.configure(disabledforeground="#a3a3a3")
        self.len.configure(foreground="#000000")
        self.len.configure(highlightbackground="#d9d9d9")
        self.len.configure(highlightcolor="black")
        self.len.configure(text='len')

        self.country = tk.Label(top)
        self.country.place(relx=0.098, rely=0.257, height=20, width=35)
        self.country.configure(activebackground="#f9f9f9")
        self.country.configure(activeforeground="black")
        self.country.configure(background="#d9d9d9")
        self.country.configure(disabledforeground="#a3a3a3")
        self.country.configure(foreground="#000000")
        self.country.configure(highlightbackground="#d9d9d9")
        self.country.configure(highlightcolor="black")
        self.country.configure(text='country')

        self.forest_type = tk.Label(top)
        self.forest_type.place(relx=0.098, rely=0.339, height=21, width=35)
        self.forest_type.configure(activebackground="#f9f9f9")
        self.forest_type.configure(activeforeground="black")
        self.forest_type.configure(background="#d9d9d9")
        self.forest_type.configure(disabledforeground="#a3a3a3")
        self.forest_type.configure(foreground="#000000")
        self.forest_type.configure(highlightbackground="#d9d9d9")
        self.forest_type.configure(highlightcolor="black")
        self.forest_type.configure(text='type')

        self.type_entry = tk.Entry(top)
        self.type_entry.place(relx=0.265, rely=0.176,height=20, relwidth=0.064)
        self.type_entry.configure(background="white")
        self.type_entry.configure(disabledforeground="#a3a3a3")
        self.type_entry.configure(font="TkFixedFont")
        self.type_entry.configure(foreground="#000000")
        self.type_entry.configure(highlightbackground="#d9d9d9")
        self.type_entry.configure(highlightcolor="black")
        self.type_entry.configure(insertbackground="black")
        self.type_entry.configure(selectbackground="#c4c4c4")
        self.type_entry.configure(selectforeground="black")

        self.nat_entry = tk.Entry(top)
        self.nat_entry.place(relx=0.265, rely=0.217,height=20, relwidth=0.064)
        self.nat_entry.configure(background="white")
        self.nat_entry.configure(disabledforeground="#a3a3a3")
        self.nat_entry.configure(font="TkFixedFont")
        self.nat_entry.configure(foreground="#000000")
        self.nat_entry.configure(highlightbackground="#d9d9d9")
        self.nat_entry.configure(highlightcolor="black")
        self.nat_entry.configure(insertbackground="black")
        self.nat_entry.configure(selectbackground="#c4c4c4")
        self.nat_entry.configure(selectforeground="black")

        self.con_entry = tk.Entry(top)
        self.con_entry.place(relx=0.265, rely=0.257,height=20, relwidth=0.064)
        self.con_entry.configure(background="white")
        self.con_entry.configure(disabledforeground="#a3a3a3")
        self.con_entry.configure(font="TkFixedFont")
        self.con_entry.configure(foreground="#000000")
        self.con_entry.configure(highlightbackground="#d9d9d9")
        self.con_entry.configure(insertbackground="black")
        self.con_entry.configure(selectbackground="#c4c4c4")
        self.con_entry.configure(selectforeground="black")

        self.type_text = tk.Label(top)
        self.type_text.place(relx=0.341, rely=0.176, height=21, width=34)
        self.type_text.configure(activebackground="#f9f9f9")
        self.type_text.configure(activeforeground="black")
        self.type_text.configure(background="#d9d9d9")
        self.type_text.configure(disabledforeground="#a3a3a3")
        self.type_text.configure(foreground="#000000")
        self.type_text.configure(highlightbackground="#d9d9d9")
        self.type_text.configure(highlightcolor="black")
        self.type_text.configure(text='type')

        self.natural_text = tk.Label(top)
        self.natural_text.place(relx=0.341, rely=0.217, height=21, width=35)
        self.natural_text.configure(activebackground="#f9f9f9")
        self.natural_text.configure(activeforeground="black")
        self.natural_text.configure(background="#d9d9d9")
        self.natural_text.configure(disabledforeground="#a3a3a3")
        self.natural_text.configure(foreground="#000000")
        self.natural_text.configure(highlightbackground="#d9d9d9")
        self.natural_text.configure(highlightcolor="black")
        self.natural_text.configure(text='nat')

        self.conserved_text = tk.Label(top)
        self.conserved_text.place(relx=0.341, rely=0.257, height=20, width=35)
        self.conserved_text.configure(activebackground="#f9f9f9")
        self.conserved_text.configure(activeforeground="black")
        self.conserved_text.configure(background="#d9d9d9")
        self.conserved_text.configure(disabledforeground="#a3a3a3")
        self.conserved_text.configure(foreground="#000000")
        self.conserved_text.configure(highlightbackground="#d9d9d9")
        self.conserved_text.configure(highlightcolor="black")
        self.conserved_text.configure(text='con')

        self.entry_lat2 = tk.Entry(top)
        self.entry_lat2.place(relx=0.56, rely=0.176,height=20, relwidth=0.064)
        self.entry_lat2.configure(background="white")
        self.entry_lat2.configure(disabledforeground="#a3a3a3")
        self.entry_lat2.configure(font="TkFixedFont")
        self.entry_lat2.configure(foreground="#000000")
        self.entry_lat2.configure(highlightbackground="#d9d9d9")
        self.entry_lat2.configure(highlightcolor="black")
        self.entry_lat2.configure(insertbackground="black")
        self.entry_lat2.configure(selectbackground="#c4c4c4")
        self.entry_lat2.configure(selectforeground="black")

        self.enry_len2 = tk.Entry(top)
        self.enry_len2.place(relx=0.56, rely=0.217,height=20, relwidth=0.064)
        self.enry_len2.configure(background="white")
        self.enry_len2.configure(disabledforeground="#a3a3a3")
        self.enry_len2.configure(font="TkFixedFont")
        self.enry_len2.configure(foreground="#000000")
        self.enry_len2.configure(highlightbackground="#d9d9d9")
        self.enry_len2.configure(highlightcolor="black")
        self.enry_len2.configure(insertbackground="black")
        self.enry_len2.configure(selectbackground="#c4c4c4")
        self.enry_len2.configure(selectforeground="black")

        self.entry_widget_lat2 = tk.Label(top)
        self.entry_widget_lat2.place(relx=0.643, rely=0.176, height=21, width=35)
        self.entry_widget_lat2.configure(activebackground="#f9f9f9")
        self.entry_widget_lat2.configure(activeforeground="black")
        self.entry_widget_lat2.configure(background="#d9d9d9")
        self.entry_widget_lat2.configure(disabledforeground="#a3a3a3")
        self.entry_widget_lat2.configure(foreground="#000000")
        self.entry_widget_lat2.configure(highlightbackground="#d9d9d9")
        self.entry_widget_lat2.configure(highlightcolor="black")
        self.entry_widget_lat2.configure(text='Lat')

        self.entry_widget_len2 = tk.Label(top)
        self.entry_widget_len2.place(relx=0.643, rely=0.217, height=21, width=35)
        self.entry_widget_len2.configure(activebackground="#f9f9f9")
        self.entry_widget_len2.configure(activeforeground="black")
        self.entry_widget_len2.configure(background="#d9d9d9")
        self.entry_widget_len2.configure(disabledforeground="#a3a3a3")
        self.entry_widget_len2.configure(highlightbackground="#d9d9d9")
        self.entry_widget_len2.configure(highlightcolor="black")
        self.entry_widget_len2.configure(text='Len')

        self.add_forest_button = tk.Button(top)
        self.add_forest_button.place(relx=0.023, rely=0.393, height=44, width=227)
        self.add_forest_button.configure(activebackground="#ececec")
        self.add_forest_button.configure(activeforeground="#000000")
        self.add_forest_button.configure(background="#d9d9d9")
        self.add_forest_button.configure(disabledforeground="#a3a3a3")
        self.add_forest_button.configure(foreground="#000000")
        self.add_forest_button.configure(highlightbackground="#d9d9d9")
        self.add_forest_button.configure(highlightcolor="black")
        self.add_forest_button.configure(pady="0")
        self.add_forest_button.configure(text='add')

        self.add_forest_type_button = tk.Button(top)
        self.add_forest_type_button.place(relx=0.265, rely=0.393, height=44, width=317)
        self.add_forest_type_button.configure(activebackground="#ececec")
        self.add_forest_type_button.configure(activeforeground="#000000")
        self.add_forest_type_button.configure(background="#d9d9d9")
        self.add_forest_type_button.configure(disabledforeground="#a3a3a3")
        self.add_forest_type_button.configure(foreground="#000000")
        self.add_forest_type_button.configure(highlightbackground="#d9d9d9")
        self.add_forest_type_button.configure(highlightcolor="black")
        self.add_forest_type_button.configure(pady="0")
        self.add_forest_type_button.configure(text='add')

        self.delete_forest_button = tk.Button(top)
        self.delete_forest_button.place(relx=0.56, rely=0.393, height=44, width=297)
        self.delete_forest_button.configure(activebackground="#ececec")
        self.delete_forest_button.configure(activeforeground="#000000")
        self.delete_forest_button.configure(background="#d9d9d9")
        self.delete_forest_button.configure(disabledforeground="#a3a3a3")
        self.delete_forest_button.configure(foreground="#000000")
        self.delete_forest_button.configure(highlightbackground="#d9d9d9")
        self.delete_forest_button.configure(highlightcolor="black")
        self.delete_forest_button.configure(pady="0")
        self.delete_forest_button.configure(text='delete')

        self.print_while_DB_button = tk.Button(top)
        self.print_while_DB_button.place(relx=0.03, rely=0.542, height=44, width=117)
        self.print_while_DB_button.configure(activebackground="#ececec")
        self.print_while_DB_button.configure(activeforeground="#000000")
        self.print_while_DB_button.configure(background="#d9d9d9")
        self.print_while_DB_button.configure(disabledforeground="#a3a3a3")
        self.print_while_DB_button.configure(foreground="#000000")
        self.print_while_DB_button.configure(highlightbackground="#d9d9d9")
        self.print_while_DB_button.configure(highlightcolor="black")
        self.print_while_DB_button.configure(pady="0")
        self.print_while_DB_button.configure(text='print whole DB')

        self.print_forests_button = tk.Button(top)
        self.print_forests_button.place(relx=0.151, rely=0.542, height=44, width=117)
        self.print_forests_button.configure(activebackground="#ececec")
        self.print_forests_button.configure(activeforeground="#000000")
        self.print_forests_button.configure(background="#d9d9d9")
        self.print_forests_button.configure(disabledforeground="#a3a3a3")
        self.print_forests_button.configure(foreground="#000000")
        self.print_forests_button.configure(highlightbackground="#d9d9d9")
        self.print_forests_button.configure(highlightcolor="black")
        self.print_forests_button.configure(pady="0")
        self.print_forests_button.configure(text='print forests')

        self.print_forest_types_button = tk.Button(top)
        self.print_forest_types_button.place(relx=0.273, rely=0.542, height=44, width=127)
        self.print_forest_types_button.configure(activebackground="#ececec")
        self.print_forest_types_button.configure(activeforeground="#000000")
        self.print_forest_types_button.configure(background="#d9d9d9")
        self.print_forest_types_button.configure(disabledforeground="#a3a3a3")
        self.print_forest_types_button.configure(foreground="#000000")
        self.print_forest_types_button.configure(highlightbackground="#d9d9d9")
        self.print_forest_types_button.configure(highlightcolor="black")
        self.print_forest_types_button.configure(pady="0")
        self.print_forest_types_button.configure(text='print forest types')

        self.print_countries_button = tk.Button(top)
        self.print_countries_button.place(relx=0.401, rely=0.542, height=44, width=117)
        self.print_countries_button.configure(activebackground="#ececec")
        self.print_countries_button.configure(activeforeground="#000000")
        self.print_countries_button.configure(background="#d9d9d9")
        self.print_countries_button.configure(disabledforeground="#a3a3a3")
        self.print_countries_button.configure(foreground="#000000")
        self.print_countries_button.configure(highlightbackground="#d9d9d9")
        self.print_countries_button.configure(highlightcolor="black")
        self.print_countries_button.configure(pady="0")
        self.print_countries_button.configure(text='print countries')

        self.add_forest_message = tk.Message(top)
        self.add_forest_message.place(relx=0.015, rely=0.095, relheight=0.058
                , relwidth=0.12)
        self.add_forest_message.configure(background="#d9d9d9")
        self.add_forest_message.configure(foreground="#000000")
        self.add_forest_message.configure(highlightbackground="#d9d9d9")
        self.add_forest_message.configure(highlightcolor="black")
        self.add_forest_message.configure(text='Add forest')
        self.add_forest_message.configure(width=159)

        self.forest_type_message = tk.Message(top)
        self.forest_type_message.place(relx=0.25, rely=0.095, relheight=0.058
                , relwidth=0.151)
        self.forest_type_message.configure(background="#d9d9d9")
        self.forest_type_message.configure(foreground="#000000")
        self.forest_type_message.configure(highlightbackground="#d9d9d9")
        self.forest_type_message.configure(highlightcolor="black")
        self.forest_type_message.configure(text='Create forest type in forest type table')
        self.forest_type_message.configure(width=200)

        self.delete_forest_message = tk.Message(top)
        self.delete_forest_message.place(relx=0.545, rely=0.068, relheight=0.085, relwidth=0.174)
        self.delete_forest_message.configure(background="#d9d9d9")
        self.delete_forest_message.configure(foreground="#000000")
        self.delete_forest_message.configure(highlightbackground="#d9d9d9")
        self.delete_forest_message.configure(highlightcolor="black")
        self.delete_forest_message.configure(text='Delete forest by cordinates')
        self.delete_forest_message.configure(width=230)

        self.print_DB_message = tk.Message(top)
        self.print_DB_message.place(relx=0.023, rely=0.637, relheight=0.248, relwidth=0.463)
        self.print_DB_message.configure(background="#d9d9d9")
        self.print_DB_message.configure(foreground="#000000")
        self.print_DB_message.configure(highlightbackground="#d9d9d9")
        self.print_DB_message.configure(highlightcolor="black")
        self.print_DB_message.configure(text='''PRINT DATABASE''')
        self.print_DB_message.configure(width=610)

    def create_table(self):
        table_forest = """ CREATE TABLE forests(
                                        forest_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        len REAL NOT NULL,
                                        lat REAL NOT NULL,
                                        country_name TEXT,
                                        forest_type_id INTEGER,
                                        FOREIGN KEY(forest_type_id) REFERENCES forest_types(ID),
                                        FOREIGN KEY(country_name) REFERENCES countries(name)
                                    ); """

        table_forest_types = """ CREATE TABLE forest_types(
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                type TEXT,
                                natural BOOLEAN,
                                conserved BOOLEAN
                            ); """
        table_countries = """ CREATE TABLE countries(
                            name TEXT PRIMARY KEY UNIQUE NOT NULL,
                            climate TEXT
                            );"""
        
        c = self.conn.cursor()
        c.execute(table_forest_types)
        c.execute(table_countries)
        c.execute(table_forest)
    

if __name__ == '__main__':
    vp_start_gui()





