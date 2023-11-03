from game_state import GameState
from player import Player
from rug import Direction, Pos, RotationDirection, RugPos


class Agent:
    def __init__(self, player: Player, game_state: GameState):
        """Inicializálja az ügynököt"""
        self.player = player
        self.game_state = game_state

    def decide_rotation(self) -> RotationDirection:
        """Eldönti, hogy a figura melyik irányba forduljon"""
        # TODO
        return RotationDirection.NONE

    def decide_rug_placement(self) -> RugPos:
        """Eldönti, hogy hova rakja le a szőnyeget"""
        # TODO
        return RugPos(Pos(0, 0), Direction.UP)
