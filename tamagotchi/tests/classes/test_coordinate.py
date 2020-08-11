import pytest

from tamagotchi.classes.coordinate import Coordinate


class TestCoordinate:

    def test_create_coordinate(self):
        coordinate = Coordinate(0, 0)

        assert isinstance(coordinate, Coordinate)
        assert coordinate.x_position == 0
        assert coordinate.y_position == 0
    
    def test_coordinate_get_x(self):
        coordinate = Coordinate(10, 0)

        assert coordinate.get_x() == 10
    
    def test_coordinate_get_y(self):
        coordinate = Coordinate(0, 10)

        assert coordinate.get_y() == 10
    
    def test_coordinate_get_coordinate(self):
        coordinate = Coordinate(10, 20)

        assert coordinate.get_coordinate() == (10, 20)