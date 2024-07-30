FROM balenalib/rpi-raspbian

RUN apt-get update && apt-get install -y python3 python3-pip python3-rpi.gpio

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

CMD ["python3", "test_led_docker.py"]