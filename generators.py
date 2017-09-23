import random


def gen_words(type):
    result = ''
    char_name = ['demonio', 'dragão', 'anjo', 'lagarto', 'goblin', 'kobold', 'ogro', 'troll', 'inseto']
    char_world = ['fogo', 'lampada', 'abismo', 'vila', 'estrela', 'inferno', 'centro', 'fundo', 'caverna', 'golem',
                  'gelo', 'lobo']
    char_adj = ['ancião', 'raivoso', 'nervoso', 'flamejante', 'feroz', 'infernal', 'divino', 'humanoide', 'zumbi',
                'imortal']
    if type == 'name':
        id = random.randint(0, len(char_name) - 1)
        result += char_name[id]
        result += ' '
        id = random.randint(0, len(char_adj) - 1)
        result += char_adj[id]
    elif type == 'world':
        char_id = random.randint(0, len(char_world) - 1)
        result += char_world[char_id]
    return result
