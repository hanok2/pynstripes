#!/usr/bin/env python3
import sys
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib')
sys.path.append('C:\\Users\\aavon\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')

import pyglet
from pyglet.graphics import Batch
from pyglet.window import key, mouse

import pyglet_gui
from pyglet_gui.theme import Theme
from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager


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
        self.window = pyglet.window.Window(width=self.init_w, height=self.init_h, resizable=True)
        self.bkgd  = pyglet.resource.image('Flornmoist_Playstation_made_by_Nintendo_console.jpg')
        self.label = pyglet.text.Label(self.label_text, font_name='Courier New', font_size=28,
                                       x=self.window.width//2, y=int(self.window.height*4/5),
                                       anchor_x='center', anchor_y='center')
        self.music = pyglet.resource.media(self.song)

        self.label_theme = Theme({"font": "Lucida Grande", "font_size": 12, "text_color": [255, 0, 0, 255]}, resources_path='')

        self.expression = ""
        self.equation = ""
        self.memory = ""
        self.computed = 0.0
        self.total = 0

        self.label = Label(self.label_text)
        self.batch = Batch()

global g 
g = Globals()


def press(num):
    global g
    g.expression = g.expression + str(num)
    print(g.expression)
    g.equation.set(g.expression)
 
def equalpress():
    global g
    try:
        g.total = str(eval(g.expression))
        g.equation.set(g.total)
        g.expression = ""
    except:
        print("ERROR:\n=========\n" + g.expression)
        g.equation.set(" error ")
        g.expression = ""
  	    
def clear():
    g.expression = ""
    g.equation.set("")
 

@g.window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')
        g.music.play()
        g.playing += 1
        g.count = 1000
    else:
        print('A key was pressed', str(symbol), repr(modifiers))

@g.window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
    else:
        print(str(button), str(x), ",", str(y), " :: ", repr(modifiers))

@g.window.event
def on_draw():
    g.window.clear()
    g.batch.draw()
    g.bkgd.blit(0,0)
    g.label.draw()

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

@g.window.event
def on_resize(width, height):
    g.label = pyglet.text.Label(g.label_text, font_name='Courier New', font_size=28,
                                x=width//2, y=int(height*4/5),
                                anchor_x='center', anchor_y='center')

# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)
mgr = Manager(g.label, window=g.window, theme=g.label_theme, batch=g.batch)

pyglet.app.run()

print(g.title)
pyglet.app.run()

