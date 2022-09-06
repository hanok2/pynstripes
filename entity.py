from typing import Tuple
from globals import globals

class Entity:
    '''
    A generic object to represent players, enemies, items, etc.
    '''
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the Entity by a given amount
        
        self.x += dx
        self.y += dy
        


##