import json
import socket
import threading
import time
from game_state_handler import GameStateHandler


class Client:
    def __init__(self, address, port, message_callback=None):
        self.server_address = address
        self.server_port = port
        self.sock = None
        self._server_responsive = True
        self.buffer = ""
        self.message_callback = message_callback
        self.reconnect_interval = 5
        self.game_state_handler = GameStateHandler()

    def connect(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.server_address, self.server_port))
                print(f'Connected to {self.server_address}:{self.server_port}')
                self.listen()
                self.send("init version:1.0")
                self.send_ping()
                break
            except Exception as e:
                print(f'Error connecting to the server: {e}. Retrying in {self.reconnect_interval} '
                      f'seconds...')
                time.sleep(self.reconnect_interval)

    def send(self, message):
        if self.sock:
            try:
                self.sock.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f'Error sending message: {e}')

    def send_ping(self):
        if self.sock and self._server_responsive:
            threading.Timer(12.0, self.send_ping).start()
            self.send("ping")
            self._server_responsive = False

    def listen(self):
        def run():
            while True:
                try:
                    data = self.sock.recv(1024)
                    if data:
                        self.on_receive_data(data)
                    else:
                        print("Server closed connection.")
                        self._server_responsive = False
                        self.reconnect()
                        break
                except Exception as e:
                    print(f'Error receiving data: {e}')
                    self._server_responsive = False
                    self.reconnect()
                    break

        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    def on_receive_data(self, data):
        self.buffer += data.decode('utf-8')
        start_marker = "S3nD:"
        end_marker = "[EOM]"

        while start_marker in self.buffer and end_marker in self.buffer:
            start_index = self.buffer.index(start_marker)
            end_index = self.buffer.index(end_marker) + len(end_marker)
            complete_message = self.buffer[start_index:end_index]

            self.buffer = self.buffer[end_index:]

            self.process_message(complete_message)

    def process_message(self, message):
        if "pong" in message:
            self._server_responsive = True
        else:
            json_start = message.find("GameState:")
            if json_start != -1:
                json_start += len("GameState:")
                json_end = message.rfind("[EOM]")
                json_str = message[json_start:json_end].strip()
                try:
                    game_state = json.loads(json_str)
                    self.game_state_handler.handle(game_state)
                except json.JSONDecodeError as e:
                    print(f'Error decoding JSON: {e}')

    def reconnect(self):
        print(f'Attempting to reconnect in {self.reconnect_interval} seconds...')
        time.sleep(self.reconnect_interval)
        self.connect()

    def disconnect(self):
        if self.sock:
            self.sock.close()
            print("Disconnected from server")
