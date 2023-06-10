from planet_interface import IPlanet

class UglyPlanet(IPlanet): #extends the IPlanet interface
    def __init__(self):
        self.color = "gray"

    def print_color(self):
        return f"I am a {self.color} planet."

