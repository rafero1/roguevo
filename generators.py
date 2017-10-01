import random


def gen_words(type):
    result = ''
    char_name = ['demon', 'dragon', 'engel', 'lizard', 'goblin', 'kobold', 'ogre', 'troll', 'insect']
    char_world = ['fire', 'lampada', 'abismo', 'vila', 'estrela', 'inferno', 'centro', 'fundo', 'caverna', 'golem',
                  'gelo', 'lobo']
    char_adj = ['ancient', 'ravenous', 'berserked', 'blazing', 'wild', 'infernal', 'divine', 'humanoid', 'undead',
                'immortal']
    if type == 'name':
        id = random.randint(0, len(char_adj) - 1)
        result += char_adj[id]
        result += ' '
        id = random.randint(0, len(char_name) - 1)
        result += char_name[id]
    elif type == 'world':
        char_id = random.randint(0, len(char_world) - 1)
        result += char_world[char_id]
    return result
