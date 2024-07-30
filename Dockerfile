FROM debian:latest

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

CMD ["python3", "test_led_docker.py"]