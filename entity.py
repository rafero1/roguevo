class Entity:
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

        self.tile = '@'
        self.color = 0
        self.bgcolor = 0
        self.px = 0
        self.py = 0

        def attack(self, target, skill):
            # Escolher abilidade -> atacar alvo.
            pass
