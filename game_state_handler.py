import board
from led_controller import LEDController
from player import read_config_and_parse_players
from stack import Stack
from game_state import GameState


class GameStateHandler:
    def __init__(self):
        self.led_controller = LEDController(board.D18, 100)
        self.players = read_config_and_parse_players()
        self.round_state_stack = Stack(0)
        self.prev_round_state = None

    def handle(self, json):
        game_state = GameState(json)
        self.prev_round_state = self.round_state_stack.peek()
        self.round_state_stack.push(game_state.round_state)

        match game_state.round_state:
            case "ROUND_PHASE":
                self.handle_round_phase(game_state)
            case "CARD_SELECTION":
                self.handle_card_selection_phase(game_state)

    def handle_card_selection_phase(self, game_state):
        if self.prev_round_state == "ROUND_PHASE":
            self.led_controller.color_wipe()
            self.led_controller.set_color_in_range(0, 31, (255, 0, 0), bulk_update=False)
            self.led_controller.set_color_in_range(31, 51, (255, 255, 255), bulk_update=False)
            self.led_controller.set_color_in_range(51, 82, (255, 0, 0), bulk_update=False)
            self.led_controller.set_color_in_range(82, 100, (255, 255, 255), bulk_update=False)
        else:
            self.led_controller.set_color_in_range(31, 51, (255, 255, 255))
            self.led_controller.set_color_in_range(82, 100, (255, 255, 255))

            game_state.set_initiatives(self.players)

            for player, player_state in self.players:
                if player_state.initiative != 0:
                    self.led_controller.set_color_in_range(player_state.start_index,
                                                           player_state.end_index,
                                                           (0, 255, 0))
                else:
                    self.led_controller.set_color_in_range(player_state.start_index,
                                                           player_state.end_index,
                                                           (255, 0, 0))

    def handle_round_phase(self, game_state):
        player = game_state.get_active_player()

        if self.prev_round_state == "CARD_SELECTION":
            self.led_controller.color_wipe()
            if player in self.players:
                self.led_controller.set_color_in_range(0, self.players.get_player(player).start_index,
                                                       (255, 255, 255), bulk_update=False)
                self.led_controller.set_color_in_range(self.players.get_player(player).start_index,
                                                       self.players.get_player(player).end_index,
                                                       (0, 255, 0), bulk_update=False)
                self.led_controller.set_color_in_range(self.players.get_player(player).end_index, 100,
                                                       (255, 255, 255), bulk_update=False)
            else:
                self.led_controller.set_color_in_range(0, 31, (255, 255, 255), bulk_update=False)
                self.led_controller.set_color_in_range(31, 51, (255, 0, 0), bulk_update=False)
                self.led_controller.set_color_in_range(31, 82, (255, 255, 255), bulk_update=False)
                self.led_controller.set_color_in_range(82, 100, (255, 0, 0), bulk_update=False)
        else:
            self.led_controller.set_all_colors((255, 255, 255))

            if player in self.players:
                self.led_controller.set_color_in_range(self.players.get_player(player).start_index,
                                                       self.players.get_player(player).end_index,
                                                       (0, 255, 0))
            else:
                self.led_controller.set_color_in_range(31, 51, (255, 0, 0))
                self.led_controller.set_color_in_range(82, 100, (255, 0, 0))

