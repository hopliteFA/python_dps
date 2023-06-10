from planet_factory import PlanetFactory

#I want to create a planet.  
#invoke the class and have it create the planet for us

saturn = PlanetFactory.get_planet("pretty")
print(saturn.print_color())