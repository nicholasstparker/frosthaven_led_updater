import board
from led_controller import LEDController
from player import read_config
from stack import Stack
from game_state import GameState


class GameStateHandler:
    def __init__(self):
        self.led_controller = LEDController(board.D18, 100)
        config_file_path = 'settings.cfg'
        player_list = read_config(config_file_path, ["Player1", "Player2", "Player3", "Player4"])
        self.players = {
            player_list[0].character: player_list[0],
            player_list[1].character: player_list[1],
            player_list[2].character: player_list[2],
            player_list[3].character: player_list[3]
        }
        self.round_state_stack = Stack(0)
        self.prev_round_state = None

    def handle(self, json):
        game_state = GameState(json)
        self.prev_round_state = self.round_state_stack.peek()
        self.round_state_stack.push(game_state.round_state)

        match game_state.round_state:
            case 1:
                self.handle_round_ready(game_state)
            case 0:
                self.handle_round_not_ready(game_state)

    def handle_round_not_ready(self, game_state):
        if self.prev_round_state == 1:
            self.led_controller.color_wipe()
            self.led_controller.set_color_in_range(0, 31, (255, 0, 0), bulk_update=False)
            self.led_controller.set_color_in_range(31, 51, (255, 255, 255), bulk_update=False)
            self.led_controller.set_color_in_range(51, 82, (255, 0, 0), bulk_update=False)
            self.led_controller.set_color_in_range(82, 100, (255, 255, 255), bulk_update=False)
        else:
            self.led_controller.set_color_in_range(31, 51, (255, 255, 255))
            self.led_controller.set_color_in_range(82, 100, (255, 255, 255))

            game_state.handle_initiatives(self.players)

            for character, character_state in self.players.items():
                if character_state.initiative != 0:
                    self.led_controller.set_color_in_range(character_state.start_led_index,
                                                           character_state.end_led_index,
                                                           (0, 255, 0))
                else:
                    self.led_controller.set_color_in_range(character_state.start_led_index,
                                                           character_state.end_led_index,
                                                           (255, 0, 0))

    def handle_round_ready(self, game_state):
        character = game_state.get_active_character()

        if self.prev_round_state == 0:
            self.led_controller.color_wipe()
            if character in self.players:
                self.led_controller.set_color_in_range(0, self.players[character].start_led_index,
                                                       (255, 255, 255), bulk_update=False)
                self.led_controller.set_color_in_range(self.players[character].start_led_index,
                                                       self.players[character].end_led_index,
                                                       (0, 255, 0), bulk_update=False)
                self.led_controller.set_color_in_range(self.players[character].end_led_index, 100,
                                                       (255, 255, 255), bulk_update=False)
            else:
                self.led_controller.set_color_in_range(0, 31, (255, 255, 255), bulk_update=False)
                self.led_controller.set_color_in_range(31, 51, (255, 0, 0), bulk_update=False)
                self.led_controller.set_color_in_range(31, 82, (255, 255, 255), bulk_update=False)
                self.led_controller.set_color_in_range(82, 100, (255, 0, 0), bulk_update=False)
        else:
            self.led_controller.set_all_colors((255, 255, 255))

            if character in self.players:
                self.led_controller.set_color_in_range(self.players[character].start_led_index,
                                                       self.players[character].end_led_index,
                                                       (0, 255, 0))
            else:
                self.led_controller.set_color_in_range(31, 51, (255, 0, 0))
                self.led_controller.set_color_in_range(82, 100, (255, 0, 0))

