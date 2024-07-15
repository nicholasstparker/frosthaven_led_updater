import board
import neopixel
import time
from typing import List, Tuple


class LEDController:
    def __init__(self, pin: board, num_pixels: int = 100):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(pin, num_pixels, brightness=1.0, auto_write=False, pixel_order="BRG")
        self.led_colors = [(0, 0, 0)] * num_pixels
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

        self.start_up_sequence()

    def set_color(self, index: int, color: Tuple[int, int, int], bulk_update: bool = True):
        if 0 <= index < self.num_pixels:
            if not self.get_color(index) == color:
                self.led_colors[index] = color
                self.pixels[index] = color
                if bulk_update is False:
                    self.pixels.show()
            else:
                pass
                # print(f"Pixel at index {index} is already {color}")

    def get_color(self, index: int) -> Tuple[int, int, int] or None:
        if 0 <= index < self.num_pixels:
            return self.led_colors[index]
        return None

    def set_all_colors(self, color: Tuple[int, int, int]):
        temp_colors = [color] * self.num_pixels
        if temp_colors != self.led_colors:
            self.led_colors = temp_colors
            self.pixels.fill(color)
            self.pixels.show()

    def set_color_in_range(self, start: int, end: int, color: Tuple[int, int, int], bulk_update: bool = True, delay: float = 0.0):
        for i in range(start, end):
            self.set_color(i, color, bulk_update)
            if delay:
                time.sleep(delay)
        if bulk_update is True:
            self.pixels.show()

    def clear(self):
        self.set_all_colors((0, 0, 0))

    def color_wipe(self, color: tuple[int, int, int] = (0, 0, 0), delay: float = 0.0):
        self.set_color_in_range(0, self.num_pixels, color, bulk_update=False, delay=delay)

    def start_up_sequence(self):
        self.color_wipe((255, 0, 0))
        self.color_wipe()
        self.color_wipe((0, 255, 0))
        self.color_wipe()
        self.color_wipe((0, 0, 255))
        self.color_wipe()
        self.color_wipe((255, 255, 255))

    def first_round_not_ready_animation(self):
        pass

    def first_round_ready_animation(self):
        pass
