# Socket-based Chat Service

This is a simple chat service implemented using sockets and TCP in Python. It allows devices to send and receive messages over a network. You and your friend can use this service to exchange messages by typing them in the console. The chat service consists of two scripts: `server.py` and `client.py`.

## Running the Code

To run the chat service, follow these steps:

### Server Script (`server.py`)

1. Open a terminal or command prompt.

2. Navigate to the directory where the `server.py` script is located.

3. Set the server's IP address and port:
   - Modify the `server_ip` variable in the `server.py` script to the IP address of the device running the server script. Make sure the IP address is accessible to the client devices.
   - Update the `server_port` variable in the `server.py` script to specify the port number on which the server should listen for incoming connections.

4. Run the server script:
   - Execute the following command:
     ```
     python server.py
     ```
   - The server will start listening for client connections and display the IP address and port it is listening on.

### Client Script (`client.py`)

1. Open a new terminal or command prompt.

2. Navigate to the directory where the `client.py` script is located.

3. Set the server's IP address and port:
   - Update the `server_ip` variable in the `client.py` script with the IP address of the device running the server script.

4. Run the client script:
   - Execute the following command:
     ```
     python client.py
     ```
   - The client will establish a connection with the server and start listening for incoming messages.

5. Chatting:
   - Enter messages in the client's console to send them to the other connected client.
   - The messages will be displayed in the respective client's console.

6. Exiting the chat:
   - To exit the chat session and terminate the client script, type "exit" (without quotes) in the client's console.
   - The client script will close the connection with the server and exit.

## Notes

- The chat service uses TCP/IP sockets, which provide reliable and ordered message delivery.
- The server script listens for incoming connections from clients and relays messages between them.
- The client script connects to the server and allows users to send and receive messages.
- The server's IP address and port must be known to the clients in order to establish a connection.
- This implementation supports a basic one-on-one chat session between two clients.
- You can run the server script on one device and the client script on multiple devices to facilitate chat sessions between different users.

Please note that this is a basic implementation for educational purposes. It does not include advanced features like authentication, encryption, or error handling. Feel free to modify and enhance the code to suit your specific requirements.

**Disclaimer:** Ensure that you have the necessary permissions to establish connections and communicate over the network.
