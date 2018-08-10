import kivy
from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout

from poc.hex_grid.hex import HexTile

kivy.require('1.10.0')


class HexGrid(GridLayout):
    hex_tiles = ListProperty()
    tile_size = NumericProperty()
    tile_rotation = NumericProperty()

    def __init__(self, **kwargs):
        super(HexGrid, self).__init__()
        tile_size = kwargs.get('tile_size', (10, 10))
        if tile_size[0] != tile_size[1]:
            tile_size = min(tile_size[0], tile_size[1])
        self.tile_size = tile_size

        self.tile_rotation = kwargs.get('tile_rotation', 0)

    def on_center(self, instance, value):
        self.populate_tiles()

    def on_size(self, instance, value):
        self.populate_tiles()

    def get_tile_width(self):
        return HexTile.calc_tile_width(self.tile_size, self.tile_rotation)

    def populate_tiles(self):
        if not self.hex_tile:
            self.hex_tiles = []
            self.add_widget(self.hex_tile)
        else:

            self.hex_tiles.clear()
            x = 0
            while x < self.width + self.tile_size:
                y = 0
                while y < self.height + self.tile_size:
                    tile = HexTile(center=(x, y), size=self.tile_size)
                    self.hex_tiles.append(tile)
                    y +=

            self.hex_tile.center = self.center
            self.hex_tile.size = self.size


if __name__ == '__main__':
    from kivy.app import App

    class HexGridApp(App):
        def build(self):
            return HexGrid()

    HexGridApp().run()
