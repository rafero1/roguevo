# coding=utf-8
import json
import random
import tdl
import sys
from engine import Engine
from input_handlers import handle_keys
from rendering import *
from functions import *
from soul import Soul
from pc import PC

def main():
    screen_width = 80
    screen_height = 60

    tdl.set_font('consolas12x12_gs_tc.png', greyscale=True, altLayout=True)

    root_console = tdl.init(screen_width, screen_height, title='roguevo')
    con = tdl.Console(screen_width, screen_height)

    engine = Engine()
    engine.gen_dungeon(5)

    pc = PC()
    pc.px, pc.py = int(screen_width/2), int(screen_height/2)

    # Console
    while not tdl.event.is_window_closed():
        draw_entity(con, pc)
        root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        for entity in engine.dungeon[engine.current_level].entities:
            draw_entity(con, entity)
            root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        tdl.flush()

        clear_all(con, engine.dungeon[engine.current_level].entities)
        clear_entity(con, pc)

        # Handle keys
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                move_enemies(engine.dungeon[engine.current_level].entities)
                break

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
            pc.move(dx, dy)

        if quit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

if __name__ == '__main__':
    main()
