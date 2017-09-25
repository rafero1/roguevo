# Player class
from entity import Entity


class PC(Entity):
    """
    Player character class
    """
    def __init__(self):
        super().__init__()
        self.is_pc = True
        self.name = 'Player'
        self.tile = '@'
        self.soulstack = []
        self.max_hp, self.hp = 50, 50
        self.max_sp, self.sp = 50, 50
        self.ar = 10
        self.df = 10
        self.spd = 5

    def absorb(self, soul):
        # Add soul to stack
        soulstack.append(soul)

    def enhance(self, weapon):
        # Choose soul -> choose upgrade -> upgrade action
        pass
