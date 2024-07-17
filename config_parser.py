import configparser
from players import Players, Player
from elements import Elements, Element


def parse_config(file_path="settings.cfg"):
    config = configparser.ConfigParser()
    config.read(file_path)

    players = Players()
    elements = Elements()

    for section in config.sections():
        if section.startswith('Player'):
            player = Player(
                config[section]['character'],
                int(config[section]['start_led_index']),
                int(config[section]['end_led_index']),
                config[section]['name']
            )
            players.add_player(player)
        elif section.startswith('Element'):
            split_colors = config[section]['color'].split(',')
            color = (int(split_colors[0]), int(split_colors[1]), int(split_colors[2]))
            element = Element(
                config[section]['name'],
                int(config[section]['start_led_index']),
                int(config[section]['end_led_index']),
                color
            )
            elements.add_element(element)

    return players, elements
