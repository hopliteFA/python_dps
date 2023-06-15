
"Implements the IPlanet interface and is the product class for pretty"

from planet_interface import IPlanet

class PrettyPlanet(IPlanet): #extends the IPlanet interface
    def __init__(self):
        self.color = "blue"

    def print_color(self):
        return f"I am a {self.color} planet."