import math

import kivy
from kivy.graphics import Line
from kivy.graphics import Color
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.logger import Logger

kivy.require('1.10.0')


class HexTile(Widget):
    corners = ListProperty()
    sides = ListProperty()
    wedge_size = NumericProperty()
    rotation_offset = NumericProperty()

    def __init__(self, **kwargs):
        super(HexTile, self).__init__()
        self.debug = kwargs.get('debug', False)
        size = kwargs.get('size', None)
        if size:
            self.size = size
        else:
            self.wedge_size = kwargs.get('wedge_size', 10)
        rotation_offset = kwargs.get('rotation_offset', 0)
        self.rotation_offset = rotation_offset
        center = kwargs.get('center', None)
        if not center:
            center = (self.center_x, self.center_y)
        self.center = center

    @staticmethod
    def calc_tile_width(size, deg):
        deg = deg % 60
        h_rad = math.radians(deg)
        off = math.radians(60)
        max_width = min(size)
        angles = [
            math.fabs(math.cos(h_rad)), math.fabs(math.cos(off - h_rad))
        ]
        return max_width * max(angles)

    @staticmethod
    def calc_tile_height(size, deg):
        deg = deg % 60
        v_rad = math.radians(deg + 60)
        off = math.radians(60)
        max_height = min(size)
        angles = [
            math.fabs(math.sin(v_rad)), math.fabs(math.sin(off - v_rad))
        ]
        return max_height * max(angles)

    @classmethod
    def calc_wedge_size(cls, size, deg):
        return max(cls.calc_tile_width(size, deg),
                   cls.calc_tile_height(size, deg)) / 2

    def update_wedge_size(self):
        self.wedge_size = self.calc_wedge_size(self.size, self.rotation_offset)

    def on_rotation_offset(self, instance, value):
        self.update_wedge_size()
        if not self.center:
            Logger.info('HexTile: on_rotation_offset -- center not set')
            return
        self.populate_corners()

    def on_size(self, instance, value):
        self.update_wedge_size()
        if not self.center:
            Logger.info('HexTile: on_size -- center not set')
            return
        self.populate_corners()

    def on_center(self, instance, value):
        if not self.wedge_size:
            Logger.info('HexTile: on_center -- wedge_size not set')
            return
        self.populate_corners()

    def populate_corners(self):
        corners = []
        for i in range(6):
            angle_deg = 60 * i - self.rotation_offset
            angle_rad = math.pi / 180 * angle_deg
            corner = (self.center_x + self.wedge_size * math.cos(angle_rad),
                      self.center_y + self.wedge_size * math.sin(angle_rad))
            corners.append(corner)
        Logger.info('HexTile: populate_corners -- corners: {}'.format(corners))
        self.corners = corners

    def on_corners(self, instance, value):
        self.populate_sides()

    def populate_sides(self):
        sides = []
        for i in range(6):
            corner_a = self.corners[i]
            corner_b = self.corners[(i + 1) % 6]
            side = (corner_a, corner_b)
            sides.append(side)
        Logger.info('HexTile: populate_sides -- sides: {}'.format(sides))
        self.sides = sides

    def on_sides(self, instance, value):
        self.draw()

    def draw(self):
        with self.canvas:
            self.canvas.clear()
            Color(1, 1, 1)
            Line(points=self.corners+[self.corners[0]], width=1)
            if self.debug:
                # Draw center line
                Line(points=[self.center, self.corners[0]], width=1)
                # Draw bounding box
                box_size = min(self.size) / 2  # Dist from center to orth edge
                box_corners = [
                    (self.center_x - box_size, self.center_y - box_size),
                    (self.center_x + box_size, self.center_y - box_size),
                    (self.center_x + box_size, self.center_y + box_size),
                    (self.center_x - box_size, self.center_y + box_size),
                ]
                Line(points=box_corners + [box_corners[0]], width=1)


if __name__ == '__main__':
    from kivy.app import App

    class HexApp(App):
        def build(self):
            return HexTile(debug=True)

    HexApp().run()
