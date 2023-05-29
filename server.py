import socket
import threading

# Define the server's IP address and port
server_ip = "192.168.148.147"  # Change this to the IP address of the server device
server_port = 12345

# Create a socket and bind it to the IP and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(2)  # Change the number of clients the server can accept (2 in this case)
print(f"Server listening on {server_ip}:{server_port}")

# Initialize the list of connected clients
clients = []

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"{client_address}: {message}")
                broadcast(message, client_socket)
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    clients.remove(client_socket)
    print(f"Connection closed with {client_address}")

def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.sendall(message.encode("utf-8"))
            except Exception as e:
                print(f"Error broadcasting message: {e}")

while True:
    client_socket, client_address = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
