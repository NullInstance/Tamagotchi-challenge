import pytest

from tamagotchi_tandersen.classes.food_inventory import FoodInventory
from tamagotchi_tandersen.classes.coordinate import Coordinate

from tamagotchi_tandersen.abstract.consumable import Consumable

class ExampleFood(Consumable):
    def __init__(self):
        return

    def get_consumable_value(self) -> int:
        return 0

    def get_consumable_name(self) -> str:
        return "ExampleFood"

    def get_consumable_weight(self):
        return 0

    def draw(self, p_game_screen, p_x_coordinate, p_y_coordinate):
        return

class ExampleFoodTwo(Consumable):
    def __init__(self):
        return

    def get_consumable_value(self) -> int:
        return 10

    def get_consumable_name(self) -> str:
        return "ExampleFoodTwo"
    
    def get_consumable_weight(self):
        return 10

    def draw(self, p_game_screen, p_x_coordinate, p_y_coordinate):
        return

class TestFoodInventory:

    def test_creating_empty_inventory(self):
        food_list = FoodInventory([], Coordinate(0,0))

        assert len(food_list.food_list) is 0

    def test_creating_non_empty_inventory(self):
        food_list = FoodInventory([ExampleFood()], Coordinate(0,0))

        assert len(food_list.food_list) is 1
    
    def test_eat_food(self):
        food_list = FoodInventory([ExampleFood()], Coordinate(0,0))

        food_to_eat = food_list.eat_food()

        print(food_to_eat)

        assert len(food_list.food_list) is 0
        assert food_to_eat.get_consumable_name() == "ExampleFood"

    def test_eat_empty_food_list(self):
        food_list = FoodInventory([], Coordinate(0,0))

        food_to_eat = food_list.eat_food()

        assert food_to_eat is None

    def test_add_food(self):
        food_list = FoodInventory([], Coordinate(0,0))

        food_list.add_food(ExampleFood())

        assert len(food_list.food_list) is 1

    def test_add_multiple_same_food(self):
        food_list = FoodInventory([], Coordinate(0,0))

        food_list.add_food(ExampleFood())
        food_list.add_food(ExampleFood())

        assert len(food_list.food_list) is 2

        assert len(food_list.get_available_food()) is 1

        assert food_list.get_available_food()["ExampleFood"] is 2

    def test_add_multiple_different_food(self):
        food_list = FoodInventory([], Coordinate(0,0))

        food_list.add_food(ExampleFood())
        food_list.add_food(ExampleFoodTwo())

        assert len(food_list.food_list) is 2

        assert len(food_list.get_available_food()) is 2