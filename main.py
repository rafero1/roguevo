# coding=utf-8
import json
import random
import tdl
import sys
from engine import *
from input_handlers import *
from mapping import *
from rendering import *
from functions import *
from logbox import *
from soul import *
from pc import *

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
        'light_wall': (130, 110, 50),
        'light_ground': (200, 180, 50),
        'desaturated_green': (63, 127, 63),
        'darker_green': (0, 127, 0),
        'dark_red': (191, 0, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
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

    tdl.set_font('consolas12x12_gs_tc.png', greyscale=True, altLayout=True)

    root_console = tdl.init(screen_width, screen_height, title='roguevo')
    con = tdl.Console(screen_width, screen_height)
    panel = tdl.Console(screen_width, panel_height)
    game_map =  game_map = GameMap(map_width, map_height)

    engine = Engine()
    engine.gen_dungeon(5)

    pc = PC()
    pc.hp, pc.max_hp = 50, 50

    make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, pc)
    fov_recompute = True
    message_log = MessageLog(message_x, message_width, message_height)
    if starting:
        message_log.add_message(Message('Welcome to Hell'))
        starting = False

    # Console
    while not tdl.event.is_window_closed():
        if fov_recompute:
            game_map.compute_fov(pc.px, pc.py, fov=fov_algorithm, radius=fov_radius, light_walls=fov_light_walls)
        draw_entity(con, pc, game_map.fov)
        root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        render_all(con, panel, engine.dungeon[0].entities, pc, game_map, fov_recompute, root_console, message_log, screen_width, screen_height, bar_width, panel_height, panel_y, colors)
        tdl.flush()

        clear_all(con, engine.dungeon[engine.current_level].entities)
        clear_entity(con, pc)
        fov_recompute = False

        # Handle keys
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                move_enemies(engine.dungeon[engine.current_level].entities, game_map)
                break
            elif event.type == 'MOUSEMOTION':
                mouse_coordinates = event.cell

        # If no input matches KEYDOWN, set user_input to None
        else:
            user_input = None

        # If there is no input, stop checking and go back to start
        if not user_input:
            continue

        action = handle_keys(user_input)
        pmove = action.get('pmove')
        quit = action.get('quit')
        fullscreen = action.get('fullscreen')

        if pmove:
            dx, dy = pmove
            if pc.px + dx < map_width and pc.py + dy < map_height:
                if game_map.walkable[pc.px + dx, pc.py + dy]:
                    pc.move(dx, dy)
                    fov_recompute = True

        if quit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

if __name__ == '__main__':
    main()
