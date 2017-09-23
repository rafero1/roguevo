# coding=utf-8
import json
import random
import tdl
import sys
from engine import Engine
from input_handlers import handle_keys
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
        con.draw_char(pc.px, pc.py, pc.tile, bg=None)
        root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        for entity in engine.dungeon[engine.current_level].entities:
            con.draw_char(entity.px, entity.py, entity.tile, bg=None)
            root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        tdl.flush()

        # Clean all console positions
        for y in range(screen_height):
            for x in range(screen_width):
                con.draw_char(x, y, ' ', bg=None)

        # Handle keys
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                move(engine.dungeon[engine.current_level].entities)
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
            pc.px += dx
            pc.py += dy

        if quit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

def move(entities):
    for entity in entities:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        entity.px += x
        entity.py += y

if __name__ == '__main__':
    main()
