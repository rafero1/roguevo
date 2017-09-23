# coding=utf-8
import json
import random
import tdl
import sys
from engine import Engine
from soul import Soul
from pc import PC

def main():
    screen_width = 80
    screen_height = 60

    tdl.set_font('consolas12x12_gs_tc.png', greyscale=True, altLayout=True)

    root_console = tdl.init(screen_width, screen_height, title='roguevo')

    engine = Engine()
    engine.gen_dungeon(5)

    pc = PC()
    pc.px, pc.py = int(screen_width/2), int(screen_height/2)

    # Console
    while not tdl.event.is_window_closed():
        root_console.draw_char(pc.px, pc.py, pc.tile, bg=None)
        for entity in engine.dungeon[engine.current_level].entities:
            root_console.draw_char(entity.px, entity.py, entity.tile, bg=None)
        tdl.flush()

        # Clean all console positions
        for y in range(screen_height):
            for x in range(screen_width):
                root_console.draw_char(x, y, ' ', bg=None)

        # Handle keys
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                move(engine.dungeon[engine.current_level].entities)
                break

        else:
            user_input = None

        if not user_input:
            continue

        if user_input.key == 'ESCAPE':
            return True
        if user_input.key == 'UP':
            pc.py += -1
        if user_input.key == 'DOWN':
            pc.py += 1
        if user_input.key == 'LEFT':
            pc.px += -1
        if user_input.key == 'RIGHT':
            pc.px += 1

def move(entities):
    for entity in entities:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        entity.px += x
        entity.py += y

if __name__ == '__main__':
    main()
