def draw_entity(con, entity):
    # Draw entity onto console
    con.draw_char(entity.px, entity.py, entity.tile, entity.color, bg=entity.bg)

def clear_entity(con, entity):
    # Erase the character that represents this object
    con.draw_char(entity.px, entity.py, ' ', entity.color, bg=None)

def render_all(con, entities, root_console, screen_width, screen_height):
    # Draw all entities in the list onto console
    for entity in entities:
        draw_entity(con, entity)

    root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)

def clear_all(con, entities):
    # Clear all entities in the list from console
    for entity in entities:
        clear_entity(con, entity)

def clear_screen(con, screen_width, screen_height):
    # Clean all console positions
    for y in range(screen_height):
        for x in range(screen_width):
            con.draw_char(x, y, ' ', bg=None)
