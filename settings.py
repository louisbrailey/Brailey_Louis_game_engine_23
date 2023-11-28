# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.9
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (100, 25, 0)
BLUE = (110, 2, 105)

GROUND = (0, HEIGHT - 50, WIDTH, 40, "normal")

PLATFORM_LIST = [
    (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, "normal"),
    (125, HEIGHT - 350, 100, 20, "moving"),
    (222, 200, 100, 20, "normal"),
    (175, 100, 50, 20, "normal")
]