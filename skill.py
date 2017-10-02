from logbox import Message


class Skill():
    """
    Skill class
    """
    def __init__(self, name, dmg, cost, message, atype='direct'):
        self.name = name
        self.attackType = atype
        self.dmg = dmg
        self.cost = cost
        self.cooldown = 0
        self.time = 0
        self.message = message
        self.requires = []

skilltree = {
    'punch': Skill('Punch', 10, 0, '{actor} punches {target} dealing {amount} damage!'),
    'kick': Skill('Kick', 16, 5, '{actor} kicks {target} dealing {amount} damage!'),
    'scratch': Skill('Scratch', 12, 1, '{actor} claws {target} dealing {amount} damage!'),
}

def getSkill(key):
    return skilltree.get(key)

def getSkills():
    return skilltree
