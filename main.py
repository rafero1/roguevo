# coding=utf-8
import json
import random
import tdl
import sys
from components.combat import *
from components.enemy_ai import *
from game_states import *
from engine import *
from input_handlers import *
from mapping import *
from rendering import *
from functions import *
from logbox import *
from soul import *
from pc import *
import colors

def main():
    starting = True
    mouse_coordinates = (0, 0)
    screen_width = 80
    screen_height = 60
    bar_width = 20
    panel_height = 15
    panel_y = screen_height - panel_height
    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1
    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 'BASIC'
    fov_light_walls = True
    fov_radius = 10

    colors = {
        'dark_wall': (0, 0, 100),
        'dark_ground': (50, 50, 100),
        'light_wall': (130, 110, 150),
        'light_ground': (200, 180, 150),
        'desaturated_green': (63, 127, 63),
        'darker_green': (0, 127, 0),
        'dark_red': (191, 0, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'lighter_black': (25, 25, 25),
        'red': (255, 0, 0),
        'orange': (255, 127, 0),
        'light_red': (255, 114, 114),
        'darker_red': (127, 0, 0),
        'violet': (127, 0, 255),
        'yellow': (255, 255, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'light_cyan': (114, 255, 255),
        'light_pink': (255, 114, 184)
    }

    # TDL init
    tdl.set_font('consolas12x12_gs_tc.png', greyscale=True, altLayout=True)
    root_console = tdl.init(screen_width, screen_height, title='roguevo')

    # Gameplay screen
    con = tdl.Console(screen_width, screen_height)

    # UI Panel
    panel = tdl.Console(screen_width, panel_height)

    # TODO: Change later. GameMap object and Engine Object
    game_map =  game_map = GameMap(map_width, map_height)
    Game = Engine()
    Game.gen_dungeon(5)
    entities = []

    # Player init
    pc_combatant = Combat(hp=25, sp=25, ar=5, df=10, spd=10)
    pc = PC(1, 1, 'Player', combat=pc_combatant)

    # TODO: Include Player at first. Change Later
    # Game.dungeon[0].entities.append(pc)
    entities.append(pc)

    state = State.PLAYER_TURN

    Game.dungeon[0].rooms = make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, pc)
    Game.dungeon[0].populate()
    fov_recompute = True
    message_log = MessageLog(message_x, message_width, message_height)
    if starting:
        message_log.add_message(Message('Welcome to Hell'))
        starting = False

    # TODO: Change later. Easy access for entity list
    for entity in Game.dungeon[0].entities:
        entities.append(entity)
        print(entity.tile, entity.name, entity.px, entity.py)

    # Draw
    while not tdl.event.is_window_closed():
        # Recompute Field of View when necessary
        if fov_recompute:
            game_map.compute_fov(pc.px, pc.py, fov=fov_algorithm, radius=fov_radius, light_walls=fov_light_walls)

        # Render everything on screen
        render_all(con, panel, entities, pc, game_map, fov_recompute, root_console, message_log, screen_width, screen_height, bar_width, panel_height, panel_y, colors)
        tdl.flush()

        # Clear all entities previous locations. Prevents ghost images
        clear_all(con, entities, pc)

        fov_recompute = False

        # Handle events
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                break
            elif event.type == 'MOUSEMOTION':
                mouse_coordinates = event.cell

        # If no input matches KEYDOWN, set user_input to None
        else:
            user_input = None

        # If there is no input, stop checking and go back to start
        if not user_input:
            continue

        # Input actions
        action = handle_keys(user_input)
        pmove = action.get('pmove')
        quit = action.get('quit')
        fullscreen = action.get('fullscreen')
        player_turn_results = []

        # Player movement
        if pmove and state == State.PLAYER_TURN:
            dx, dy = pmove
            fx = pc.px + dx
            fy = pc.py + dy
            if fx < map_width and fy < map_height:
                if game_map.walkable[fx, fy]:
                    target = get_blocking_entities_at(entities, fx, fy)
                    if target:
                        attack_results = pc.combat.attack(target)
                        player_turn_results.extend(attack_results)
                    else:
                        pc.move(dx, dy)
                        fov_recompute = True
                    state = State.ENEMY_TURN

        if quit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

        for player_turn_result in player_turn_results:
            message = player_turn_result.get('message')
            dead_entity = player_turn_result.get('dead')

            if message:
                message_log.add_message(message)

            if dead_entity:
                if dead_entity == pc:
                    message = kill_player(dead_entity)
                    state = State.PLAYER_DEAD

                else:
                    message = kill_monster(dead_entity)
                message_log.add_message(message)

        if state == State.ENEMY_TURN:
            for entity in entities:
                if entity.ai:
                    enemy_turn_results = entity.ai.act(pc, game_map, entities)
                    for enemy_turn_result in enemy_turn_results:
                        message = enemy_turn_result.get('message')
                        dead_entity = enemy_turn_result.get('dead')

                        if message:
                            message_log.add_message(message)

                        if dead_entity:
                            if dead_entity == pc:
                                message = kill_player(dead_entity)
                                state = State.PLAYER_DEAD

                            else:
                                message = kill_monster(dead_entity)

                            message_log.add_message(message)

                            if state == State.PLAYER_DEAD:
                                break

                    if state == State.PLAYER_DEAD:
                        break
            else:
                state = State.PLAYER_TURN

if __name__ == '__main__':
    main()
