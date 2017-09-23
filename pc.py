# Player class
from entity import Entity


class PC(Entity):
    """
    Player character class
    """
    def __init__(self):
        super().__init__()
        self.tile = '@'
        self.soulstack = []

    def absorb(self, soul):
        # Add soul to stack
        soulstack.append(soul)

    def enhance(self, weapon):
        # Choose soul -> choose upgrade -> upgrade action
        pass
