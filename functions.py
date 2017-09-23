import random


def move_enemies(entities):
    for entity in entities:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        entity.move(x, y)
