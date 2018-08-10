import math
from unittest import TestCase

from poc.hex_grid.hex import HexTile


class TestHex(TestCase):

    def test_calc_tile_width_flat(self):
        exp = 4
        size = (4, 4)
        rot = 0
        act = HexTile.calc_tile_width(size, rot)
        self.assertEqual(exp, act)

    def test_calc_tile_width_point(self):
        exp = 2 * math.sqrt(3)
        size = (4, 4)
        rot = 30
        act = HexTile.calc_tile_width(size, rot)
        self.assertAlmostEqual(exp, act)

    def test_calc_tile_height_flat(self):
        exp = 2 * math.sqrt(3)
        size = (4, 4)
        rot = 0
        act = HexTile.calc_tile_height(size, rot)
        self.assertAlmostEqual(exp, act)

    def test_calc_tile_height_point(self):
        exp = 4
        size = (4, 4)
        rot = 30
        act = HexTile.calc_tile_height(size, rot)
        self.assertEqual(exp, act)

    def test_calc_wedge_size_flat(self):
        exp = 1
        size = (2, 2)
        rot = 0
        act = HexTile.calc_wedge_size(size, rot)
        self.assertEqual(exp, act)

    def test_calc_wedge_size_flat_60(self):
        exp = 1
        size = (2, 2)
        rot = 60
        act = HexTile.calc_wedge_size(size, rot)
        self.assertEqual(exp, act)

    def test_calc_wedge_size_flat_120(self):
        exp = 1
        size = (2, 2)
        rot = 120
        act = HexTile.calc_wedge_size(size, rot)
        self.assertEqual(exp, act)

    def test_calc_wedge_size_point(self):
        exp = 1
        size = (2, 2)
        rot = 30
        act = HexTile.calc_wedge_size(size, rot)
        self.assertEqual(exp, act)

    def test_calc_wedge_size_point_90(self):
        exp = 1
        size = (2, 2)
        rot = 90
        act = HexTile.calc_wedge_size(size, rot)
        self.assertEqual(exp, act)

    def test_calc_wedge_size_flat_rect(self):
        exp = 1
        size = (2, 4)
        rot = 0
        act = HexTile.calc_wedge_size(size, rot)
        self.assertEqual(exp, act)

    def test_calc_wedge_size_point_rect(self):
        exp = 1
        size = (2, 4)
        rot = 30
        act = HexTile.calc_wedge_size(size, rot)
        self.assertEqual(exp, act)
