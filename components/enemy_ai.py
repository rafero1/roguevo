import random


class Basic:
    def act(self, target, game_map, entities):
        actor = self.owner
        result = []

        if game_map.fov[actor.px, actor.py]:
            if actor.distance_to(target) >= 2:
                actor.move_towards(target.px, target.py, game_map, entities)

            elif target.combat.hp > 0:
                skill = actor.combat.skills[random.randint(0,len(actor.combat.skills)-1)]
                result.extend(actor.combat.attack(target, skill))
        return result
