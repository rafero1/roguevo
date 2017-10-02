from enum import Enum, auto


class State(Enum):
    """
    Controls game state
    """
    PLAYER_TURN = auto()
    ENEMY_TURN = auto()
    PLAYER_DEAD = auto()
    PMENU_OPEN = auto()
