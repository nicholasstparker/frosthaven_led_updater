from typing import Tuple, Iterator
from led_controller import LEDController


class Player:
    def __init__(self, character, start_index, end_index, name, led: LEDController):
        self.character: str = character
        self.start_index: int = start_index
        self.end_index: int = end_index
        self.name: str = name
        self.led = led
        self.initiative: int or None = None

    def set_player_color(self, color: tuple[int, int, int]):
        self.led.set_future_led_state(self.start_index, self.end_index, color)


class Players:
    def __init__(self):
        self.players: dict[str, Player] = dict()

    def __iter__(self) -> Iterator[Tuple[str, Player]]:
        return iter(self.players.items())

    def __contains__(self, character: str) -> bool:
        return character in self.players

    def add_player(self, player: Player):
        self.players[player.character] = player

    def get_player(self, player: str) -> Player or None:
        return self.players.get(player, None)
