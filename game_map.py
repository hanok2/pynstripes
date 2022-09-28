from typing import Iterable, Iterator, Optional, TYPE_CHECKING

import numpy as np  # type: ignore
import tcod
from tcod.console import Console
from PIL import Image

from entity import Actor
import tile_types

from entity import Entity

from globals import *


class GameMap:
    def __init__(self, engine, width: int, height: int, entities: Iterable[Entity] = ()):
        self.engine = engine
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")  # Tiles the player can now see
        self.explored = np.full((width, height), fill_value=False, order="F")  # Tiles the player has seen before

    @property
    def actors(self) -> Iterator[Actor]:
        """Iterate over this maps living actors."""
        yield from (
            entity
            for entity in self.entities
            if isinstance(entity, Actor) and entity.is_alive
        )

    def get_blocking_entity_at_location(self, location_x: int, location_y: int) -> Optional[Entity]:
        for entity in self.entities:
            if (
                    entity.blocks_movement
                    and entity.x == location_x
                    and entity.y == location_y
            ):
                return entity

        return None

    def get_actor_at_location(self, x: int, y: int) -> Optional[Actor]:
        for actor in self.actors:
            if actor.x == x and actor.y == y:
                return actor

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".

        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
        """
        console.tiles_rgb[0: self.width, 0: self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD,
        )

        entities_sorted_for_rendering = sorted(
            self.entities, key=lambda x: x.render_order.value
        )

        img_temp = Image.open("1bit_imitate/LOTR/tiles/tiles31.png")
        img_temp = img_temp.convert("RGB")
        # console.draw_semigraphics(pixels=img_temp, x=entity.x, y=entity.y)

        for entity in entities_sorted_for_rendering:
            # Only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                # test out some features here...

                # Used to be: console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)

                if entity.char == '@':
                    console.put_char(x=entity.x, y=entity.y, ch=tcod.tileset.CHARMAP_CP437[18])
                elif entity.char == 'S':
                    console.put_char(x=entity.x, y=entity.y, ch=9829)
                elif entity.char == 'D':
                    console.put_char(x=entity.x, y=entity.y, ch=9830)
                elif entity.char == 'W':
                    console.put_char(x=entity.x, y=entity.y, ch=9827)
                else:
                    console.put_char(x=entity.x, y=entity.y, ch=tcod.tileset.CHARMAP_CP437[15])

        ##

##
