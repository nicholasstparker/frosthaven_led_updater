import neopixel
# from mock_modules import MockNeoPixel as neopixel
from typing import Tuple


# For testing, use the mock_modules.py file to mock the neopixel module. remove NeoPixel from the
# LEDController class so it uses neopixel instead of neopixel.NeoPixel.


class Color:
    RED: Tuple[int, int, int] = (255, 0, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    OFF: Tuple[int, int, int] = (0, 0, 0)


class LEDController:
    """
    A controller for managing LED states and animations for NeoPixel LEDs.

    Attributes:
        num_pixels (int): The number of pixels in the LED strip.
        pixels (NeoPixel): The NeoPixel object representing the LED strip.
        led_states (list): The current color state of each LED. This is software state tracking.
            LED data lines are one directional, so we'll track it here.
        future_led_states (list): The future (intended) color state of each LED. The purpose of
            this is to first update future_led_states, compare it to led_states, and then update the
            strip all at one time. This is to prevent flickering of the LEDs and to ensure only one
            led_state update per state change. It also allows animations of EVERY state with the
            bulk_update flag.
        pixels.show_called (bool): Flag to track if the `show` method has been called.

    Methods:
        get_current_color(led_index): Returns the current color of the specified LED.
        get_future_color(led_index): Returns the future color of the specified LED.
        current_color_equals_future_color(index): Checks if the current and future colors are the
            same for the specified LED.
        set_all_colors(color): Sets all LEDs to the specified color.
        clear(): Turns off all LEDs.
        start_up_sequence(): Executes a startup sequence of color wipes.
        _update_led_color(led_index, color, bulk_update): Updates the color of a single LED.
        update_single_led(led_index, color): Updates the color of a single LED and applies the
            change immediately.
        set_future_led_state(start, end, color): Sets the future state for a range of LEDs.
        update_led_state_to_future(bulk_update): Updates the LED strip to match the future state.
        color_wipe(color): Fills the LED strip with a single color, one LED at a time.
    """

    def __init__(self, pin, num_pixels: int = 100):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(pin, num_pixels,
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
