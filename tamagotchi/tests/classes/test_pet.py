import pytest

from tamagotchi.classes.pet import Pet
from tamagotchi.classes.coordinate import Coordinate

from tamagotchi.enums.actor_state import ActorState
from tamagotchi.enums.age import Age

from tamagotchi.abstract.consumable import Consumable


class ExampleFood(Consumable):
    def __init__(self):
        return

    def get_consumable_value(self) -> int:
        return 10

    def get_consumable_name(self) -> str:
        return "ExampleFood"

    def get_consumable_weight(self):
        return 10

    def draw(self, p_game_screen, p_x_coordinate, p_y_coordinate):
        return


class TestPet:

    def test_creating_pet(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        assert pet.max_health == 100
        assert pet.get_position() == (x_coordinate, y_coordinate)

    def test_pet_is_alive(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        assert pet.is_alive() == True

    def test_pet_is_not_alive(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.set_state(ActorState.DEAD)

        assert pet.is_alive() == False
    
    def test_pet_is_doing_action(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.set_state(ActorState.EATING)

        assert pet.is_doing_action() == True
    
    def test_pet_is_not_doing_action(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.set_state(ActorState.AWAKE)

        assert pet.is_doing_action() == False

    def test_pet_awake(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.set_state(ActorState.ASLEEP)

        assert pet.get_state() == ActorState.ASLEEP

        pet.awake()

        assert pet.get_state() == ActorState.AWAKE

    def test_pet_run_die_hunger(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.health = 0

        pet.run_turn()

        assert pet.is_alive() == False

    def test_pet_run_die_age(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.age = 100

        pet.run_turn()

        assert pet.is_alive() == False

    def test_pet_run_poop(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.fullness = 70

        pet.run_turn()

        assert pet.get_state() == ActorState.POOPING

    def test_pet_run_sleeping(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        pet.energy = 10

        pet.run_turn()

        assert pet.get_state() == ActorState.ASLEEP

    def test_pet_eating_max_health(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        example_food = ExampleFood()

        pet.eat(example_food)

        assert pet.fullness == example_food.get_consumable_weight()
        assert pet.get_health() == pet.max_health

    def test_pet_eating_low_health(self):
        frames_per_second, x_coordinate, y_coordinate = 30, 0, 0

        pet = Pet(frames_per_second, Coordinate(x_coordinate, y_coordinate))

        new_health = 10
        pet.health = new_health

        example_food = ExampleFood()

        pet.eat(example_food)

        assert pet.fullness == example_food.get_consumable_weight()
        assert pet.get_health() == ExampleFood().get_consumable_value() + new_health