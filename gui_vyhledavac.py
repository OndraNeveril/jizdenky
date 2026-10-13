import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime
from tkcalendar import DateEntry

import database

def start(root):
    home = ttk.Frame(root, padding=10, style='Vyhl.TFrame')
    home.pack(fill='both', expand=True)

    # Tlačítka přidání jízdenek

    ttk.Label(
        home,
        style='Vyhl.TLabel',
        text='Vyhledávač spojení',
        font=('Arial', 16, 'bold')
    ).pack(pady=(20, 15))

    buttons = ttk.Frame(home, style='Vyhl.TFrame')
    buttons.pack()

    ttk.Button(
        buttons,
        text='Hledat',
        width=25,
        style='Vyhl.TButton',
    ).pack(side='top', padx=5, pady=5)

    # Tabulky s jízdenkami

    ttk.Label(
        home,
        style='Vyhl.TLabel',
        text='To be done soon',
        font=('Arial', 20, 'bold')
    ).pack(pady=(40, 25))