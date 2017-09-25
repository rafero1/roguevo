from logbox import Message
import random


def move_enemies(entities, game_map, message_log, player):
    for entity in entities:
        dx = random.randint(-1,1)
        dy = random.randint(-1,1)
        fx = entity.px + dx
        fy = entity.py + dy
        if game_map.walkable[fx, fy]:
            target = get_entites_at(entities, fx, fy)
            if target:
                pass

            elif fx == player.px and fy == player.py:
                target = player
                entity.attack(target)
                message_log.add_message(Message(entity.name+' attacks '+ target.name+ ' for'+ ' zero'+ ' damage'))

            else:
                entity.move(dx, dy)

def get_entites_at(entities, x, y):
    for entity in entities:
        if entity.px == x and entity.py == y:
            return entity
    else:
        return None
