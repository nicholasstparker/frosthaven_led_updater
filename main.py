import time
from client import Client

if __name__ == "__main__":
    client = Client("192.168.0.196", 4567)
    client.connect()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client.disconnect()
