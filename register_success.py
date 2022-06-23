import tkinter as tk
import sqlite3 as sl
from participant import Participant
from login import login_run

def login_window(ws):
    ws.destroy()
    login_run()

def register_success_run():

    ws = tk.Tk()
    ws.title('Participante - Cadastro efeutado')
    ws.geometry('800x600')
    ws.config(bg="#ffffd7")



    # tk.Frames
    frame = tk.Frame(ws, padx=20, pady=20)
    frame.pack(expand=True)

    # tk.Labels
    tk.Label(
        frame, 
        text="Cadastro efetuado com sucesso!",
        font=("Times", "24", "bold")
        ).grid(row=0, columnspan=3, pady=10)

    # tk.Button 
    login_button = tk.Button(frame, text="Fazer login", padx=0, pady=10, relief=tk.SOLID, font=("Times", "14", "bold"), command=lambda: login_window(ws))
    login_button.grid(row=7, columnspan=3, pady=20)

    ws.mainloop()