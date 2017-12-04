from pico2d import *
import cookie_main

class UI:
    def __init__(self):
        self.hp_image=load_image('hpbar.png')

    def exit(self):
        del(self.hp_image)

    def enter(self):
        pass

    def update(self,frame_time):
        pass

    def draw(self):
        if cookie_main.cookie.life>0:
            rate=(int)(300*(cookie_main.cookie.life/500))
            self.hp_image.clip_draw(0,0,rate*2,64,rate+50,550)