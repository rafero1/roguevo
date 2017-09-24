import random


def move_enemies(entities, game_map):
    for entity in entities:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        if game_map.walkable[entity.px + x, entity.py + y]:
            entity.move(x, y)
