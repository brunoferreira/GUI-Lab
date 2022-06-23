import tkinter as tk
import sqlite3 as sl

class Participant():

    @classmethod
    def login(self, username, password):
        if len(Participant.get_participant_by_username(username)) == 0:
            return False
        user = Participant.get_participant_by_username(username)[0]
        return password == user['password']


    @classmethod
    def register(cls, name, username, password, email, address, phone_number):
        if len(Participant.get_participant_by_username(username)) > 0:
            return 'Usuário já existente'
        if len(Participant.get_participant_by_email(email)) > 0:
            return 'Email já cadastrado'

        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        columns = '(name, username, password, email, address, phone_number)'
        cur.execute("INSERT INTO {0}{1} VALUES (?, ?, ?, ?, ?, ?)".format(table, columns), (name, username, password, email, address, phone_number))
        con.commit()
        con.close()
        return True

    @classmethod
    def update(cls, logged_data, new_name, new_username, new_password, new_email, new_address, new_phone_number):
        if len(Participant.get_participant_by_username(new_username)) > 0:
            return 'Usuário já existente'
        if len(Participant.get_participant_by_email(new_email)) > 0:
            return 'Email já cadastrado'
        
        update_fields_str = ''
        update_fields = []
        aux = {
            'name': new_name,
            'username': new_username,
            'password': new_password,
            'email': new_email,
            'address': new_address,
            'phone_number': new_phone_number
        }
        for field, new_value in aux.items():
            if new_value != '':
                update_fields.append(new_value)
                update_fields_str += field + ' = ? , '
        update_fields_str = update_fields_str[:-3]
        update_fields.append(logged_data['username'])
        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        columns = '(name, username, password, email, address, phone_number)'
        cur.execute("UPDATE {0} SET {1} WHERE username = ?".format(table, update_fields_str), update_fields)
        con.commit()
        con.close()
        return True

    @classmethod
    def delete(cls, logged_data):

        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        columns = '(name, username, password, email, address, phone_number)'
        cur.execute("DELETE FROM {0} WHERE username = ?".format(table), (logged_data['username'], ))
        con.commit()
        con.close()
        return True

    @classmethod
    def deserialize(cls, serialized_data):
        participant = {}
        participant['id'] = serialized_data[0]
        participant['name'] = serialized_data[1]
        participant['username'] = serialized_data[2]
        participant['password'] = serialized_data[3]
        participant['email'] = serialized_data[4]
        participant['address'] = serialized_data[5]
        participant['phone_number'] = serialized_data[6]
        return participant

    @classmethod
    def get_participant_by_username(cls, username):
        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        cur.execute("SELECT * FROM {0} WHERE username=?".format(table), (username,))
        participants = cur.fetchall()
        con.close()
        if len(participants) > 0:
            return [cls.deserialize(participants[0])]
        return []

    @classmethod
    def get_participant_by_email(cls, email):
        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        cur.execute("SELECT * FROM {0} WHERE email=?".format(table), (email,))
        participants = cur.fetchall()
        con.close()
        if len(participants) > 0:
            return [cls.deserialize(participants[0])]
        return []

    @classmethod
    def get_all_participants(cls):
        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        cur.execute("SELECT * FROM {0}".format(table))
        participants = cur.fetchall()
        con.close()
        for i in range(len(participants)):
            participants[i] = cls.deserialize(participants[i])
        return participants

    @classmethod
    def delete_participant_by_username(cls, username):
        if len(Participant.get_participant_by_username(username)) == 0:
            print("Username doesn't exist")
            return False
        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        cur.execute("DELETE FROM {0} WHERE username=?".format(table), (username,))
        cur.commit()
        con.close()
        return True

    @classmethod
    def delete_participant_by_email(cls, email):
        if len(Participant.get_participant_by_email(email)) == 0:
            print("Email doesn't exist")
            return False
        con = sl.connect('app.db')
        cur = con.cursor()
        table = 'participants'
        cur.execute("DELETE FROM {0} WHERE email=?".format(table), (email,))
        participants = cur.fetchall()
        con.close()
        return True
