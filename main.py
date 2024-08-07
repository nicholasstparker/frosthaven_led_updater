import os
import time
from client import Client

if __name__ == "__main__":
    address = str(os.getenv("SERVER_ADDRESS", "192.168.0.130"))
    port = int(os.getenv("SERVER_PORT", 4567))
    client = Client(address, port)
    client.connect()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client.disconnect()
