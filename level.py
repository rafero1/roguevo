import random
from creature import Creature
from components.combat import *
from components.enemy_ai import *
from skill import *
from generators import gen_words


class Level:
    """
    Dungeon level class
    TODO: Should probably have the game_map
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

    def populate(self, min=0, max=10):
        for room in self.rooms:
            amount = random.randint(min, max)
            for number in range(amount):
                x = random.randint(room.x1 + 1, room.x2 - 1)
                y = random.randint(room.y1 + 1, room.y2 - 1)
                if not any([entity for entity in self.entities if entity.px == x and entity.py == y]):
                    name = gen_words('name')
                    color = (random.randint(25, 235), random.randint(25, 235), random.randint(25, 235))
                    hp = random.randint(300,1000)
                    sp = random.randint(70,300)
                    ar = random.randint(10,10)
                    df = random.randint(5,25)
                    spd = random.randint(5,35)
                    mskills = [getSkill('punch'), getSkill('kick'), getSkill('scratch')]
                    combat_component = Combat(hp=hp, sp=sp, ar=ar, df=df, spd=spd, skills=mskills)
                    ai_component = Basic()
                    beast = Creature(x, y, name, combat=combat_component, ai=ai_component)
                    beast.color = color
                    self.entities.append(beast)
