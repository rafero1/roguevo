colors = {
    'dark_wall': (0, 0, 100),
    'dark_ground': (50, 50, 100),
    'light_wall': (130, 110, 50),
    'light_ground': (200, 180, 50),
    'desaturated_green': (63, 127, 63),
    'darker_green': (0, 127, 0),
    'dark_red': (191, 0, 0),
    'crimson': (145, 35, 20),
    'dark_crimson': (100, 25, 10),
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

def getColor(key):
    return colors.get(key)

def getColors():
    return colors
