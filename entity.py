class Entity:
    """
    Entity class for player and creatures
    """
    def __init__(self):
        self.name = ''
        self.max_hp = 10
        self.hp = self.max_hp
        self.max_sp = 10
        self.sp = self.max_sp
        self.ar = 0
        self.df = 0
        self.spd = 0
        self.skills = []

        self.tile = '?'
        self.color = (255, 255, 255)
        self.bg = None
        self.px = 0
        self.py = 0

    def move(self, dx, dy):
        self.px += dx
        self.py += dy

    def manage():
        if self.hp <= 0:
            self.death()

    def attack(self, target):
        # Choose skill -> choose target.
        damage = max(0, self.ar - target.df)
        return damage

    def take_hit():
        pass

    def death():
        pass
