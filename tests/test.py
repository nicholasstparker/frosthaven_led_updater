import unittest
from unittest.mock import patch
from led_controller import LEDController, Color


class TestLEDController(unittest.TestCase):
    def test_initial_state_black(self):
        led_controller = LEDController(18, 100)
        self.assertTrue(led_controller.led_states == [(0, 0, 0)] * led_controller.num_pixels)
        self.assertTrue(led_controller.future_led_states == [(0, 0, 0)] * led_controller.num_pixels)

    def test_set_all_colors(self):
        led_controller = LEDController(18, 100)
        led_controller.set_all_colors((0, 0, 0))
        self.assertTrue(led_controller.led_states == [(0, 0, 0)] * led_controller.num_pixels)
        self.assertTrue(led_controller.future_led_states == [(0, 0, 0)] * led_controller.num_pixels)
        self.assertTrue(led_controller.get_current_color(50) == (0, 0, 0))
        self.assertTrue(led_controller.get_future_color(50) == (0, 0, 0))
        led_controller.set_all_colors((255, 255, 255))
        self.assertTrue(led_controller.get_current_color(50) == (255, 255, 255))
        self.assertTrue(led_controller.get_future_color(50) == (255, 255, 255))
        self.assertTrue(led_controller.led_states == [(255, 255, 255)] * led_controller.num_pixels)
        self.assertTrue(led_controller.future_led_states == [(255, 255, 255)] * led_controller.num_pixels)

    def test_get_current_future_color(self):
        led_controller = LEDController(18, 100)
        led_controller.set_all_colors((255, 255, 255))
        self.assertTrue(led_controller.get_current_color(0) == (255, 255, 255))
        self.assertTrue(led_controller.get_future_color(0) == (255, 255, 255))
        self.assertTrue(led_controller.current_color_equals_future_color(0))

    def test_update_single_led(self):
        led_controller = LEDController(18, 100)
        led_controller.set_all_colors((0, 0, 0))
        led_controller.update_single_led(0, (255, 255, 255))
        self.assertTrue(led_controller.get_current_color(0) == (255, 255, 255))
        self.assertTrue(led_controller.get_future_color(0) == (255, 255, 255))
        self.assertTrue(led_controller.get_current_color(1) == (0, 0, 0))
        self.assertTrue(led_controller.get_future_color(1) == (0, 0, 0))

    def test_set_future_led_state(self):
        led_controller = LEDController(18, 100)
        led_controller.set_all_colors((0, 0, 0))

        for i in range(100):
            self.assertEqual(led_controller.get_current_color(i), (0, 0, 0))
            self.assertEqual(led_controller.get_future_color(i), (0, 0, 0))

        led_controller.set_future_led_state(0, 50, (255, 255, 255))

        for i in range(50):
            self.assertEqual(led_controller.get_future_color(i), (255, 255, 255))

        for i in range(50, 100):
            self.assertEqual(led_controller.get_future_color(i), (0, 0, 0))

        for i in range(100):
            self.assertEqual(led_controller.get_current_color(i), (0, 0, 0))

    def test_update_led_state_to_future(self):
        led_controller = LEDController(18, 100)
        led_controller.set_all_colors((0, 0, 0))

        # Set future states
        led_controller.set_future_led_state(0, 50, (255, 255, 255))
        led_controller.update_led_state_to_future()

        # Check that current states are updated to future states
        for i in range(50):
            self.assertEqual(led_controller.get_current_color(i), (255, 255, 255))

        # Check that current states out of range remain unchanged
        for i in range(50, 100):
            self.assertEqual(led_controller.get_current_color(i), (0, 0, 0))

    def test_color_wipe(self):
        led_controller = LEDController(18, 100)
        led_controller.set_all_colors((0, 0, 0))

        # Perform color wipe with white color
        led_controller.color_wipe((255, 255, 255))

        # Check that all LEDs are updated to white
        for i in range(100):
            self.assertEqual(led_controller.get_current_color(i), (255, 255, 255))

        # Perform color wipe with off color (black)
        led_controller.color_wipe()

        # Check that all LEDs are updated to off (black)
        for i in range(100):
            self.assertEqual(led_controller.get_current_color(i), (0, 0, 0))

    def test_update_led_state_to_future_bulk_update(self):
        led_controller = LEDController(18, 100)

        self.assertFalse(led_controller.pixels.show_called)

        led_controller.set_future_led_state(0, 50, (255, 255, 255))
        led_controller.update_led_state_to_future(bulk_update=True)

        self.assertTrue(led_controller.pixels.show_called)

        led_controller.pixels.show_called = False

        led_controller.set_future_led_state(0, 50, (255, 0, 0))
        led_controller.update_led_state_to_future(bulk_update=False)

        for i in range(50):
            self.assertEqual(led_controller.get_current_color(i), (255, 0, 0))

    def test_clear(self):
        led_controller = LEDController(18, 100)
        led_controller.set_all_colors((255, 255, 255))
        self.assertTrue(led_controller.led_states == [(255, 255, 255)] * led_controller.num_pixels)
        self.assertTrue(led_controller.future_led_states == [(255, 255, 255)] *
                        led_controller.num_pixels)
        self.assertTrue(led_controller.get_current_color(50) == (255, 255, 255))
        self.assertTrue(led_controller.get_future_color(50) == (255, 255, 255))
        led_controller.clear()
        self.assertTrue(led_controller.led_states == [(0, 0, 0)] * led_controller.num_pixels)
        self.assertTrue(led_controller.future_led_states == [(0, 0, 0)] * led_controller.num_pixels)
        self.assertTrue(led_controller.get_current_color(50) == (0, 0, 0))
        self.assertTrue(led_controller.get_future_color(50) == (0, 0, 0))
        self.assertTrue(led_controller.led_states == [(0, 0, 0)] * led_controller.num_pixels)
        self.assertTrue(led_controller.future_led_states == [(0, 0, 0)] * led_controller.num_pixels)

    @patch.object(LEDController, 'color_wipe')
    def test_start_up_sequence(self, mock_color_wipe):
        led_controller = LEDController(18, 100)

        # Run the startup sequence
        led_controller.start_up_sequence()

        # Verify that color_wipe was called with the expected colors
        expected_calls = [
            ((Color.RED,),),
            ((),),
            ((Color.GREEN,),),
            ((),),
            ((Color.BLUE,),),
            ((),),
            ((Color.WHITE,),),
            ((),)
        ]
        self.assertEqual(mock_color_wipe.call_count, len(expected_calls))
        mock_color_wipe.assert_has_calls(expected_calls, any_order=False)
