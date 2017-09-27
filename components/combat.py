from logbox import Message


class Combat:
    """
    Combat module for entities. Allows fighting.
    """
    def __init__(self, hp, sp, ar, df, spd):
        self.max_hp = hp
        self.hp = hp
        self.max_sp = sp
        self.sp = sp
        self.ar = ar
        self.df = df
        self.spd = spd
        self.skills = []

    def attack(self, target):
        result = []
        damage = max(0, self.ar * int(self.spd * 0.3) - target.combat.df)
        if damage > 0:
            result.append({'message': Message('{0} strikes at {1} dealing {2} damage!'.format(self.owner.name.capitalize(), target.name, str(damage)))})
            result.extend(target.combat.take_hit(damage))
        else:
            result.append({'message': Message('{0} tries to attack {1} but the damage is mitigated'.format(self.owner.name.capitalize(), target.name))})
        return result

    def take_hit(self, value):
        result = []
        self.hp -= value
        if self.hp <= 0:
            result.append({'dead': self.owner})
        return result
