from pico2d import *

class Grass:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 36000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self,w,h):
        self.image=load_image('grass.png')
        self.speed = 0
        self.width = 0
        self.screen_width = w
        self.screen_height = h

    def exit(self):
        del(self.image)

    def draw(self):
        x = int(self.width)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    def update(self, frame_time):
        self.speed = Grass.RUN_SPEED_PPS
        self.width = (self.width + frame_time * self.speed) % self.image.w