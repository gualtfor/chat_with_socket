import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
from dotenv import load_dotenv
from client import Client

load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
GREY = os.getenv('GREY')
MEDIUM_GREY = os.getenv('MEDIUM_GREY')
BLUE = os.getenv('BLUE')
WHITE = os.getenv(' WHITE')
FONT_FAMILY = os.getenv('FONT_FAMILY')
FONT_SIZE = os.getenv('FONT_SIZE')
BUTTON_SIZE = os.getenv('BUTTON_SIZE')
SMALL_FONT_SIZE = os.getenv('SMALL_FONT_SIZE')

class sandbox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Messenger Client")
        self.root.resizable(False, False)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=4)
        self.root.grid_rowconfigure(2, weight=1)
        
        self.client = Client()

        self.top_frame = tk.Frame(self.root, width=600, height=100, bg=GREY)
        self.top_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.middle_frame = tk.Frame(self.root, width=600, height=400, bg=MEDIUM_GREY)
        self.middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.bottom_frame = tk.Frame(self.root, width=600, height=100, bg=GREY)
        self.bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

        self.username_label = tk.Label(self.top_frame, text="Ingrese su usuario:", font=(FONT_FAMILY, FONT_SIZE), bg=GREY, fg=WHITE)
        self.username_label.pack(side=tk.LEFT, padx=10)

        self.username_textbox = tk.Entry(self.top_frame, font=(FONT_FAMILY, FONT_SIZE), bg=WHITE, fg=WHITE, width=23)
        self.username_textbox.pack(side=tk.LEFT)

        self.username_button = tk.Button(self.top_frame, text="Unirse", font=(FONT_FAMILY, BUTTON_SIZE), bg=BLUE, fg=WHITE, command=self.connect)
        self.username_button.pack(side=tk.LEFT, padx=15)

        self.message_textbox = tk.Entry(self.bottom_frame, font=(FONT_FAMILY, FONT_SIZE), bg=WHITE, fg=WHITE, width=38)
        self.message_textbox.pack(side=tk.LEFT, padx=10)

        self.message_button = tk.Button(self.bottom_frame, text="Enviar", font=(FONT_FAMILY, BUTTON_SIZE), bg=BLUE, fg=WHITE, command=self.enviar_mensaje)
        self.message_button.pack(side=tk.LEFT, padx=10)

        self.message_box = scrolledtext.ScrolledText(self.middle_frame, font=(FONT_FAMILY, SMALL_FONT_SIZE), bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)
        self.message_box.config(state=tk.DISABLED)
        self.message_box.pack(side=tk.TOP)
        
        
    def run(self):
        self.root.mainloop()
        
    def connect(self) -> None:
        user = self.username_textbox.get()
        if user :
            self.client.connect(HOST,PORT, self.username_textbox, self.username_button, self.message_box)
        else:
            messagebox.showerror("Usuario invalido", "El usuario no puede estar vacio")
            
    def enviar_mensaje(self):
        message = self.message_textbox.get()
        if message:
            self.client.enviar_mensaje(message)
            self.message_textbox.delete(0, tk.END)
        else:
            messagebox.showerror("Mensaje vacio", "No puedes enviar un mensaje vacio.")
        
if __name__ == '__main__':
    home= sandbox()
    home.run()