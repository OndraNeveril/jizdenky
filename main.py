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
gui_style.configure('Jizd.TButton', background='SlateGray4', font=('Arial', 14))
gui_style.configure('Jizd.TFrame', background='light blue')
gui_style.configure('Jizd.TLabel', background='light blue')
gui_style.configure('Vyhl.TButton', background='Green3', font=('Arial', 14))
gui_style.configure('Vyhl.TFrame', background='DarkOliveGreen3')
gui_style.configure('Vyhl.TLabel', background='DarkOliveGreen3')
gui_style.configure('lista_jizd.TButton', background='SlateGray4', font=('Arial', 14), foreground='white')
gui_style.configure('lista_vyhl.TButton', background='Green3', font=('Arial', 14), foreground='white')
gui_style.configure('lista.TFrame', background='aquamarine4')

obsah = ttk.Frame(root)
obsah.pack(fill='both', expand=True)

jizdenky = ttk.Frame(obsah, style='My.TFrame')
vyhledavani = ttk.Frame(obsah, style='My.TFrame')

gui_jizdenky.start(jizdenky)
gui_vyhledavac.start(vyhledavani)

lista = ttk.Frame(root, style='lista.TFrame')
lista.pack(side='bottom', fill='x')

ttk.Button(
    lista,
    text='Jízdenky',
    style='lista_jizd.TButton',
    width=20,
    command=lambda: zobrazit(jizdenky)
).pack(side='left', pady=20, expand=True)

ttk.Button(
    lista,
    text='Vyhledávač',
    style='lista_vyhl.TButton',
    width=20,
    command=lambda: zobrazit(vyhledavani)
).pack(side='right', pady=20, expand=True)

def zobrazit(ramec):
    jizdenky.pack_forget()
    vyhledavani.pack_forget()
    ramec.pack(fill='both', expand=True)

zobrazit(jizdenky)

root.mainloop()