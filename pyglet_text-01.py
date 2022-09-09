#!/usr/bin/env python3
import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')

import pyglet
from pyglet.window import key, mouse

class Globals:
    def __init__(self) -> None:
        self.label_text = 'Hello, Melissa, my Lovie!'
        self.init_w = 960
        self.init_h = 960
        self.title = "Pynstriped Pyglet Demo"
        self.song = 'Lyre Le Temps - Clock Is Mine.mp3'
        self.playing = 0
        self.count = 0
        self.count_text = ''

g = Globals()

window = pyglet.window.Window(width=g.init_w, height=g.init_h)
bkgd  = pyglet.resource.image('Flornmoist_Playstation_made_by_Nintendo_console.jpg')
label = pyglet.text.Label(g.label_text, font_name='Courier New', font_size=28,
                          x=window.width//2, y=window.height-180,
                          anchor_x='center', anchor_y='center')
music = pyglet.resource.media(g.song)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')
        music.play()
        g.playing += 1
        g.count = 1000
    else:
        print('A key was pressed', str(symbol), repr(modifiers))

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
    else:
        print(str(button), str(x), ",", str(y), " :: ", repr(modifiers))

@window.event
def on_draw():
    window.clear()
    bkgd.blit(0,0)
    label.draw()

    if g.count > 0:
        print(g.playing)
        g.count -= 10
        if g.count > 900:
            g.count_text = 'Lyre '
            print(g.count_text)
        elif g.count > 800:
            g.count_text = 'Lyre Le '
            print(g.count_text)
        elif g.count > 700:
            g.count_text = 'Lyre Le Temps '
            print(g.count_text)
        elif g.count > 600:
            g.count_text = 'Le Temps - The '
            print(g.count_text)
        elif g.count > 500:
            g.count_text = 'Temps - The Clock '
            print(g.count_text)
        elif g.count > 600:
            g.count_text = '- The Clock Is'
            print(g.count_text)
        elif g.count > 0:
            g.count_text = 'The Clock Is Mine'
            print(g.count_text)
        elif g.count <= 0:
            g.count = 0


# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

print(g.title)
pyglet.app.run()

