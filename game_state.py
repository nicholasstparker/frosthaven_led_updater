from elements import Elements
from typing import List, Dict


class GameState:
    def __init__(self, json, elements):
        self.round_state: str = "CARD_SELECTION" if json["roundState"] == 0 else "ROUND_PHASE"
        self.character_states: List[Dict] = list(json["currentList"])
        self.elements: Elements = self.set_element_state(json["elementState"], elements)

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

    @staticmethod
    def set_element_state(json, elements: Elements) -> Elements:
        for k, v in json.items():
            match k:
                case "0":
                    match v:
                        case 0:
                            elements.get_element("Fire").state = "FULL"
                        case 1:
                            elements.get_element("Fire").state = "WANING"
                        case 2:
                            elements.get_element("Fire").state = "DEAD"
                case "1":
                    match v:
                        case 0:
                            elements.get_element("Ice").state = "FULL"
                        case 1:
                            elements.get_element("Ice").state = "WANING"
                        case 2:
                            elements.get_element("Ice").state = "DEAD"
                case "2":
                    match v:
                        case 0:
                            elements.get_element("Air").state = "FULL"
                        case 1:
                            elements.get_element("Air").state = "WANING"
                        case 2:
                            elements.get_element("Air").state = "DEAD"
                case "3":
                    match v:
                        case 0:
                            elements.get_element("Earth").state = "FULL"
                        case 1:
                            elements.get_element("Earth").state = "WANING"
                        case 2:
                            elements.get_element("Earth").state = "DEAD"
                case "4":
                    match v:
                        case 0:
                            elements.get_element("Light").state = "FULL"
                        case 1:
                            elements.get_element("Light").state = "WANING"
                        case 2:
                            elements.get_element("Light").state = "DEAD"
                case "5":
                    match v:
                        case 0:
                            elements.get_element("Dark").state = "FULL"
                        case 1:
                            elements.get_element("Dark").state = "WANING"
                        case 2:
                            elements.get_element("Dark").state = "DEAD"
        return elements
