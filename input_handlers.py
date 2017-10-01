def handle_keys(user_input):
    # Movement
    if user_input.key == 'UP' or user_input.key == 'KP8':
        return {'pmove': (0, -1)}

    elif user_input.key == 'DOWN' or user_input.key == 'KP2':
        return {'pmove': (0, 1)}

    elif user_input.key == 'LEFT' or user_input.key == 'KP4':
        return {'pmove': (-1, 0)}

    elif user_input.key == 'RIGHT' or user_input.key == 'KP6':
        return {'pmove': (1, 0)}

    elif user_input.key == 'KP7':
        return {'pmove': (-1, -1)}

    elif user_input.key == 'KP9':
        return {'pmove': (1, -1)}

    elif user_input.key == 'KP1':
        return {'pmove': (-1, 1)}

    elif user_input.key == 'KP3':
        return {'pmove': (1, 1)}

    elif user_input.key == 'KP5':
        return {'pmove': (0, 0)}

    # Fullscreen (Alt+Enter)
    if user_input.key == 'ENTER' and user_input.alt:
        return {'fullscreen': True}

    # Exit
    elif user_input.key == 'ESCAPE':
        return {'quit': True}

    elif user_input.keychar == 'z':
        return {'upgd_menu': True}

    # If nothing pressed, return nothing
    return {}
