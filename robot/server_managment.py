import socket
import threading

class Server:
    def __init__(self, host, port, header=64, format="utf-8", disconnect_cmd="!bye"):
        self.host = host
        self.port = port
        self.header = header
        self.format = format
        self.disconnect_cmd = disconnect_cmd
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

    def start(self):
        self.server_socket.listen()
        print(f"Server started on {self.host}:{self.port}...")
        while True:
            conn, addr = self.server_socket.accept()
            print(f"Connected to {addr}")
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        print(f"New connection from {addr}")
        connected = True
        while connected:
            msg_length = conn.recv(self.header).decode(self.format)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.format)
                print(f"Received message: {msg}")
                if msg == self.disconnect_cmd:
                    connected = False
                # Handle other commands...
        conn.close()
