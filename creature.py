import random
from entity import Entity
from soul import Soul
from generators import gen_words


class Creature(Entity):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.tile = name[:1].upper()
        self.rank = 0
        self.race = ''
        self.gen_stats()
        self.soul = ''

    def gen_stats(self):
        self.name = gen_words('name')
        self.hp = random.randint(30, 50)
        self.ar = random.randint(5, 20)

    def die(self, player):
        print(self.name, 'morreu')
        player.soulstack.append(self.soul)
        print('got', self.name,"'s soul")
