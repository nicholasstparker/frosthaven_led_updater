import board
from led_controller import LEDController, Color
from parse_config import parse_config
from stack import Stack
from game_state import GameState
from typing import Dict, Any


class GameStateHandler:
    def __init__(self, settings_file_path: str = "settings.cfg"):
        self.led = LEDController(board.D18, 100)
        self.players, self.dummy_players, self.elements = parse_config(settings_file_path, self.led)
        self.round_state_stack = Stack(0)
        self.prev_round_state = None
        self.led.start_up_sequence()

    def handle(self, json: Dict[str, Any]):
        game_state = GameState(json)
        self.prev_round_state = self.round_state_stack.peek()
        self.round_state_stack.push(game_state.round_state)

        match game_state.round_state:
            case "ROUND_PHASE":
                self.handle_round_phase(game_state)
            case "CARD_SELECTION":
                self.handle_card_selection_phase(game_state)

    def handle_card_selection_phase(self, game_state: GameState):
        bulk_update = True  # True means do not animate. False means animate. Goal is to animate
        # only when switching round states.
        if self.prev_round_state == "ROUND_PHASE":
            self.led.color_wipe()
            bulk_update = False
        game_state.set_initiatives(self.players)
        for player, player_state in self.players:
            match player_state.initiative:
                case 0:
                    player_state.set_player_color(Color.RED)
                case _:
                    player_state.set_player_color(Color.GREEN)
        for dummy_player, dummy_player_state in self.dummy_players:
            dummy_player_state.set_player_color(Color.WHITE)
        for element, element_state in self.elements:
            element_state.set_element_color(element.color)
        self.led.update_led_state_to_future(bulk_update)

    def handle_round_phase(self, game_state: GameState):
        bulk_update = True  # True means do not animate. False means animate. Goal is to animate
        # only when switching round states.
        player = game_state.get_active_player()
        if self.prev_round_state == "CARD_SELECTION":
            self.led.color_wipe()
            bulk_update = False
        if player in self.players:
            self.led.set_future_led_state(0, self.led.num_pixels, Color.WHITE)
            self.players.get_player(player).set_player_color(Color.GREEN)
        else:
            for player, player_state in self.players:
                player_state.set_player_color(Color.WHITE)
            for dummy_player, dummy_player_state in self.dummy_players:
                dummy_player_state.set_player_color(Color.RED)
        for element, element_state in self.elements:
            element_state.set_element_color(element.color)
        self.led.update_led_state_to_future(bulk_update)
