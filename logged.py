import tkinter as tk
import sqlite3 as sl
from participant import Participant
import tkinter.messagebox

def delete_account(logged_data, ws):
    msg = Participant.delete(logged_data)
    ws.destroy()
    from delete_success import delete_success_run
    delete_success_run()


def update_account(logged_data, ws, name, username, email, password, address, phone_number):
    msg = Participant.update(logged_data, name.get(), username.get(), password.get(), email.get(), address.get(), phone_number.get())
    if isinstance(msg, str):
        tk.messagebox.showerror('', msg)
    else:
        ws.destroy()
        from update_success import update_success_run
        update_success_run()

def submit(logged_data, ws, name, username, email, password, address, phone_number):

    check = name.get() or username.get() or email.get() or password.get() or address.get() or phone_number.get()

    if check:
        update_account(logged_data, ws, name, username, email, password, address, phone_number)
    else:
        tk.messagebox.showerror('', 'Nenhum dado para atualizar')

def logged_run(logged_data):

    ws = tk.Tk()
    ws.title('Participante - Página do usuário')
    ws.geometry('800x600')
    ws.config(bg="#ffffd7")

    u = logged_data['username']

    # tk.Frames
    frame = tk.Frame(ws, padx=20, pady=20)
    frame.pack(expand=True)

    # tk.Labels
    tk.Label(
        frame, 
        text="Atualizar dados",
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
        text='Senha', 
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
    delete_button = tk.Button(
        frame, 
        text="Deletar conta", 
        padx=20, pady=10, 
        relief=tk.RAISED, 
        font=("Times", "14", "bold"), 
        command=lambda: delete_account(logged_data, ws)
        )

    delete_button.grid(row=7, columnspan=3, pady=10, sticky='w', padx=0)

    # tk.Button 
    update_button = tk.Button(frame, text="Atualizar", padx=0, pady=10, relief=tk.RAISED, font=("Times", "14", "bold"),
        command=lambda: submit(logged_data, ws, name, username, email, password, address, phone_number))
    update_button.grid(row=7, columnspan=3, pady=10, sticky='e', padx=0)

    ws.mainloop()