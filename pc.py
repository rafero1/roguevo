# Player class
from entity import Entity


class PC(Entity):
    """
    Player character class
    """
    def __init__(self, x, y, name, combat):
        super().__init__(x, y, name, combat=combat)
        self.tile = '@'
        # self.soulstack = []
        self.soulstack = 0
        self.render_order = 0

    def absorb(self, s):
        # Add soul to stack
        # self.soulstack.append(s)
        self.soulstack += s

    def enhance(self, weapon):
        # Choose soul -> choose upgrade -> upgrade action
        pass
