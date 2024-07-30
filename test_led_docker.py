from led_controller import LEDController, Color
from time import sleep

led = LEDController()

while True:
    led.set_all_colors(Color.RED)
    sleep(5)
    led.set_all_colors(Color.GREEN)
    sleep(5)
    led.set_all_colors(Color.BLUE)
    sleep(5)
