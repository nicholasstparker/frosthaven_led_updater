class Player:
    def __init__(self, character, start_index, end_index, name, led_controller):
        self.character: str = character
        self.start_index: int = start_index
        self.end_index: int = end_index
        self.name: str = name
        self.led_controller = led_controller
        self.initiative: int or None = None


class Players:
    def __init__(self):
        self.players: dict[str, Player] = dict()

    def __iter__(self):
        return iter(self.players.items())

    def __contains__(self, character: str) -> bool:
        return character in self.players

    def add_player(self, player: Player):
        self.players[player.character] = player

    def get_player(self, player: str) -> Player or None:
        return self.players.get(player, None)

    def get_start_index(self, player: str) -> int:
        return self.players.get(player).start_index

    def get_end_index(self, player: str) -> int:
        return self.players.get(player).end_index
