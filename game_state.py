class GameState:
    def __init__(self, json):
        self.round_state: str = "CARD_SELECTION" if json["roundState"] == 0 else "ROUND_PHASE"
        self.character_states = list(json["currentList"])

    def get_active_player(self) -> str:
        for item in self.character_states:
            if item['turnState'] == 1:
                character = item["id"]
                return character

    def set_initiatives(self, players):
        for item in self.character_states:
            initiative = None
            state = item.get("characterState", None)
            if state:
                initiative = state.get("initiative", None)
            if initiative is not None:
                character = item["id"]
                players.get_player(character).initiative = initiative
