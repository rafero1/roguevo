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
        self.rooms = []

    def populate(self, min=0, max=5):
        amount = random.randint(min, max)
        for room in self.rooms:
            for number in range(amount):
                name = gen_words('name')
                color = (random.randint(15, 255), random.randint(15, 255), random.randint(15, 255))
                beast = Creature(name)
                beast.color = color
                beast.hp = random.randint(5,20)
                beast.max_hp = beast.hp
                beast.sp = random.randint(5,20)
                beast.max_sp = beast.sp
                beast.ar = random.randint(2,25)
                beast.df = random.randint(2,25)
                beast.spd = random.randint(2,25)
                beast.px = random.randint(room.x1 + 1, room.x2 - 1)
                beast.py = random.randint(room.y1 + 1, room.y2 - 1)
                self.entities.append(beast)
