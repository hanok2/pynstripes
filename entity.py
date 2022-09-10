import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import copy
from typing import Optional, Tuple, Type, TypeVar, TYPE_CHECKING

from render_order import RenderOrder
from globals import globals

from ai import BaseAI
from fighter import Fighter
if TYPE_CHECKING:
    from game_map import GameMap

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
        render_order: RenderOrder = RenderOrder.CORPSE,
    ) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        self.render_order = render_order
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
        

class Actor(Entity):
    def __init__(
        self,
        *,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        ai_cls: Type[BaseAI],
        fighter: Fighter
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movement=True,
            render_order=RenderOrder.ACTOR,
        )

        self.ai: Optional[BaseAI] = ai_cls(self)

        self.fighter = fighter
        self.fighter.entity = self

    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)


##