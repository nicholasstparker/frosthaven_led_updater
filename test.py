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

print(Color.RED)
