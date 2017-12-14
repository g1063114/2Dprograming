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
        self.big_frame=0
        self.jump_frame=0
        self.collide_frame=0
        self.dead_frame=0
        self.slide_frame=0
        self.jump = False
        self.slide=False
        self.collision=False
        self.dead = False
        self.big = False
        self.dir=0
        self.life=500
        self.jellyCount=0
        self.bigCount=0
        self.image=load_image('기본쿠키.png')
        self.jump_image=load_image('쿠키점프.png')
        self.collide_image=load_image('충돌이미지.png')
        self.dead_image=load_image('죽음.png')
        self.slide_image=load_image('슬라이드.png')
        self.big_image=load_image('큰쿠키.png')

    def exit(self):
        del(self.image)
        del(self.jump_image)
        del(self.collide_image)
        del(self.dead_image)
        del(self.slide_image)
        del(self.big_image)

    def update(self,frame_time):
        global jump
        self.frame = (self.frame + 1) % 6
        self.jump_frame = (self.jump_frame + 1) % 1
        self.collide_frame = (self.collide_frame + 1) % 1
        self.slide_frame=(self.slide_frame+1)%1
        self.big_frame=(self.big_frame+1)%6

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

        if self.big is True:
            self.bigCount+=0.5
            if self.bigCount>100:
                self.big=False
                self.bigCount=0

    def check_collision(self):
        self.collision=True

    def draw(self):
        if self.jump is False and self.collision is False and self.dead is False and self.slide is False and self.big is False:
            self.image.clip_draw(self.frame*75,0,75,100,self.x,self.y)
        elif self.jump is True and self.big is False:
            self.jump_image.clip_draw(self.jump_frame*75,0,75,100,self.x,self.y)
        if self.collision is True:
            self.collide_image.clip_draw(self.collide_frame*75,0,75,100,self.x,self.y)
        if self.dead is True:
            self.dead_image.clip_draw(self.dead_frame*100,0,100,100,self.x,self.y)
        if self.slide is True and self.big is False:
            self.slide_image.clip_draw(self.slide_frame*100,0,100,50,self.x,self.y-20)
        if self.big is True and self.slide is False:
            self.big_image.clip_draw(self.big_frame*300,0,300,348,self.x,self.y+130)

    def get_bb(self):
        if self.slide is True:
            return self.x-40,self.y-10,self.x+40,self.y+10
        if self.big is True:
            return self.x-100,self.y-30,self.x+100,self.y+240
        return self.x-20,self.y-30,self.x+20,self.y+30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self,event):
        if (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
            self.jump=True
        if(event.type,event.key)==(SDL_KEYDOWN,SDLK_DOWN):
            self.slide=True
        elif(event.type,event.key)==(SDL_KEYUP,SDLK_DOWN):
            self.slide=False




