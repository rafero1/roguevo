from logbox import Message
import random


class Combat:
    """
    Combat module for entities. Allows fighting.
    """
    def __init__(self, hp, sp, ar, df, spd, skills):
        self.max_hp = hp
        self.hp = hp
        self.max_sp = sp
        self.sp = sp
        self.ar = ar
        self.df = df
        self.spd = spd
        self.skills = skills

    def attack(self, target):
        skill = self.skills[random.randint(0,len(self.skills)-1)]

        result = []
        damage = max(0, skill.dmg + int(self.ar*0.5) * int(self.spd * 0.3) - target.combat.df)
        if damage > 0:
            kwargs = { 'actor': self.owner.name.capitalize(), 'target': target.name, 'amount': str(damage) }
            result.append({
                'message': Message(skill.message.format(**kwargs))
                })
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
