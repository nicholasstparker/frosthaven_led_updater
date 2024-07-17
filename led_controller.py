import board
import neopixel
import time
from typing import Tuple


class Color:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def rgb(self) -> Tuple[int, int, int]:
        return self.red, self.green, self.blue

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.rgb() == other.rgb()
        elif isinstance(other, Tuple):
            return self.rgb() == other
        return False

    def __repr__(self):
        return f"Color({self.red}, {self.green}, {self.blue})"


Color.RED = Color(255, 0, 0)
Color.GREEN = Color(0, 255, 0)
Color.BLUE = Color(0, 0, 255)
Color.WHITE = Color(255, 255, 255)
Color.OFF = Color(0, 0, 0)


class LEDController:
    """
    A controller for managing a strip of NeoPixel LEDs.

    Attributes:
        num_pixels (int): The number of pixels in the NeoPixel strip.
        pixels (NeoPixel): The NeoPixel object representing the LED strip.
        led_colors (list of tuple): A list of tuples representing the color of each LED in the strip.

    Methods:
        set_color(index, color, bulk_update): Sets the color of a single LED.
        get_color(index): Returns the color of the LED at the specified index.
        set_all_colors(color): Sets the color of all LEDs in the strip to the specified color.
        set_color_in_range(start, end, color, bulk_update, delay): Sets the color of a range of LEDs.
        clear(): Clears the LED strip, setting all LEDs to off.
        color_wipe(color, delay): Fills the strip with a single color, one LED at a time.
        start_up_sequence(): Performs a startup sequence, cycling through several colors.
    """

    def __init__(self, pin: board, num_pixels: int = 100):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(pin, num_pixels, brightness=1.0, auto_write=False, pixel_order="BRG")
        self.led_colors = [(0, 0, 0)] * num_pixels
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        self.start_up_sequence()

    def set_color(self, index: int, color: Tuple[int, int, int], bulk_update: bool = True):
        """
        Sets the color of a single LED.

        Parameters:
            index (int): The index of the LED to set.
            color (Tuple[int, int, int]): The color to set the LED to.
            bulk_update (bool): If False, updates the LED strip immediately.
        """
        if 0 <= index < self.num_pixels:
            if not self.get_color(index) == color:
                self.led_colors[index] = color
                self.pixels[index] = color
                if bulk_update is False:
                    self.pixels.show()

    def get_color(self, index: int) -> Tuple[int, int, int] or None:
        """
        Returns the color of the LED at the specified index.

        Parameters:
            index (int): The index of the LED.

        Returns:
            Tuple[int, int, int] or None: The color of the LED, or None if the index is out of range.
        """
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
        """
        Sets the color of a range of LEDs.

        Parameters:
            start (int): The starting index of the range.
            end (int): The ending index of the range.
            color (Tuple[int, int, int]): The color to set the LEDs to.
            bulk_update (bool): If True, updates the LED strip after setting all colors in the range.
            delay (float): The delay between setting each LED's color.
        """
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

    def first_card_selection_round(self):
        self.color_wipe()
        self.set_color_in_range(0, 31, (255, 0, 0), bulk_update=False)
        self.set_color_in_range(31, 51, (255, 255, 255), bulk_update=False)
        self.set_color_in_range(51, 82, (255, 0, 0), bulk_update=False)
        self.set_color_in_range(82, 100, (255, 255, 255), bulk_update=False)

    def set_element_colors(self, elements):
        for element, element_state in elements:
            if element_state.state in ["FULL", "WANING"]:
                self.set_color_in_range(element_state.start_index, element_state.end_index, element_state.color)
            else:
                self.set_color_in_range(element_state.start_index, element_state.end_index, (0, 0, 0))
