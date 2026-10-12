import tkinter as tk
from tkinter import ttk
import database
import gui_jizdenky
import gui_vyhledavac

database.init_db()

root = tk.Tk()
root.title('Jízdenky')
root.geometry('500x900')

gui_style = ttk.Style()
gui_style.configure('My.TButton', background='slate gray', font=('Arial', 14))
gui_style.configure('My.TFrame', background='light blue')
gui_style.configure('My.TLabel', background='light blue')

obsah = ttk.Frame(root)
obsah.pack(fill='both', expand=True)

jizdenky = ttk.Frame(obsah, style='My.TFrame')
vyhledavani = ttk.Frame(obsah, style='My.TFrame')

gui_jizdenky.start(jizdenky)
gui_vyhledavac.start(vyhledavani)

lista = ttk.Frame(root, style='My.TFrame')
lista.pack(side='bottom', fill='x')

ttk.Button(
    lista,
    text='Jízdenky',
    style='My.TButton',
    width=20,
    command=lambda: zobrazit(jizdenky)
).pack(side='left', padx=5, pady=5, expand=True)

ttk.Button(
    lista,
    text='Vyhledávač',
    style='My.TButton',
    width=20,
    command=lambda: zobrazit(vyhledavani)
).pack(side='right', padx=5, pady=5, expand=True)

def zobrazit(ramec):
    jizdenky.pack_forget()
    vyhledavani.pack_forget()
    ramec.pack(fill='both', expand=True)

zobrazit(jizdenky)

root.mainloop()