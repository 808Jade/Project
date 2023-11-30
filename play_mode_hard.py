from pico2d import *
import game_framework
import game_world

import title_mode
from hitter import Hitter
from pitcher import Pitcher
from playground import Playground
from sign import Outsign
from strike_counter import Strike_counter
from strike_zone import Strike_zone
from score_calculator import ScoreCalculator


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            hitter.handle_event(event)


def init():
    global playground
    global hitter
    global pitcher
    global strike_zone
    global strike_counter
    global score_calculator
    global outsign, outsign_flag

    playground = Playground()
    game_world.add_object(playground, 0)

    hitter = Hitter()
    game_world.add_object(hitter, 1)

    pitcher = Pitcher()
    pitcher.current_mode = 'hard'
    game_world.add_object(pitcher, 1)

    strike_zone = Strike_zone()
    game_world.add_object(strike_zone, 3)

    strike_counter = Strike_counter()
    game_world.add_object(strike_counter, 2)

    score_calculator = ScoreCalculator()

    outsign = Outsign()
    outsign_flag = False


def finish():
    game_world.clear()
    pass


def update():
    global outsign_flag
    game_world.update()
    if strike_counter.count >= 3 and outsign_flag == False:
        game_world.add_object(outsign, 2)
        outsign.sign_on()
        outsign_flag = True


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
