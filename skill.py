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
    'punch': Skill('punch', 10, 0, Message(''))
}

def getSkill(key):
    return skilltree.get(key)

def getSkills():
    return skilltree
