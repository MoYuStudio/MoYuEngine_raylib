
import pyray as raylib

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def main():
    raylib.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "MoYuEngine")

    while not raylib.window_should_close():

        if raylib.is_key_pressed(raylib.KEY_SPACE):
            print('space')

        raylib.begin_drawing()
        raylib.clear_background(raylib.RAYWHITE)

        raylib.end_drawing()

    raylib.close_window()

if __name__ == '__main__':
    main()
