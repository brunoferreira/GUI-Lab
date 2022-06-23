import tkinter as tk
import sqlite3 as sl
from participant import Participant
from register import register_run

class ParticipantApp():

    def __init__(self, master=None):
        self.font = ('Verdana', '10')

        self.containers = {}
        self.labels = {}
        self.inputs = {}

        self.containers['title'] = tk.Frame(master)
        self.containers['title'].pack()
        self.title = tk.Label(self.containers['title'], text = 'Participante')
        self.title['font'] = ('Calibri', '17', 'bold')
        self.title.pack()

        fields = ['name', 'username', 'password', 'email', 'address', 'phone_number']
        ui_fields = {
            'name': 'Nome',
            'username': 'Usuário',
            'password': 'Senha',
            'email': 'Email',
            'address': 'Endereço',
            'phone_number': 'Telefone'
        }
        for field in fields:
            self.containers[field] = tk.Frame(master)
            self.containers[field]['padx'] = 20
            self.containers[field]['pady'] = 5
            self.containers[field].pack()
            self.labels[field] = tk.Label(self.containers[field], text = ui_fields[field], font = self.font, width = 12)
            self.labels[field].pack(side=tk.LEFT)
            self.inputs[field] = tk.Entry(self.containers[field])
            self.inputs[field]['width'] = 28
            self.inputs[field]['font'] = self.font
            self.inputs[field].pack(side=tk.LEFT)

def run():
    con = sl.connect('app.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS participants (
                    id INTEGER PRIMARY KEY,
                    name text,
                    username text UNIQUE,
                    password text,
                    email text UNIQUE,
                    address text,
                    phone_number tex
                )''')
    con.close()

    register_run()

if __name__ == '__main__':
    run()