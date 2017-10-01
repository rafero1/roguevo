import math
from functions import *


class Entity:
    """
    Entity class for player and creatures
    """
    def __init__(self, x, y, name, stopper=True, combat=None, ai=None):
        self.name = name
        self.tile = name[:1].upper()
        self.color = (255, 255, 255)
        self.bg = None
        self.stopper = stopper
        self.px = x
        self.py = y
        self.render_order = 1

        self.combat = combat
        self.ai = ai

        if self.combat:
            self.combat.owner = self

        if self.ai:
            self.ai.owner = self

    def move(self, dx, dy):
        self.px += dx
        self.py += dy

    def move_towards(self, target_x, target_y, game_map, entities):
        path = game_map.compute_path(self.px, self.py, target_x, target_y)

        dx = path[0][0] - self.px
        dy = path[0][1] - self.py

        if game_map.walkable[path[0][0], path[0][1]] and not get_blocking_entities_at(entities, self.px + dx, self.py + dy):
            self.move(dx, dy)

    def distance_to(self, other):
        dx = other.px - self.px
        dy = other.py - self.py
        return math.sqrt(dx ** 2 + dy ** 2)
