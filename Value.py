class Value(staticmethod):
    fps_clock = None
    surface = None

    GAME_NAME = "Game"
    MOVE_SPEED = 5
    FPS = 60
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 576

    BLOCK_SIZE = 40
    BLOCK_SIZE_TUPLE = (40, 40)

    BASE_BLOCK_COLOR = (0, 100, 0)
    CORNER_BLOCK_COLOR = (255, 0, 0)
    DOOR_BLOCK_COLOR = (0, 255, 0)

    NORMAL_ACTOR_SIZE_TUPLE = (50, 70)

    is_key_w_down = False
    is_key_s_down = False
    is_key_a_down = False
    is_key_d_down = False

    is_mouse_down = False
    mouse_down_x = 0
    mouse_down_y = 0

    is_move_up = False
    is_move_down = False
    is_move_left = False
    is_move_right = False
