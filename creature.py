import random
from entity import Entity
from soul import Soul
from generators import gen_words


class Creature(Entity):
    def __init__(self, x, y, name, combat, ai):
        super().__init__(x, y, name, combat=combat, ai=ai)
        self.rank = 0
        self.race = ''
        # self.soulv = self.gen_soul()
        self.soulv = 1

    def gen_soul(self):
        return Soul(self.name+ " soul")
