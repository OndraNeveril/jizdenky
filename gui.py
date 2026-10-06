import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime
from tkcalendar import DateEntry

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

    # Tabulky s jízdenkami

    ttk.Label(
        home,
        style='My.TLabel',
        text='Jízdenky',
        font=('Arial', 20, 'bold')
    ).pack(pady=(40, 25))

    seznam = ttk.Treeview(
        home,
        columns=('dopravce', 'datum', 'vlak', 'kam'),
        show='headings'
    )

    seznam.column('dopravce', width=90, anchor='center', stretch=False)
    seznam.column('datum', width=160, stretch=False)
    seznam.column('vlak', width=90, anchor='center', stretch=False)
    seznam.column('kam', width=120, stretch=False)

    seznam.heading('dopravce', text='dopravce')
    seznam.heading('datum', text='datum')
    seznam.heading('vlak', text='vlak')
    seznam.heading('kam', text='cíl')

    for jizdenka in database.get_jednorazove():
        seznam.insert('','end', iid=str(jizdenka[0]),
            values=(
                jizdenka[1],
                f'{datetime.strptime(jizdenka[2], "%Y-%m-%d").strftime("%d. %m. %Y")}    {jizdenka[3]}',
                jizdenka[6], jizdenka[5]
            ))

    seznam.pack()

    ttk.Label(
        home,
        style='My.TLabel',
        text='Časové jízdenky',
        font=('Arial', 20, 'bold')
    ).pack(pady=(40, 25))

    seznam2 = ttk.Treeview(
        home,
        columns=('dopravce', 'zacatek', 'konec', 'zony'),
        show='headings'
    )

    seznam2.column('dopravce', width=75, anchor='center', stretch=False)
    seznam2.column('zacatek', width=150, stretch=False)
    seznam2.column('konec', width=150, stretch=False)
    seznam2.column('zony', width=100, stretch=False)

    seznam2.heading('dopravce', text='dopravce')
    seznam2.heading('zacatek', text='začátek')
    seznam2.heading('konec', text='konec')
    seznam2.heading('zony', text='zóny')

    for jizdenka in database.get_casove():
        seznam2.insert('', 'end', iid=str(jizdenka[0]), values=(
            jizdenka[1], f'{datetime.strptime(jizdenka[2], "%Y-%m-%d").strftime("%d. %m. %Y")}    {jizdenka[3]}', f'{datetime.strptime(jizdenka[4], "%Y-%m-%d").strftime("%d. %m. %Y")}    {jizdenka[5]}', jizdenka[6]))

    seznam2.pack()

    seznam.bind('<Double-1>', lambda event: upravit_jednorazovou(root, seznam))
    seznam2.bind('<Double-1>', lambda event: upravit_casovou(root, seznam2))

    seznam.bind('<Delete>', lambda event: smazat_jednorazovou(seznam))
    seznam2.bind('<Delete>', lambda event: smazat_casovou(seznam2))

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
    gui_style.configure('Ticket.TLabel', background='light blue', font=('Arial', 12))

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

    ttk.Label(
        frame,
        text='Dopravce:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    dopravce = ttk.Combobox(
        frame,
        values=['ČD', 'Regiojet', 'Leoexpres', 'Arriva', 'Jiný'],
        state='readonly'
    )
    dopravce.current(0)
    dopravce.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Datum:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    datum = DateEntry(
        frame,
        date_pattern='yyyy-mm-dd'
    )
    datum.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Čas odjezdu:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    cas_od = ttk.Entry(frame)
    cas_od.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Odkud:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    odkud = ttk.Entry(frame)
    odkud.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Kam:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    kam = ttk.Entry(frame)
    kam.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Vlak:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    vlak = ttk.Entry(frame)
    vlak.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Místo:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    misto = ttk.Entry(frame)
    misto.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Doklad:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    # Potvrzení/zrušení

    buttons = ttk.Frame(frame, style='Ticket.TFrame')
    buttons.pack(fill='x', pady=(25, 0))

    def zrusit():
        okno.destroy()
        parent.deiconify()

    def ulozit():
        if not all([
            dopravce.get(),
            datum.get(),
            cas_od.get(),
            odkud.get(),
            kam.get(),
            vlak.get()
        ]):
            return

        try:
            datetime.strptime(datum.get(), '%Y-%m-%d')
        except ValueError:
            return

        try:
            datetime.strptime(cas_od.get(), '%H:%M')
        except ValueError:
            return

        database.pridat_jednorazovou(
            dopravce.get(),
            datum.get(),
            cas_od.get(),
            odkud.get(),
            kam.get(),
            vlak.get(),
            misto.get() or None,
            None
        )

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
        text='Uložit',
        command=ulozit
    ).pack(side='right', padx=5)

def pridat_casovou(parent):
    parent.withdraw()

    # Vzhled

    okno = tk.Toplevel(parent)
    okno.title('Přidat jednorázovou jízdenku')
    okno.geometry('500x800')
    okno.configure(background='white')

    gui_style = ttk.Style()
    gui_style.configure('Ticket.TButton', background='slate gray', font=('Arial', 14))
    gui_style.configure('Ticket.TFrame', background='light blue')
    gui_style.configure('Ticket.TLabel', background='light blue', font=('Arial', 12))

    frame = ttk.Frame(
        okno,
        padding=20,
        style='Ticket.TFrame'
    )
    frame.pack(fill='both', expand=True)

    ttk.Label(
        frame,
        text='Přidat časovou jízdenku',
        style='Ticket.TLabel',
        font=('Arial', 18, 'bold')
    ).pack(pady=(10, 25))

    # Zadání informací

    ttk.Label(
        frame,
        text='Dopravce:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    dopravce = ttk.Combobox(
        frame,
        values=['PID'],
        state='readonly'
    )
    dopravce.current(0)
    dopravce.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Datum od:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    datum_od = DateEntry(
        frame,
        date_pattern='yyyy-mm-dd'
    )
    datum_od.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Čas od:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    cas_od = ttk.Entry(frame)
    cas_od.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Datum do:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    datum_do = DateEntry(
        frame,
        date_pattern='yyyy-mm-dd'
    )
    datum_do.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Čas do:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    cas_do = ttk.Entry(frame)
    cas_do.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Zóny:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    zony = ttk.Entry(frame)
    zony.pack(fill='x', pady=(2, 10))

    ttk.Label(
        frame,
        text='Doklad:',
        style='Ticket.TLabel'
    ).pack(anchor='w')

    # Potvrzení/zrušení

    buttons = ttk.Frame(frame, style='Ticket.TFrame')
    buttons.pack(fill='x', pady=(25, 0))

    def zrusit():
        okno.destroy()
        parent.deiconify()

    def ulozit():
        if not all([
            dopravce.get(),
            datum_od.get(),
            cas_od.get(),
            datum_do.get(),
            cas_do.get(),
        ]):
            return

        try:
            datetime.strptime(datum_od.get(), '%Y-%m-%d')
        except ValueError:
            return

        try:
            datetime.strptime(datum_do.get(), '%Y-%m-%d')
        except ValueError:
            return

        try:
            datetime.strptime(cas_od.get(), '%H:%M')
        except ValueError:
            return

        try:
            datetime.strptime(cas_do.get(), '%H:%M')
        except ValueError:
            return

        database.pridat_casovou(
            dopravce.get(),
            datum_od.get(),
            cas_od.get(),
            datum_do.get(),
            cas_do.get(),
            zony.get() or None,
            None
        )

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
        text='Uložit',
        command=ulozit
    ).pack(side='right', padx=5)

def upravit_jednorazovou(parent, seznam):
    vybrane = seznam.selection()

    if not vybrane:
        return

    id = int(vybrane[0])

    print(id)

def upravit_casovou(parent, seznam):
    vybrane = seznam.selection()

    if not vybrane:
        return

    id = int(vybrane[0])

    print(id)

def smazat_jednorazovou(seznam):
    vybrane = seznam.selection()

    if not vybrane:
        return

    id = int(vybrane[0])

    if not messagebox.askyesno(
        'Smazat jízdenku',
        'Opravdu chcete tuto jízdenku smazat?'
    ):
        return

    database.smazat_jednorazovou(id)
    seznam.delete(vybrane[0])

def smazat_casovou(seznam):
    vybrane = seznam.selection()

    if not vybrane:
        return

    id = int(vybrane[0])

    if not messagebox.askyesno(
        'Smazat jízdenku',
        'Opravdu chcete tuto jízdenku smazat?'
    ):
        return

    database.smazat_casovou(id)
    seznam.delete(vybrane[0])