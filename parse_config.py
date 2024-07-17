import configparser
from typing import Tuple
from elements import Elements, Element
from players import Players, Player
from led_controller import LEDController


def parse_config(file_path: str, led_controller: LEDController) -> Tuple[Players, Players, Elements]:
    """
    Parses a configuration file to create and return two collections of players: actual players and
    dummy players.

    The configuration file should contain sections starting with 'Player' or 'DummyPlayer', each
        representing a player with properties such as character, start_led_index, end_led_index,
        and name. These properties are used to instantiate Player objects which are then added to
        the respective Players collection.

    Args:
        file_path (str): The path to the configuration file to be parsed. led_controller
        (LEDController): An instance of LEDController to be associated with each player.

    Returns:
        Tuple[Players, Players]: A tuple containing two Players instances. The first one contains
            actual players, and the second one contains dummy players.
    """
    config = configparser.ConfigParser()
    config.read(file_path)

    players = Players()
    dummy_players = Players()
    elements = Elements()

    for section in config.sections():
        if section.startswith('Player') or section.startswith('DummyPlayer'):
            player = Player(
                config[section]['character'],
                int(config[section]['start_led_index']),
                int(config[section]['end_led_index']),
                config[section]['name'],
                led_controller
                )
            if section.startswith('Player'):
                players.add_player(player)
            elif section.startswith('DummyPlayer'):
                dummy_players.add_player(player)
        elif section.startswith('Element'):
            color = config[section]['color'].split(',')
            element = Element(
                config[section]['name'],
                int(config[section]['start_led_index']),
                int(config[section]['end_led_index']),
                (int(color[0]), int(color[1]), int(color[2])),
                led_controller
            )
            elements.add_element(element)

    return players, dummy_players, elements
