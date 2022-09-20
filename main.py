#!/usr/bin/env python3
import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import copy

import tcod
## pip install -r requirements.txt

import color
from engine import Engine
from globals import globals # including globals object
import entity_factories
from input_handler import EventHandler
from procgen import generate_dungeon

# -------------------

def main() -> None:
    screen_width = globals.screen_width
    screen_height= globals.screen_height

    map_width = screen_width-0
    map_height= screen_height-7

    tileset = tcod.tileset.load_tilesheet(
        "16x16-RogueEdit.png", 16, 16, tcod.tileset.CHARMAP_CP437
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

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
    )

    window_height=screen_height*tileset.tile_height
    window_width=screen_width*tileset.tile_width

    root_console = tcod.Console(screen_width, screen_height, order="F")
        
    # sdl_window = tcod.sdl.video.new_window(window_width, window_height,flags=tcod.lib.SDL_WINDOW_RESIZABLE | tcod.lib.SDL_WINDOW_OPENGL, title="Red Planet Rogue")

    # sdl_renderer = tcod.sdl.render.new_renderer(sdl_window, target_textures=True)
        
    # atlas = tcod.render.SDLTilesetAtlas(sdl_renderer, tileset)
    # console_render = tcod.render.SDLConsoleRender(atlas)

    with tcod.context.new(
        width=window_width, height=window_height, tileset=tileset, title = "Red Planet Rogue", vsync=True,
        renderer=tcod.context.RENDERER_SDL2
    ) as context:
        
        while True:
            root_console.clear()
            # engine.event_handler.on_render(console=root_console, sdl_renderer=sdl_renderer, console_render=console_render)
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            # engine.render(console=root_console, sdl_renderer=sdl_renderer, console_render=console_render)

            engine.event_handler.handle_events(context)

    ##
            
# ===========================

if __name__ == "__main__":
    main()

## 