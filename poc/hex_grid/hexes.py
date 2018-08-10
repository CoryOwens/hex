import math

import kivy
from kivy.app import App
from kivy.config import Config
from kivy.graphics import Line
from kivy.graphics import Color
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.logger import Logger

kivy.require('1.10.0')
Config.set('graphics', 'window_state', 'maximized')


class HexGrid(GridLayout):
    hex_tile = ObjectProperty()

    def __init__(self):
        super(HexGrid, self).__init__()

    def on_size(self, instance, value):
        self.populate_tiles()

    def populate_tiles(self):
        if not self.hex_tile:
            self.hex_tile = HexTile(center=self.center)
            self.add_widget(self.hex_tile)
        else:
            self.hex_tile.center = self.center


class HexesApp(App):
    def build(self):
        return HexGrid()


if __name__ == '__main__':
    HexesApp().run()
