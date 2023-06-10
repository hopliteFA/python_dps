'The planet factory class'

from pretty_planet import PrettyPlanet
from bland_planet import BlandPlanet
from ugly_planet import UglyPlanet

#class that returns a planet object to the caller
class PlanetFactory:
    @staticmethod
    def get_planet(descriptor):
        if descriptor == 'pretty':
            return PrettyPlanet() 
        if descriptor == "bland":
            return BlandPlanet()
        if descriptor == "ugly":
            return UglyPlanet()
        return None
