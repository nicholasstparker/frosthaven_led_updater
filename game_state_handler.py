import board
from led_controller import LEDController
from stack import Stack
from game_state import GameState
from config_parser import parse_config


class GameStateHandler:
    def __init__(self):
        self.led = LEDController(board.D18, 100)
        self.players, self.elements = parse_config()
        self.round_state_stack = Stack(0)
        self.prev_round_state = None

    def handle(self, json):
        game_state = GameState(json, self.elements)
        self.prev_round_state = self.round_state_stack.peek()
        self.round_state_stack.push(game_state.round_state)

        match game_state.round_state:
            case "ROUND_PHASE":
                self.handle_round_phase(game_state)
            case "CARD_SELECTION":
                self.handle_card_selection_phase(game_state)

    def handle_card_selection_phase(self, game_state):
        if self.prev_round_state == "ROUND_PHASE":
            self.led.first_card_selection_round()
        else:
            self.led.set_color_in_range(31, 51, (255, 255, 255))
            self.led.set_color_in_range(82, 100, (255, 255, 255))

            game_state.set_initiatives(self.players)

            for player, player_state in self.players:
                if player_state.initiative != 0:
                    self.led.set_color_in_range(player_state.start_index, player_state.end_index, (0, 255, 0))
                else:
                    self.led.set_color_in_range(player_state.start_index, player_state.end_index, (255, 0, 0))

    def handle_round_phase(self, game_state):
        player = game_state.get_active_player()

        if self.prev_round_state == "CARD_SELECTION":
            self.led.color_wipe()
            if player in self.players:
                start_index = self.players.get_start_index(player)
                end_index = self.players.get_end_index(player)
                self.led.set_color_in_range(0, start_index, (255, 255, 255), bulk_update=False)
                self.led.set_color_in_range(start_index, end_index, (0, 255, 0), bulk_update=False)
                self.led.set_color_in_range(end_index, 100, (255, 255, 255), bulk_update=False)
            else:
                self.led.set_color_in_range(0, 31, (255, 255, 255), bulk_update=False)
                self.led.set_color_in_range(31, 51, (255, 0, 0), bulk_update=False)
                self.led.set_color_in_range(31, 82, (255, 255, 255), bulk_update=False)
                self.led.set_color_in_range(82, 100, (255, 0, 0), bulk_update=False)
        else:
            self.led.set_all_colors((255, 255, 255))

            if player in self.players:
                start_index = self.players.get_start_index(player)
                end_index = self.players.get_end_index(player)
                self.led.set_color_in_range(start_index, end_index, (0, 255, 0))
            else:
                self.led.set_color_in_range(31, 51, (255, 0, 0))
                self.led.set_color_in_range(82, 100, (255, 0, 0))

