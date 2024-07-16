import configparser


class Player:
    def __init__(self, character, start_index, end_index, name):
        self.character: str = character
        self.start_index: int = start_index
        self.end_index: int = end_index
        self.name: str = name
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


def read_config_and_parse_players() -> Players:
    config = configparser.ConfigParser()
    config.read('settings.cfg')
    player_list = ["Player1", "Player2", "Player3", "Player4"]
    players = Players()
    for player in player_list:
        player_config = config[player]
        player = Player(player_config['character'],
                        int(player_config['start_led_index']),
                        int(player_config['end_led_index']),
                        player_config['name'])
        players.add_player(player)
    return players
