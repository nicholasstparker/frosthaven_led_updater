class GameState:
    def __init__(self, json):
        self.round_state = json["roundState"]
        self.character_states = list(json["currentList"])

    def get_active_character(self) -> str:
        for item in self.character_states:
            if item['turnState'] == 1:
                character = item["id"]
                return character
