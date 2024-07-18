from typing import Tuple
from led_controller import LEDController, Color


class Element:
    def __init__(self, element: str, start_index: int, end_index: int, color: Tuple[int, int, int], led: LEDController):
        self.element = element
        self.start_index = start_index
        self.end_index = end_index
        self.color = color
        self.led = led
        self.state = None

    def set_element_color(self, color: tuple[int, int, int]):
        self.led.set_future_led_state(31, 32, (0, 0, 0))
        self.led.set_future_led_state(self.start_index, self.end_index, color)
        self.led.set_future_led_state(50, 51, (0, 0, 0))


class Elements:
    def __init__(self):
        self.elements = dict()

    def __iter__(self):
        return iter(self.elements.items())

    def add_element(self, element: Element):
        self.elements[element.element] = element

    def get_element(self, element: str) -> Element or None:
        return self.elements.get(element, None)

    def get_color(self, element: str) -> Tuple[int, int, int]:
        return self.elements.get(element).color

    def get_start_index(self, element: str) -> int:
        return self.elements.get(element).start_index

    def get_end_index(self, element: str) -> int:
        return self.elements.get(element).end_index

    def get_state(self, element: str) -> str or None:
        return self.elements.get(element).state

    def set_all_element_colors(self):
        for element, element_state in self.elements.items():
            match element_state.state:
                case "DEAD":
                    element_state.set_element_color(element_state.start_index, element_state.end_index, Color.OFF)
                case _:
                    element_state.set_element_color(element_state.start_index, element_state.end_index, element_state.color)
