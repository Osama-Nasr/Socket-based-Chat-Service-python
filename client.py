import socket

# Define the server's IP address and port
server_ip = "192.168.16.147"  # Change this to the IP address of the server device
server_port = 12345

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"\n{message}")
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

# Start the receiving thread
import threading
threading.Thread(target=receive_messages).start()

while True:
    message = input("Type a message: ")
    if message.lower() == "exit":
        break
    client_socket.sendall(message.encode("utf-8"))

client_socket.close()
