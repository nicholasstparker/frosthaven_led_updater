from mock_modules import MockBoard as board, MockNeoPixel as neopixel
import time
from typing import Tuple


class Color:
    RED: Tuple[int, int, int] = (255, 0, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    OFF: Tuple[int, int, int] = (0, 0, 0)


class LEDController:
    """
    A controller for managing a strip of NeoPixel LEDs.

    Attributes:
        num_pixels (int): The number of pixels in the NeoPixel strip.
        pixels (NeoPixel): The NeoPixel object representing the LED strip.
        led_states (list of tuple): A list of tuples representing the color of each LED in the
        strip. THIS IS SOFTWARE MANAGED STATE! LED data is one directional, so we resort to
        keeping track of it's state in software. Everytime we update the LED strip, we update
        led_states to update the current state.

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
        self.pixels = neopixel(pin, num_pixels,
                               brightness=1.0,
                               auto_write=False,
                               pixel_order="BRG")
        self.led_states = [Color.OFF] * num_pixels
        self.future_led_states = [Color.OFF] * num_pixels
        self.pixels.fill(Color.OFF)
        self.pixels.show()
        self.pixels.show_called = False

    def get_current_color(self, led_index: int) -> Tuple[int, int, int]:
        return self.led_states[led_index]

    def get_future_color(self, led_index: int) -> Tuple[int, int, int]:
        return self.future_led_states[led_index]

    def current_color_equals_future_color(self, index: int) -> bool:
        return self.get_current_color(index) == self.get_future_color(index)

    def set_all_colors(self, color: Tuple[int, int, int]):
        self.future_led_states = [color] * self.num_pixels
        if self.future_led_states != self.led_states:
            self.led_states = self.future_led_states
            self.pixels.fill(color)
            self.pixels.show()

    def clear(self):
        self.set_all_colors(Color.OFF)

    def start_up_sequence(self):
        self.color_wipe(Color.RED)
        self.color_wipe()
        self.color_wipe(Color.GREEN)
        self.color_wipe()
        self.color_wipe(Color.BLUE)
        self.color_wipe()
        self.color_wipe(Color.WHITE)
        self.color_wipe()

    def _update_led_color(self, led_index: int, color: Tuple[int, int, int], bulk_update=True):
        self.pixels[led_index] = color
        if bulk_update is False:
            self.pixels.show()

    def update_single_led(self, led_index: int, color: Tuple[int, int, int]):
        self.set_future_led_state(led_index, led_index + 1, color)
        self.update_led_state_to_future()

    def set_future_led_state(self, start: int, end: int, color: Tuple[int, int, int]):
        for led_index in range(start, end):
            if self.get_current_color(led_index) != color:
                self.future_led_states[led_index] = color

    def update_led_state_to_future(self, bulk_update=True):
        for led_index in range(self.num_pixels):
            if self.current_color_equals_future_color(led_index) is False:
                self.led_states[led_index] = self.future_led_states[led_index]
                self._update_led_color(led_index, self.led_states[led_index], bulk_update)
        if bulk_update is True:
            self.pixels.show()

    def color_wipe(self, color: Tuple[int, int, int] = Color.OFF):
        self.set_future_led_state(0, self.num_pixels, color)
        self.update_led_state_to_future(bulk_update=False)


class FrosthavenLEDStates(LEDController):
    def first_card_selection_round(self):
        self.color_wipe()
        self.set_future_led_state(0, 31, Color.RED)
        self.set_future_led_state(31, 51, Color.WHITE)
        self.set_future_led_state(51, 82, Color.RED)
        self.set_future_led_state(82, 100, Color.WHITE)
        self.update_led_state_to_future(bulk_update=False)
