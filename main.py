from pico2d import *
import game_framework

import play_mode as start_mode
import logo_mode
# import title_mode

open_canvas()
game_framework.run(start_mode)
close_canvas()