from pico2d import *

class Jelly:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 36000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self,jx,jy,jtype):
        self.x,self.y=jx,jy
        self.sizeX,self.sizeY=54,53
        self.type=jtype
        self.dir=0

    def enter(self):
        if self.type==0:
            self.skill=0
            self.image=load_image('big.png')
        elif self.type==1:
            self.skill=1
            self.image=load_image('젤리아이콘.png')
        elif self.type==2:
            self.skill=80
            self.image=load_image('회복.png')

    def update(self,frame_time):
        distance = Jelly.RUN_SPEED_PPS * frame_time
        self.x -= (self.dir * distance)
        self.dir = 0.5

    def draw(self):
        self.image.draw(self.x,self.y)

    def exit(self):
        del(self.image)

    def get_bb(self):
        return self.x-30,self.y-30,self.x+30,self.y+30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())