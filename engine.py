from __future__ import annotations
import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
from typing import TYPE_CHECKING

from tcod.context import Context
from tcod.console import Console

from globals import globals
from tcod.map import compute_fov

from entity import Actor

from input_handler import MainGameEventHandler
from message_log import MessageLog
from render_functions import render_bar



class Engine:
    game_map = None

    def __init__(self, player):
        self.event_handler: MainGameEventHandler = MainGameEventHandler(self)
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                entity.ai.perform()

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console,  
        # sdl_renderer, console_render
    ) -> None:
        self.game_map.render(console)
        self.message_log.render(console=console, x=21, y=45, width=40, height=5)

        render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )
        
        # sdl_renderer.copy(console_render.render(console))
        
        # context.present(console)

        # sdl_renderer.present()

        # console.clear()
    
    

##