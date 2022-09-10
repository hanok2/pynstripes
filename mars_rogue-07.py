#!/usr/bin/env python3
import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import copy

import tcod
## pip install -r requirements.txt

from engine import Engine
from globals import globals # including globals object
import entity_factories
from input_handler import EventHandler
from procgen import generate_dungeon

# -------------------

def main() -> None:
    screen_width = globals.screen_width
    screen_height= globals.screen_height

    map_width = 80
    map_height= 45

    tileset = tcod.tileset.load_tilesheet(
        "16x16_ascii-charset.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    # game_map = GameMap(map_width, map_height)
    engine.game_map = generate_dungeon(
        max_rooms=globals.max_rooms,
        room_min_size=globals.room_min_size,
        room_max_size=globals.room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=globals.max_monsters_per_room,
        engine=engine
    )
    engine.update_fov()

    with tcod.context.new_terminal(
        screen_width, screen_height, 
        tileset=tileset,
        title = "Mars Rogue", vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            engine.event_handler.handle_events()

            
# ===========================

if __name__ == "__main__":
    main()

## 