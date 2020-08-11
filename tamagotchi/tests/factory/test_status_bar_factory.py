import pytest

from tamagotchi.factory.status_bar_factory import StatusBarFactory
from tamagotchi.classes.state_bars import HealthBar, EnergyBar
from tamagotchi.classes.coordinate import Coordinate


#from ...factory.status_bar_factory import StatusBarFactory

#from ...classes.state_bars import HealthBar, EnergyBar
#from ...classes.coordinate import Coordinate


class TestStatusBarFactory:

    m_test_coordinate = Coordinate(0,0)

    def test_creating_factory(self):
        status_bar_factory = StatusBarFactory()

        assert isinstance(status_bar_factory, StatusBarFactory)
    
    def test_creating_health(self):
        status_bar_factory = StatusBarFactory()

        health_bar = status_bar_factory.get_status_bar("health", TestStatusBarFactory.m_test_coordinate)

        assert isinstance(health_bar, HealthBar)

    def test_creating_energy(self):
        status_bar_factory = StatusBarFactory()

        energy_bar = status_bar_factory.get_status_bar("energy", TestStatusBarFactory.m_test_coordinate)

        assert isinstance(energy_bar, EnergyBar)
    
    def test_creating_throws(self):
        status_bar_factory = StatusBarFactory()
        with pytest.raises(ValueError):
            no_object = status_bar_factory.get_status_bar("none", TestStatusBarFactory.m_test_coordinate)