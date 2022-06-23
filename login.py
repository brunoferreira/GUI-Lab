from cmath import e
import tkinter as tk
import sqlite3 as sl

from numpy import isin
from participant import Participant
import tkinter.messagebox
from logged import logged_run

def createAccount(ws):
    ws.destroy()
    from register import register_run
    register_run()

def submit(ws, uname, pwd):
    u = uname.get()
    p = pwd.get()
    check_counter=0
    if p == "":
        warn = "Senha não pode ser vazia"
    else:
        check_counter += 1
    if u == "":
       warn = "Usuário não pode ser vazio"
    else:
        check_counter += 1
    if check_counter == 2:
        users = Participant.get_participant_by_username(u)
        if len(users) == 0:
            tk.messagebox.showerror('', 'Usuário ou senha inválidos')
        else:
            if Participant.login(u, p):
                ws.destroy()
                logged_data = {'username': u, 'password': p}
                logged_run(logged_data)
            else:
                tk.messagebox.showerror('', 'Usuário ou senha inválidos')
    else:
        tk.messagebox.showerror('', warn)

def login_run(): 

    ws = tk.Tk()
    ws.title('Participante - Login')
    ws.geometry('800x600')
    ws.config(bg="#ffffd7")

    # frame
    frame = tk.Frame(ws, padx=20, pady=20)
    frame.pack_propagate(False)
    frame.pack(expand=True)


    # labels
    tk.Label(
        frame, 
        text="Login", 
        font=("Times", "24", "bold") 
        ).grid(row=0,  columnspan=3, pady=10) #..place(x=170, y=10)

    tk.Label(
        frame, 
        text='Usuário', 
        font=("Times", "14")
        ).grid(row=1, column=1, pady=5) #.place(x=50, y=70)

    tk.Label(
        frame, 
        text='Senha', 
        font=("Times", "14")
        ).grid(row=2, column=1, pady=5) #.place(x=50, y=110)

    # tk.Entry
    uname = tk.Entry(frame, width=20)
    pwd = tk.Entry(frame, width=20, show="*")
    # uname.place(x=220, y=70)
    # pwd.place(x=220, y=110)
    uname.grid(row=1, column=2)
    pwd.grid(row=2, column=2)

    # button 
    reg = tk.Button(
        frame, 
        text="Criar conta", 
        padx=20, pady=10, 
        relief=tk.RAISED, 
        font=("Times", "14", "bold"), 
        command=lambda: createAccount(ws)
        )

    sub = tk.Button(
        frame, 
        text="Login", 
        padx=20, 
        pady=10, 
        relief=tk.RAISED, 
        font=("Times", "14", "bold"), 
        command=lambda: submit(ws, uname, pwd)
        )

    reg.grid(row=3, column=1, pady=10)
    sub.grid(row=3, column=2, pady=10)

    ws.mainloop()