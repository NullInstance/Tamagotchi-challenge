import pytest

from tamagotchi.classes.food import Pear, Apple, Strawberry


class TestPear:
    
    def test_name(self):
        pear = Pear()

        assert pear.get_consumable_name() == "Pear"

    def test_value(self):
        pear = Pear()

        assert pear.get_consumable_value() == 40

    def test_weight(self):
        pear = Pear()
        
        assert pear.get_consumable_weight() == 50


class TestApple:
    
    def test_name(self):
        apple = Apple()

        assert apple.get_consumable_name() == "Apple"

    def test_value(self):
        apple = Apple()

        assert apple.get_consumable_value() == 60

    def test_weight(self):
        apple = Apple()
        
        assert apple.get_consumable_weight() == 70


class TestStrawberry:
    
    def test_name(self):
        strawberry = Strawberry()

        assert strawberry.get_consumable_name() == "Strawberry"

    def test_value(self):
        strawberry = Strawberry()

        assert strawberry.get_consumable_value() == 20

    def test_weight(self):
        strawberry = Strawberry()
        
        assert strawberry.get_consumable_weight() == 30