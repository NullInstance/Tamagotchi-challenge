import pytest

from tamagotchi_tandersen.factory.consumable_factory import ConsumableFactory

from tamagotchi_tandersen.classes.food import Apple, Pear, Strawberry

class TestConsumableFactory:

    def test_creating_factory(self):
        consumable_factory = ConsumableFactory()

        assert isinstance(consumable_factory, ConsumableFactory)
    
    def test_creating_apple(self):
        consumable_factory = ConsumableFactory()

        apple = consumable_factory.get_consumable("apple")

        assert isinstance(apple, Apple)

    def test_creating_pear(self):
        consumable_factory = ConsumableFactory()

        pear = consumable_factory.get_consumable("pear")

        assert isinstance(pear, Pear)
    
    def test_creating_strawberry(self):
        consumable_factory = ConsumableFactory()

        strawberry = consumable_factory.get_consumable("strawberry")

        assert isinstance(strawberry, Strawberry)
    
    def test_creating_throws(self):
        consumable_factory = ConsumableFactory()
        with pytest.raises(ValueError):
            no_object = consumable_factory.get_consumable("none")