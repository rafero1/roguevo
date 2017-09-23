class Entity:
    """
    Entity class for player and creatures
    """
    def __init__(self):
        self.name = ''
        self.lvl = 0
        self.xp = 0
        self.hp = 0
        self.sp = 0
        self.ar = 0
        self.df = 0
        self.spd = 0
        self.skills = []

        self.tile = 'Z'
        self.color = (255, 255, 255)
        self.bg = None
        self.px = 0
        self.py = 0

    def move(self, dx, dy):
        self.px += dx
        self.py += dy

    def attack(self, target, skill):
        # Choose skill -> choose target.
        pass
