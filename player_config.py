import configparser
from typing import List


class PlayerConfig:
    def __init__(self, character, start_led_index, end_led_index, name):
        self.character = character
        self.start_led_index = start_led_index
        self.end_led_index = end_led_index
        self.name = name
        self.initiative = None


def read_config(file_path, players: List):
    config = configparser.ConfigParser()
    config.read(file_path)
    player_list = []
    for player in players:
        player_config = config[player]
        player = PlayerConfig(player_config['character'],
                              int(player_config['start_led_index']),
                              int(player_config['end_led_index']),
                              player_config['name'])
        player_list.append(player)
    return player_list
