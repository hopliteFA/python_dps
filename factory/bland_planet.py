from planet_interface import IPlanet

class BlandPlanet(IPlanet): #extends the IPlanet interface
    def __init__(self):
        self.color = "brown"

    def print_color(self):
        return f"I am a {self.color} planet."
