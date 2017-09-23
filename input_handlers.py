def handle_keys(user_input):
    # Movement
    if user_input.key == 'UP':
        return {'pmove': (0, -1)}

    elif user_input.key == 'DOWN':
        return {'pmove': (0, 1)}

    elif user_input.key == 'LEFT':
        return {'pmove': (-1, 0)}

    elif user_input.key == 'RIGHT':
        return {'pmove': (1, 0)}

    # Fullscreen (Alt+Enter)
    if user_input.key == 'ENTER' and user_input.alt:
        return {'fullscreen': True}

    # Exit
    elif user_input.key == 'ESCAPE':
        return {'quit': True}

    # If nothing pressed, return nothing
    return {}
