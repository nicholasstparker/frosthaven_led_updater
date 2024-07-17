class MockBoard:
    pass


class MockNeoPixel:
    def __init__(self, pin, num_pixels, brightness=1.0, auto_write=False, pixel_order="BRG"):
        self.pin = pin
        self.num_pixels = num_pixels
        self.brightness = brightness
        self.auto_write = auto_write
        self.pixel_order = pixel_order
        self.pixels = [(0, 0, 0)] * num_pixels  # Initialize all pixels to off
        self.show_called = False

    def __setitem__(self, index, color):
        if 0 <= index < self.num_pixels:
            self.pixels[index] = color
            if self.auto_write:
                self.show()
        else:
            raise IndexError("Pixel index out of range")

    def __getitem__(self, index):
        if 0 <= index < self.num_pixels:
            return self.pixels[index]
        else:
            raise IndexError("Pixel index out of range")

    def show(self):
        self.show_called = True
        return True

    def fill(self, color):
        self.pixels = [color] * self.num_pixels
        if self.auto_write:
            self.show()
