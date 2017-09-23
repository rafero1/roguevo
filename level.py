import random
from creature import Creature
from generators import gen_words


class Level:
    """
    Dungeon level class
    """
    ID = 0
    def __init__(self, name):
        Level.ID += 1
        self.id = Level.ID
        self.name = name
        self.active = False
        self.cleared = False
        self.entities = []

    def populate(self, num):
        amount = random.randint(2, num)
        for number in range(amount):
            name = gen_words('name')
            beast = Creature(name)
            beast.px = random.randint(0, 80)
            beast.py = random.randint(0, 60)
            self.entities.append(beast)
