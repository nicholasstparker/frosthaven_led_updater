import unittest
from unittest.mock import patch, MagicMock
import board
from led_controller import LEDController, Color  # Replace `your_module` with the actual module name


class TestLEDController(unittest.TestCase):

    @patch('neopixel.NeoPixel')
    def test_initialization(self, MockNeoPixel):
        mock_pixels = MagicMock()
        MockNeoPixel.return_value = mock_pixels

        controller = LEDController(pin=board.D18, num_pixels=100)

        MockNeoPixel.assert_called_once_with(board.D18, 100, brightness=1.0, auto_write=False, pixel_order="BRG")

    @patch('neopixel.NeoPixel')
    def test_set_color(self, MockNeoPixel):
        mock_pixels = MagicMock()
        MockNeoPixel.return_value = mock_pixels
        controller = LEDController(pin=board.D18, num_pixels=100)

        controller.set_color(0, Color.RED.rgb())

        mock_pixels.__setitem__.assert_called_once_with(0, (255, 0, 0))
        mock_pixels.show.assert_called_once()

    @patch('neopixel.NeoPixel')
    def test_set_all_colors(self, MockNeoPixel):
        mock_pixels = MagicMock()
        MockNeoPixel.return_value = mock_pixels
        controller = LEDController(pin=board.D18, num_pixels=100)

        controller.set_all_colors(Color.GREEN.rgb())

        mock_pixels.fill.assert_called_once_with((0, 255, 0))
        mock_pixels.show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
