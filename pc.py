# Player class
from entity import Entity


class PC(Entity):
    """
    Player character class
    """
    def __init__(self, x, y, name, combat):
        super().__init__(x, y, name, combat=combat)
        self.tile = '@'
        self.soulstack = []

    def absorb(self, soul):
        # Add soul to stack
        soulstack.append(soul)

    def enhance(self, weapon):
        # Choose soul -> choose upgrade -> upgrade action
        pass
