from typing import Tuple


class Element:
    def __init__(self, element: str, start_index: int, end_index: int, color: Tuple[int, int, int]):
        self.element = element
        self.start_index = start_index
        self.end_index = end_index
        self.color = color
        self.state = None


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
