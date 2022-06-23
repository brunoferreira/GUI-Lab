import tkinter as tk
import sqlite3 as sl
from participant import Participant
import tkinter.messagebox
from register_success import register_success_run
 
def loginInstead(ws):
    ws.destroy()
    from login import login_run
    login_run()


def register(ws, name, username, email, password, address, phone_number):
    msg = Participant.register(name.get(), username.get(), password.get(), email.get(), address.get(), phone_number.get())
    if isinstance(msg, str):
        tk.messagebox.showerror('', msg)
    else:
        ws.destroy()
        register_success_run()

def submit(ws, name, username, email, password, address, phone_number):

    name_check = name.get()
    username_check = username.get()
    email_check = email.get()
    password_check = password.get()
    address_check = address.get()
    phone_number_check = phone_number.get()
    
    check_count = 0

    if phone_number_check == "":
        warn = "Telefone não pode ser vazio"
    else:
        check_count += 1
    if address_check == "":
        warn = "Endereço não pode ser vazio"
    else:
        check_count += 1
    if password_check == "":
        warn = "Senha não pode ser vazia"
    else:
        check_count += 1
    if email_check == "":
        warn = "Email não pode ser vazio"
    else:
        check_count += 1
    if username_check == "":
        warn = "Usuário não pode ser vazio"
    else:
        check_count += 1
    if name_check == "":
        warn = "Nome não pode ser vazio"
    else:
        check_count += 1

    if check_count == 6:
        register(ws, name, username, email, password, address, phone_number)
    else:
        tk.messagebox.showerror('', warn)

def register_run():

    ws = tk.Tk()
    ws.title('Participante - Cadastro')
    ws.geometry('800x600')
    ws.config(bg="#ffffd7")

    # tk.Frames
    frame = tk.Frame(ws, padx=20, pady=20)
    frame.pack(expand=True)

    # tk.Labels
    tk.Label(
        frame, 
        text="Cadastrar nova conta",
        font=("Times", "24", "bold")
        ).grid(row=0, columnspan=3, pady=10)

    tk.Label(
        frame, 
        text='Nome', 
        font=("Times", "14")
        ).grid(row=1, column=0, pady=5)

    tk.Label(
        frame, 
        text='Usuário', 
        font=("Times", "14")
        ).grid(row=2, column=0, pady=5)

    tk.Label(
        frame, 
        text='Email', 
        font=("Times", "14")
        ).grid(row=3, column=0, pady=5)

    tk.Label(
        frame, 
        text='Password', 
        font=("Times", "14")
        ).grid(row=4, column=0, pady=5)

    tk.Label(
        frame, 
        text='Endereço', 
        font=("Times", "14")
        ).grid(row=5, column=0, pady=5)

    tk.Label(
        frame, 
        text='Telefone', 
        font=("Times", "14")
        ).grid(row=6, column=0, pady=5)


    # tk.Entry
    name = tk.Entry(frame, width=30)
    username = tk.Entry(frame, width=30)
    email = tk.Entry(frame, width=30)
    password = tk.Entry(frame, width=30)
    address = tk.Entry(frame, width=30)
    phone_number = tk.Entry(frame, width=30)

    name.grid(row=1, column=1)
    username.grid(row=2, column=1)
    email.grid(row=3, column=1)
    password.grid(row=4, column=1)
    address.grid(row=5, column=1)
    phone_number.grid(row=6, column=1)

    # button 
    log = tk.Button(
        frame, 
        text="Fazer login", 
        padx=20, pady=10, 
        relief=tk.RAISED, 
        font=("Times", "14", "bold"), 
        command=lambda: loginInstead(ws)
        )

    log.grid(row=7, columnspan=3, pady=10, sticky='w', padx=14)

    # tk.Button 
    register_button = tk.Button(frame, text="Cadastrar", padx=0, pady=10, relief=tk.RAISED, font=("Times", "14", "bold"),
        command=lambda: submit(ws, name, username, email, password, address, phone_number))
    register_button.grid(row=7, columnspan=3, pady=10, sticky='e', padx=14)

    ws.mainloop()