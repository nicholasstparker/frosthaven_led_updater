import configparser
from players import Players, Player


def parse_config(file_path="settings.cfg") -> Players:
    config = configparser.ConfigParser()
    config.read(file_path)

    players = Players()

    for section in config.sections():
        if section.startswith('Player'):
            player = Player(
                config[section]['character'],
                int(config[section]['start_led_index']),
                int(config[section]['end_led_index']),
                config[section]['name']
            )
            players.add_player(player)

    return players
