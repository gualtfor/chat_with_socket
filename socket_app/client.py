import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from server import executeCommand, executeCommandSelect
import postgres.connection as pc

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_db = self.connect_to_db()

    def connect_to_db(self):
        try:
            db_connection = pc.PostgresConnection()
            db_connection.connect()
            return db_connection
        except Exception as e:
            print(f"Error {e}")
        
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
    
    def procesar_comando(self, tabla, operacion, datos, condiciones) -> None:
        if datos != '':
            match operacion:
                case "select":
                    query = f"SELECT {datos} FROM hrAirline.{tabla} {condiciones}"
                    executeCommandSelect(self.client_db, query, self.client)
                case "insert":
                    match tabla:
                        case "empleados":
                            fields = "nombres, apellidos, numero_identidad, fecha_de_nacimiento, nacionalidad, estado_civil, genero, ciudad_residencia, direccion, telefono, fecha_contrato, jefe_inmediato, id_sede, id_profesion, id_departamento, id_avion"
                        case "departamento":
                            fields = "nombre, gerente, descripcion, fecha_inicial"
                        case "profesion":
                            fields = "nombre, descripcion, dotacion_vestido, requiere_experiencia, nivel, tipo, fecha_inicial"
                        case "expediente":
                            fields = "id_empleado, tipo, descripcion, documento_realizado, nivel, afecta_cv, fecha_reporte"
                        case "aviones":
                            fields = "nombre, descripcion, tipo, marca, estado"
                        case "sedes":
                            fields = "nombre, descripcion, activo, ciudad, nombre_calle, n_calle_av, n_casa, fecha_inicial"
                    datos = ", ".join([f"'{datos.strip()}'" for datos in datos.split(",")])
                    query = f"INSERT INTO hrAirline.{tabla}({fields}) VALUES({datos})"
                    executeCommand(self.client_db, query, self.client)
                case "update":
                    query = f"UPDATE hrAirline.{tabla} SET {datos} WHERE {condiciones}"
                    executeCommand(self.client_db, query, self.client)
                case "delete":
                    query = f"DELETE FROM hrAirline.{tabla} WHERE {datos}"
                    executeCommand(self.client_db, query, self.client)
        else:
            messagebox.showerror("Datos ausentes", "Debe aportar los datos a consultar segun la operación")
    
    def escuchar_mensaje_del_servidor(self, client, message_box: tk.scrolledtext):
        while True:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                self.agregar_mensaje(f"{message}", message_box)
            else:
                messagebox.showerror("Error", "El mensaje del usuario se encuentra vacio")
