import socket
import threading
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
LISTENER_LIMIT = int(os.getenv('LISTENER_LIMIT'))

active_clients = []

def escucharMensajes(client, username):
    prev_mess = None
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message != '' and prev_mess not in ('Chao', 'chao'):
                final_msg = username + '~' + message
                enviarMensajeTodos(final_msg)
                prev_mess = message
            elif prev_mess in ('Chao', 'chao'):
                break
            else:
                print(f"El mensaje enviado por el usuario {username} esta vacio")
        except Exception:
            break
    client.close()

def enviarMensajeCliente(client, message):
    client.sendall(message.encode())


def enviarMensajeTodos(message):
    for user in active_clients:
        enviarMensajeCliente(user[1], message)
        
def usuariosActivosSandbox(client):
    print(f"{client}")
    message = f"active~Los usuarios activos son:\n"
    for val, user in enumerate(active_clients):
        message += f"    {val} {user[0]}\n"
    enviarMensajeUnUsuario(client, message)
        
def enviarMensajeUnUsuario(client, message):
    client.send(message.encode())

def manejadorClientes(client, host, port):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client, host, port))
            prompt_message = "SERVER~" + f"{username} fue agregado al chat"
            enviarMensajeTodos(prompt_message)
            usuariosActivosSandbox(client)
            break
        else:
            print("El usuario esta vacio")

    threading.Thread(target=escucharMensajes, args=(client, username, )).start()

# Main function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"El servido esta activo en {HOST} {PORT}")

        server.listen(LISTENER_LIMIT)
        print("El servidor esta escuchando...")
        while True:
            client, address = server.accept()
            print(f"Conexion exitosa del usuario {address[0]} {address[1]}")
            threading.Thread(target=manejadorClientes, args=(client, address[0], address[1])).start()
    except Exception as e:
        print(f"Error {e}")
    finally:
        server.close()
        print("Servidor cerrado")
    

if __name__ == '__main__':
    main()