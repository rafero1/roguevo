# coding=utf-8
"""
    TODO: Progression system
    TODO: Multiple dungeon levels
    TODO: Custom dungeon generation algorithmn
    TODO: Skill Window
    TODO: Combat Revamp
"""
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
from skill import *
from colors import getColors

def main():

    Game = Engine()
    colors = getColors()

    show_upgd_menu = False

    # TDL init
    tdl.set_font(Game.font, greyscale=Game.greyscale, altLayout=Game.altLayout)
    root_console = tdl.init(Game.screen_width, Game.screen_height, title=Game.title)

    # Gameplay screen
    con = tdl.Console(Game.screen_width, Game.screen_height)

    # UI Panel
    panel = tdl.Console(Game.screen_width, Game.panel_height)

    # Upgrade Screen
    upgd = tdl.Console(Game.screen_width, Game.panel_height)

    # TODO: Change later. GameMap object and Engine Object
    game_map = GameMap(Game.map_width, Game.map_height)

    Game.gen_dungeon(5)
    entities = []

    # Player init
    pskills = [getSkill('punch'), getSkill('kick'), getSkill('scratch')]
    pc_combatant = Combat(hp=500, sp=100, ar=15, df=10, spd=15, skills=pskills)
    pc = PC(1, 1, 'Player', combat=pc_combatant)

    # TODO: Include Player at first. Change Later
    # Game.dungeon[0].entities.append(pc)
    entities.append(pc)

    state = State.PLAYER_TURN

    Game.dungeon[0].rooms = make_map(game_map, Game.max_rooms, Game.room_min_size, Game.room_max_size, Game.map_width, Game.map_height, pc)
    Game.dungeon[0].populate(1,2)
    fov_recompute = True
    message_log = MessageLog(Game.message_x, Game.message_width, Game.message_height)
    if Game.starting:
        message_log.add_message(Message('Welcome to Hell'))
        Game.starting = False

    # TODO: Change later. Easy access for entity list
    for entity in Game.dungeon[0].entities:
        entities.append(entity)
        print(entity.tile, entity.name, entity.px, entity.py)

    # Draw
    while not tdl.event.is_window_closed():
        # Recompute Field of View when necessary
        if fov_recompute:
            game_map.compute_fov(pc.px, pc.py, fov=Game.fov_algorithm, radius=Game.fov_radius, light_walls=Game.fov_light_walls)

        # Render everything on screen
        render_all(con, panel, entities, pc, game_map, fov_recompute, root_console, message_log, Game, colors)
        # -------------------------------


        if show_upgd_menu:
            upgd.clear(fg=colors.get('white'), bg=colors.get('black'))
            upgd.draw_str(1, 1, 'Status')

            upgd.draw_str(1, 4, pc.name)

            y = 8
            for skill in pc.combat.skills:
                upgd.draw_str(1, y, skill.name)
                y += 1
            root_console.blit(upgd, 0, 0, Game.screen_width, Game.screen_height, 0, 0)

        # -------------------------------
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
                Game.mouse_coordinates = event.cell

        # If no input matches KEYDOWN, set user_input to None
        else:
            user_input = None

        # If there is no input, continue checking. This means the game only continues if there's user input (Keypress).
        if not user_input:
            continue

        # Input actions

        action = handle_keys(user_input)
        pmove = action.get('pmove')
        quit = action.get('quit')
        fullscreen = action.get('fullscreen')
        upgd_menu = action.get('upgd_menu')

        # Varible to hold results from player turn
        player_turn_results = []

        # Player movement and controls
        if pmove and state == State.PLAYER_TURN and not show_upgd_menu:
            dx, dy = pmove
            fx = pc.px + dx
            fy = pc.py + dy
            if fx < Game.map_width and fy < Game.map_height:
                if game_map.walkable[fx, fy]:
                    target = get_blocking_entities_at(entities, fx, fy)
                    if target and target is not pc:
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

        if upgd_menu:
            show_upgd_menu = not show_upgd_menu

        # Handle results form player turn
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

        # Handle enemy turn
        if state == State.ENEMY_TURN and not show_upgd_menu:
            for entity in entities:
                # Enemies act
                if entity.ai:
                    enemy_turn_results = entity.ai.act(pc, game_map, entities)

                    # Handle results
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
