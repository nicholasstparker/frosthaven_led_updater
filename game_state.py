class GameState:
    def __init__(self, json):
        self.round_state = json["roundState"]
        self.character_states = list(json["currentList"])
