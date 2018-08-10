import kivy
from kivy.config import Config
from kivy.app import App
from kivy.graphics import *
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

kivy.require('1.10.0')
Config.set('graphics', 'window_state', 'maximized')


class GameSquare(Rectangle):

    def __init__(self, pos=(0, 0), size=1, padding=0):
        if padding:
            pos = (pos[0]+padding, pos[1]+padding)
            size = size - padding*2
        super(GameSquare, self).__init__(pos=pos, size=(size, size))


class SquareGrid(Widget):
    def __init__(self, **kwargs):
        super(SquareGrid, self).__init__(**kwargs)
        self.populate_grid()

    def populate_grid(self):
        self.width = Window.width
        self.height = Window.height
        with self.canvas:
            side = 100
            padding = 1
            Logger.info('SquareGrid: width={}, height={}'.format(
                self.width, self.height
            ))
            x = 0
            while x < self.width:
                y = 0
                while y < self.height:
                    Logger.info('SquareGrid: Rectangle at {},{}'.format(x, y))
                    GameSquare(pos=(x, y), size=side, padding=padding)
                    y += side
                x += side


class SquaresApp(App):
    def build(self):
        return SquareGrid()


if __name__ == '__main__':
    SquaresApp().run()
