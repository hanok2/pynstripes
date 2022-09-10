import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import copy
from typing import Optional, Tuple, TypeVar, TYPE_CHECKING

from globals import globals

# from game_map import GameMap

T = TypeVar("T", bound="Entity")



class Entity:
    '''
    A generic object to represent players, enemies, items, etc.
    '''

    gamemap = None

    def __init__(
        self, 
        gamemap = None,
        x: int = 0, 
        y: int = 0, 
        char: str = "?", 
        color: Tuple[int, int, int] = (255, 0, 0),
        name: str = "<Unnamed>",
        blocks_movement: bool = False,
    ) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            # If gamemap isn't provided now then we will set it later.
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self, gamemap, x:int, y:int):
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap=None) -> None:
        """Place this entity at a new location.  Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            # modified like berzerk...
            if self.gamemap:
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx: int, dy: int) -> None:
        # Move the Entity by a given amount
        
        self.x += dx
        self.y += dy
        


##