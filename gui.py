import tkinter as tk
from tkinter import ttk
from datetime import date

import database

def start():
    root = tk.Tk()
    root.title('Jízdenky')
    root.geometry('500x800')
    root.configure(background='white')

    # Vzhled

    gui_style = ttk.Style()
    gui_style.configure('My.TButton', background='slate gray', font=('Arial', 14))
    gui_style.configure('My.TFrame', background='light blue')
    gui_style.configure('My.TLabel', background='light blue')

    home = ttk.Frame(root, padding=10, style='My.TFrame')
    home.pack(fill='both', expand=True)

    # Tlačítka přidání jízdenek

    ttk.Label(
        home,
        style='My.TLabel',
        text='Přidat jízdenku:',
        font=('Arial', 16, 'bold')
    ).pack(pady=(20, 15))

    buttons = ttk.Frame(home, style='My.TFrame')
    buttons.pack()

    ttk.Button(
        buttons,
        text='Přidat časovou jízdenku',
        style='My.TButton',
        width=25,
        command=lambda: pridat_casovou(root)
    ).pack(side='bottom', padx=5, pady=5)

    ttk.Button(
        buttons,
        text='Přidat jednorázovou jízdenku',
        width=25,
        style='My.TButton',
        command=lambda: pridat_jednorazovou(root)
    ).pack(side='top', padx=5, pady=5)

    # Tabulka s jízdenkami

    ttk.Label(
        home,
        style='My.TLabel',
        text='Jízdenky',
        font=('Arial', 20, 'bold')
    ).pack(pady=(40, 25))

    seznam = ttk.Treeview(
        home,
        columns=('typ', 'informace'),
        show='headings'
    )

    seznam.heading('typ', text='Typ')
    seznam.heading('informace', text='Informace')

    seznam.pack(fill='both', expand=True, side='bottom')

    root.mainloop()

def pridat_jednorazovou(parent):
    parent.withdraw()

    # Vzhled

    okno = tk.Toplevel(parent)
    okno.title('Přidat jednorázovou jízdenku')
    okno.geometry('500x800')
    okno.configure(background='white')

    gui_style = ttk.Style()
    gui_style.configure('Ticket.TButton', background='slate gray', font=('Arial', 14))
    gui_style.configure('Ticket.TFrame', background='light blue')
    gui_style.configure('Ticket.TLabel', background='light blue')

    frame = ttk.Frame(
        okno,
        padding=20,
        style='Ticket.TFrame'
    )
    frame.pack(fill='both', expand=True)

    ttk.Label(
        frame,
        text='Přidat jednorázovou jízdenku',
        style='Ticket.TLabel',
        font=('Arial', 18, 'bold')
    ).pack(pady=(10, 25))

    # Zadání informací

    # Potvrzení/zrušení

    buttons = ttk.Frame(frame, style='Ticket.TFrame')
    buttons.pack(fill='x', pady=(25, 0))

    def zrusit():
        okno.destroy()
        parent.deiconify()

    ttk.Button(
        buttons,
        style='Ticket.TButton',
        text='Zrušit',
        command=zrusit
    ).pack(side='left', padx=5)

    ttk.Button(
        buttons,
        style='Ticket.TButton',
        text='Uložit'
    ).pack(side='right', padx=5)

def pridat_casovou(parent):
    pass

if __name__ == '__main__':
    start()