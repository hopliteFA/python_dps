from abc import abstractmethod #prompted to import this by vscode when I added the @ decorator
#from abc import ABCMeta #added b/c he did, not sure why - next video explains

class IPlanet:
    @staticmethod
    @abstractmethod
    def print_color():
        'interface, abstact method' 
