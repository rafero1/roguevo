def draw_entity(con, entity, fov):
    # Draw entity onto console
    if fov[entity.px, entity.py]:
        con.draw_char(entity.px, entity.py, entity.tile, entity.color, bg=entity.bg)

def clear_entity(con, entity):
    # Erase the character that represents this object
    con.draw_char(entity.px, entity.py, ' ', entity.color, bg=None)

# Get names of entities at mouse location if they're visible
def get_names_under_mouse(mouse_coordinates, entities, game_map):
    x, y = mouse_coordinates

    names = [entity.name for entity in entities
             if entity.px == x and entity.py == y and game_map.fov[entity.px, entity.py]]
    names = ', '.join(names)

    return names.capitalize()

def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color, string_color):
    # Render a bar (HP, experience, etc). first calculate the width of the bar
    bar_width = int(float(value) / maximum * total_width)

    # Render the background first
    panel.draw_rect(x, y, total_width, 1, None, bg=back_color)

    # Now render the bar on top
    if bar_width > 0:
        panel.draw_rect(x, y, bar_width, 1, None, bg=bar_color)

    # Text and values
    text = name + ': ' + str(value) + '/' + str(maximum)
    x_centered = x + int((total_width-len(text)) / 2)

    panel.draw_str(x_centered, y, text, fg=string_color, bg=None)

def render_all(con, panel, entities, player, game_map, fov_recompute, root_console, message_log, engine, colors):
    screen_width = engine.screen_width
    screen_height = engine.screen_height
    bar_width = engine.bar_width
    panel_height = engine.panel_height
    panel_y = engine.panel_y
    mouse_coordinates = engine.mouse_coordinates
    # Draw map tiles
    if fov_recompute:
        for x, y in game_map:
            wall = not game_map.transparent[x, y]

            if game_map.fov[x, y]:
                if wall:
                    con.draw_char(x, y, None, fg=None, bg=colors.get('crimson'))
                else:
                    con.draw_char(x, y, None, fg=None, bg=colors.get('dark_crimson'))

                game_map.explored[x][y] = True

            # If area was seen, draw this way
            elif game_map.explored[x][y]:
                if wall:
                    con.draw_char(x, y, None, fg=None, bg=colors.get('dark_wall'))
                else:
                    con.draw_char(x, y, None, fg=None, bg=colors.get('dark_ground'))

    # Draw all entities in the list onto console
    # draw_entity(con, player, game_map.fov)
    sorted_entities = sorted(entities, key=lambda x: x.render_order, reverse=True)
    for entity in sorted_entities:
        draw_entity(con, entity, game_map.fov)

    root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
    panel.clear(fg=colors.get('white'), bg=colors.get('black'))

    # Print the game messages, one line at a time
    y = 1
    for message in message_log.messages:
        panel.draw_str(message_log.x, y, message.text, bg=None, fg=message.color)
        y += 1

    render_bar(panel, 1, 1, bar_width, 'HP', player.combat.hp, player.combat.max_hp,
               colors.get('light_red'), colors.get('darker_red'), colors.get('white'))
    render_bar(panel, 1, 2, bar_width, 'SP', player.combat.sp, player.combat.max_sp, colors.get('light_cyan'), colors.get('blue'), colors.get('black'))

    # Entities names
    mx, my = mouse_coordinates
    panel.draw_str(1, 0, get_names_under_mouse(mouse_coordinates, entities, game_map))

    root_console.blit(panel, 0, panel_y, screen_width, panel_height, 0, 0)

def clear_all(con, entities, player):
    # Clear all entities in the list from console
    for entity in entities:
        clear_entity(con, entity)
    # clear_entity(con, player)

def clear_screen(con, screen_width, screen_height):
    # Clean all console positions
    for y in range(screen_height):
        for x in range(screen_width):
            con.draw_char(x, y, ' ', bg=None)
