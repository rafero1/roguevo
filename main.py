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
        'light_wall': (130, 110, 50),
        'light_ground': (200, 180, 50),
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

    tdl.set_font('consolas12x12_gs_tc.png', greyscale=True, altLayout=True)

    root_console = tdl.init(screen_width, screen_height, title='roguevo')
    con = tdl.Console(screen_width, screen_height)
    panel = tdl.Console(screen_width, panel_height)
    game_map =  game_map = GameMap(map_width, map_height)

    Game = Engine()
    Game.gen_dungeon(5)

    pc = PC()

    Game.dungeon[0].rooms = make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, pc)
    Game.dungeon[0].populate()
    fov_recompute = True
    message_log = MessageLog(message_x, message_width, message_height)
    if starting:
        message_log.add_message(Message('Welcome to Hell'))
        starting = False

    # Draw
    while not tdl.event.is_window_closed():
        # Recompute Field of View when necessary
        if fov_recompute:
            game_map.compute_fov(pc.px, pc.py, fov=fov_algorithm, radius=fov_radius, light_walls=fov_light_walls)

        # Render everything on screen
        render_all(con, panel, Game.dungeon[0].entities, pc, game_map, fov_recompute, root_console, message_log, screen_width, screen_height, bar_width, panel_height, panel_y, colors)
        tdl.flush()

        # Clear all entities previous locations. Prevents ghost images
        clear_all(con, Game.dungeon[0].entities, pc)

        fov_recompute = False

        # Handle events
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                move_enemies(Game.dungeon[Game.current_level].entities, game_map)
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

        # Player movement
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
