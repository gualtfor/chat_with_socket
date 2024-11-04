import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def agregar_mensaje(self, message: str, message_box: tk.scrolledtext) -> None:
        message_box.config(state=tk.NORMAL)
        message_box.insert(tk.END, message + '\n')
        message_box.config(state=tk.DISABLED)
    
    def connect(self, host: str, port: int, username_textbox: tk.Entry, username_button:tk.Button, message_box: tk.scrolledtext) -> None:
        try:
            self.client.connect((host, port))
            print("Conexion exitosa con el servidor")
            self.agregar_mensaje("[SERVER] conexion exitosa a el servidor.", message_box)
            user = username_textbox.get()
            if user != '':
                self.client.sendall(user.encode())
            else:
                messagebox.showerror("Usuario invalido", "El usuario no puede estar vacio")
                
            threading.Thread(target=self.escuchar_mensaje_del_servidor, args=(self.client, message_box,)).start()
            username_textbox.config(state=tk.DISABLED)
            username_button.config(state=tk.DISABLED)
        except Exception as e:
            print(f"Error {e}")
            messagebox.showerror("No se puede hacer la conexion con el servidor", f"No fue exitosa la conexion al servidor en el host {host} en el puerto {port}")
    
    def enviar_mensaje(self, message) -> None:
        if message != '':
            self.client.sendall(message.encode())
            # message_textbox.delete(0, len(message))
    
    def escuchar_mensaje_del_servidor(self, client, message_box: tk.scrolledtext):
        while True:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                usuario = message.split('~')[0]
                contenido = message.split('~')[1]
                if contenido not in ('chao', 'Chao') and usuario != 'active':
                    print(f"[{usuario}] {contenido}", message_box)
                    self.agregar_mensaje(f"[{usuario}] {contenido}", message_box)
                elif usuario == 'active':
                    contenido = message.split('~')[1]
                    print(f"este es la list {message}")
                    print(f"los componentes {contenido}", message_box)
                    self.agregar_mensaje(f"{contenido}", message_box)
                else:
                    self.agregar_mensaje(f"[{usuario}] Finalizo la sesión", message_box)
                    print("Servidor cerrado")
                    client.close()
                    break
            else:
                messagebox.showerror("Error", "El mensaje del usuario se encuentra vacio")
