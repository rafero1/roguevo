

class Basic:
    def act(self, target, game_map, entities):
        result = []
        if game_map.fov[self.owner.px, self.owner.py]:
            if self.owner.distance_to(target) >= 2:
                self.owner.move_towards(target.px, target.py, game_map, entities)

            elif target.combat.hp > 0:
                result.extend(self.owner.combat.attack(target))
        return result
