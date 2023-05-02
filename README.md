## Websocket TCP/IP in Python - University assignment

This Python code implements a basic TCP/IP server and client communication model. The server script creates a TCP/IP socket, binds it to a specific IP address and port number, listens for incoming connections from clients, receives data from the client, converts the received message to uppercase, and sends the message back to the client. The client script creates a socket, connects to the server's IP address and port number, and sends a string to the server. Once the server receives the message, it converts it to uppercase and sends it back to the client.

## Requirements
- Python 2.7 or higher
- A working internet connection

## Running the code
1. Save the server and client code to separate files with the extension ".py".
2. Run the server script by opening a command prompt and typing `python server.py`.
3. In another command prompt, run the client script by typing `python client.py`.
4. Follow the instructions in the client prompt to send a message to the server and receive a response.

Note: The IP address and port number used in the code are set to default values. You can modify them to suit your specific needs.
## Author

- [Junior Camargo](https://github.com/JuniorC07)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.