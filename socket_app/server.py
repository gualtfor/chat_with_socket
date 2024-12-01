import socket
import threading
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import postgres.connection as pc
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
LISTENER_LIMIT = int(os.getenv('LISTENER_LIMIT'))

active_clients = []

def escucharMensajes(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                enviarMensajeUnUsuario(client, message)
            else:
                print(f"El mensaje enviado por el usuario {username} esta vacio")
        except Exception:
            break
    client.close()

        
def enviarMensajeUnUsuario(client, message):
    if isinstance(message, list):
        formatted_message = "\n\n  ".join(" ".join(map(str, part)) for part in message) + '\n'
        client.send(formatted_message.encode())
    else:
        client.send(message.encode())

def manejadorClientes(client, host, port):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client, host, port))
            prompt_message = "[SERVER] " + f"{username} fue agregado"
            enviarMensajeUnUsuario(client, prompt_message)
            break
        else:
            print("El usuario esta vacio")

    threading.Thread(target=escucharMensajes, args=(client, username, )).start()
    
def executeCommand(client_db: pc.PostgresConnection, command: str, client: socket.socket) -> None:
    try:
        client_db.execute_query(command)
        prompt_message = "[SERVER] Operación realizada con exito."
        enviarMensajeUnUsuario(client, prompt_message)
    except:
        prompt_message = "[SERVER]  Datos ausentes o mal formato: Error al ejecutar la consulta."
        enviarMensajeUnUsuario(client, prompt_message)

    
    
def executeCommandSelect(client_db: pc.PostgresConnection, command: str, client) -> None:
    try:
        prompt_message = "[SERVER] Resultado de la consulta."
        enviarMensajeUnUsuario(client, prompt_message)
        message = client_db.retrieve_data_query(command)
        enviarMensajeUnUsuario(client, message)
    except:
        prompt_message = "[SERVER]  Datos ausentes o mal formato: Error al ejecutar la consulta."
        enviarMensajeUnUsuario(client, prompt_message)

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