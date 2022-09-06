#from html import entities
import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import tcod
## pip install -r requirements.txt

from engine import Engine
from entity import * # including globals object
#from actions import EscapeAction, MovementAction
from game_map import GameMap
from input_handler import EventHandler

# -------------------

def main() -> None:
    screen_width = globals.screen_width
    screen_height= globals.screen_height

    map_width = 80
    map_height= 45

    tileset = tcod.tileset.load_tilesheet(
        "16x16_ascii-charset.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    event_handler = EventHandler()

    player = Entity(x=int(screen_width/2), y=int(screen_height/2), char="@", color=(255,255,255))
    npc = Entity(x=int(screen_width/2 - 5), y=int(screen_height/2), char="@", color=(255,255,0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width, screen_height, 
        tileset=tileset,
        title = "Mars Rogue", vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            #root_console.print(x=player_x, y=player_y, string="@")
            #root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            engine.render(console=root_console, context=context)

            #context.present(root_console) # Important if you want things to display at all!
            events = tcod.event.wait()
            engine.handle_events(events)
            #root_console.clear()

            
# ===========================

if __name__ == "__main__":
    main()

## 