from pico2d import *


class Pitcher:
    def __init__(self):
        self.x, self.y = 400, 100
        self.frame = 0
        self.action = 3  # ?
        self.image = load_image('Pitcher.png')

    def update(self):
        pass

    def handle_event(self):
        pass

    def draw(self):
        pass
