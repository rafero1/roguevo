# Engine class
import random
from creature import Creature
from generators import gen_words
from level import Level


class Engine():
    """
    Handle game variables and functions.
    """

    first_time = False
    done = False
    dungeon = []
    current_level = 0

    def gen_dungeon(self, levels):
        for amount in range(levels):
            name = gen_words('world')
            self.dungeon.append(Level(name))
            if amount == 0:
                self.dungeon[0].active = True
                self.dungeon[0].populate(12)

    def manage_dungeon(self):
        num = 0
        for place in self.world:
            if place.active:
                self.current_level = num
                if len(self.creatures) <= 0:
                    place.cleared = True
                    print('O labirinto de', place.name, 'foi completamente conquistado!')
            num += 1

    def move_to(self, t):
        for level in self.dungeon:
            if level.active:
                level.active = False
        t.active = True
        t.populate(12)

    def advance(self):
        c = 0
        for level in self.dungeon:
            if level.active:
                level.active = False
                self.dungeon[c + 1].active = True
                self.dungeon[c + 1].populate(12)
                break
            c += 1
