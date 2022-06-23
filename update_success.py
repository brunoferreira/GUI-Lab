import tkinter as tk

def update_success_run():

    ws = tk.Tk()
    ws.title('Participante - Atualização concluída')
    ws.geometry('800x600')
    ws.config(bg="#ffffd7")

    # tk.Frames
    frame = tk.Frame(ws, padx=20, pady=20)
    frame.pack(expand=True)

    # tk.Labels
    tk.Label(
        frame, 
        text="Atualização efetuada com sucesso!",
        font=("Times", "24", "bold")
        ).grid(row=0, columnspan=3, pady=10)

    ws.mainloop()