import board
from led_controller import LEDController, Color
from parse_config import parse_config
from typing import Dict, Any, List
from elements import Elements


class GameStateHandler:
    def __init__(self, settings_file_path: str = "settings.cfg"):
        self.led = LEDController(board.D18, 100)
        self.players, self.dummy_players, self.elements = parse_config(settings_file_path, self.led)
        self.round_state_stack = Stack(0)
        self.prev_round_state = None
        self.led.start_up_sequence()

    def handle(self, json: Dict[str, Any]):
        game_state = GameState(json, self.elements)
        self.prev_round_state = self.round_state_stack.peek()
        self.round_state_stack.push(game_state.round_state)

        match game_state.round_state:
            case "ROUND_PHASE":
                self.handle_round_phase(game_state)
            case "CARD_SELECTION":
                self.handle_card_selection_phase(game_state)

    def handle_card_selection_phase(self, game_state):
        bulk_update = True  # True means do not animate. False means animate. Goal is to animate
        # only when switching round states.
        if self.prev_round_state == "ROUND_PHASE":
            self.led.color_wipe()
            bulk_update = False
        game_state.set_initiatives(self.players)
        for player, player_state in self.players:
            match player_state.initiative:
                case 0:
                    player_state.set_player_color(Color.RED)
                case _:
                    player_state.set_player_color(Color.GREEN)
        for dummy_player, dummy_player_state in self.dummy_players:
            dummy_player_state.set_player_color(Color.WHITE)
        self.elements.set_all_element_colors()
        self.led.update_led_state_to_future(bulk_update)

    def handle_round_phase(self, game_state):
        bulk_update = True  # True means do not animate. False means animate. Goal is to animate
        # only when switching round states.
        player = game_state.get_active_player()
        if self.prev_round_state == "CARD_SELECTION":
            self.led.color_wipe()
            bulk_update = False

        if player in self.players:
            for player_, player_state_ in self.players:
                if player_ != player:
                    player_state_.set_player_color(Color.WHITE)
            self.players.get_player(player).set_player_color(Color.GREEN)
            for dummy_player, dummy_player_state in self.dummy_players:
                dummy_player_state.set_player_color(Color.WHITE)

        else:
            for player, player_state in self.players:
                player_state.set_player_color(Color.WHITE)
            for dummy_player, dummy_player_state in self.dummy_players:
                dummy_player_state.set_player_color(Color.RED)
        self.elements.set_all_element_colors()
        self.led.update_led_state_to_future(bulk_update)


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


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if not self.top:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def peek(self):
        return self.top.value
