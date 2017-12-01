from pico2d import *
from barrier import *
from collide import *

class Player:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 18000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER



    def __init__(self):
        self.x,self.y=50,100
        self.frame=0
        self.jump_frame=0
        self.collide_frame=0
        self.dead_frame=0
        self.jump = False
        self.collision=False
        self.dir=0
        self.life=300
        self.dead=False
        self.big=False
        self.jellyCount=0
        self.image=load_image('기본쿠키.png')
        self.jump_image=load_image('쿠키점프.png')
        self.collide_image=load_image('충돌이미지.png')
        self.dead_image=load_image('죽음.png')

    def update(self,frame_time):
        global jump
        self.frame = (self.frame + 1) % 6
        self.jump_frame = (self.jump_frame + 1) % 1
        self.collide_frame = (self.collide_frame + 1) % 1

        if self.dead==False:
            self.life-=0.5
        elif self.dead==True:
            self.dead_frame=(self.dead_frame+1)%4
        if self.life<0:
            self.dead=True
            self.life=0
            self.dead_frame=0

        distance = Player.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)
        self.y = clamp(100, self.y, 500)
        if self.jump:
            if self.y < 230 :
                self.dir = 5
            if self.y > 230 :
                self.jump = False
        if not self.jump:
            self.dir = -7

        #elif (jump_time >= 4):
        #    jump = False
        #if (isjump >= 0):
        #    self.y -= (self.dir * distance)
        #    isjump -= 20
        #if (jump_time == 5):
        #    self.y += 0
        #    isjump += 0
        #if (isjump == 0):
        #    jump_time = 0

    def check_collision(self):
        self.collision=True

    def draw(self):
        if self.jump is False and self.collision is False and self.dead is False:
            self.image.clip_draw(self.frame*75,0,75,100,self.x,self.y)
        elif self.jump is True:
            self.jump_image.clip_draw(self.jump_frame*75,0,75,100,self.x,self.y)
        if self.collision is True:
            self.collide_image.clip_draw(self.collide_frame*75,0,75,100,self.x,self.y)
        if self.dead is True:
            self.dead_image.clip_draw(self.dead_frame*100,0,100,100,self.x,self.y)

    def get_bb(self):
        return self.x-20,self.y-40,self.x+20,self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self,event):
        if (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
            self.jump=True




