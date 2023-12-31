from dataclasses import dataclass

from .color import Color
from .directions import Direction
from .position import Pos


@dataclass
class RugPos:
    """Egy szőnyeg pozícióját leíró osztály

    A `start` megadja az egyik felének a koordinátáit, a `direction` pedig azt, hogy a
    szőnyeg másik fele ettől milyen irányban van.
    """

    start: Pos
    direction: Direction

    def intersects(self, other: "RugPos") -> bool:
        """Megadja, hogy fedésben van-e egymással a két szőnyeg"""
        # TODO
        raise NotImplementedError
        return False

    def as_tuple(self) -> tuple[Pos, Pos]:
        """Visszaadja a szőnyeg két mezőjének koordinátáit"""
        # TODO
        raise NotImplementedError
        return (self.start, Pos(0, 0))

    @staticmethod
    def from_tuple(positions: tuple[Pos, Pos]) -> "RugPos":
        """Létrehoz egy `RugPos` objektumot a két mező koordinátáiból

        Ha a két mező nem szomszédos, akkor `ValueError` kivételt dob.
        """
        # TODO
        raise NotImplementedError
        return RugPos(positions[0], Direction.UP)

    def __eq__(self, other: object) -> bool:
        """Két `RugPos` objektum akkor egyenlő, ha teljesen fedik egymást"""
        if not isinstance(other, RugPos):
            return False
        tup1 = self.as_tuple()
        tup2 = other.as_tuple()
        if tup1 == tup2:
            return True
        if tup1 == (tup2[1], tup2[0]):
            return True
        return False


@dataclass
class Rug:
    """Egy szőnyeg adatait leíró osztály"""

    pos: RugPos
    color: Color
