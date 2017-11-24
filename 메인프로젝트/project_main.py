from pico2d import *
import random
import game_framework
import title_state

speed=5.0
back_speed=3.0
bgm_main=None

class Barrier:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 180000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x,self.y=400,80
        self.image = load_image('장애물.png')
        #self.speed = 0
        #self.width = 0
        #self.screen_width = w
        #self.screen_height = h

    def enter(self):
        self.sizeX,self.sizeY=80,440
        self.y=600-(self.sizeY/2)

    #def draw(self):
    #    x = int(self.width)
    #    w = min(self.image.w - x, self.screen_width)
    #    self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
    #    self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    #def update(self, frame_time):
    #    self.speed = Barrier.RUN_SPEED_PPS
    #    self.width = (self.width + frame_time * self.speed) % self.image.w

    def update(self,frame_time):
        self.x-=5

    def draw(self):
        self.image.draw(self.x,self.y)

    def exit(self):
        del(self.image)

    def get_bb(self):
        return self.x-8,self.y-20,self.x+8,self.y+20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Background:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 180000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self,w,h):
        self.image=load_image('b.png')
        self.speed=0
        self.width=0
        self.screen_width=w
        self.screen_height=h

    def update(self, frame_time):
        self.speed = Background.RUN_SPEED_PPS
        self.width = (self.width + frame_time * self.speed) % self.image.w

    def draw(self):
        x = int(self.width)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

class Grass:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 180000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self,w,h):
        self.image=load_image('grass.png')
        self.speed = 0
        self.width = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        x = int(self.width)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    def update(self, frame_time):
        self.speed = Grass.RUN_SPEED_PPS
        self.width = (self.width + frame_time * self.speed) % self.image.w

class Boy:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 180000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x,self.y=50,130
        self.frame=0
        self.jump_frame=0
        self.collide_frame=0
        self.jump_time=0
        self.isjump=0
        self.image=load_image('기본쿠키.png')
        self.jump_image=load_image('쿠키점프.png')
        self.collide_image=load_image('충돌이미지.png')

    def update(self):
        global jump,jump_time,isjump
        self.frame=(self.frame+1)%6
        self.jump_frame=(self.jump_frame+1)%1
        self.collide_frame=(self.collide_frame+1)%3

        if(jump==True and jump_time<4):
            jump_time+=0.5
            boy.y+=60
            isjump+=40
        elif(jump_time>=4):
            jump=False
        if(isjump>=0):
            boy.y-=30
            isjump-=20
        if(jump_time==5):
            boy.y+=0
            isjump+=0
        if(isjump==0):
            jump_time=0

        #elif(jump_time>=2 and jump==False):
        #    boy.y-=60
        #    jump_time=0


    def draw(self):
        if(jump==False and collide(boy,barrier)==False):
            self.image.clip_draw(self.frame*75,0,75,100,self.x,self.y)

        elif(jump==True):
            self.jump_image.clip_draw(self.jump_frame*75,0,75,100,self.x,self.y)

        if (collide(boy, barrier)):
            self.collide_image.clip_draw(self.collide_frame * 100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-20,self.y-40,self.x+20,self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

def collide(a,b):
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b,right_b,top_b=b.get_bb()

    if left_a>right_b:
        return False
    if right_a<left_b:
        return False
    if top_a<bottom_b:
        return False
    if bottom_a>top_b:
        return False
    return True

def enter():
    global boy,grass,background,jump,running,barrier,jump_time,isjump,crash,bgm_main
    #open_canvas()
    #bgm_main = load_music('스테이지1.wav')
    #bgm_main.set_volume(64)
    #bgm_main.repeat_play()
    boy=Boy()
    grass=Grass(800,60)
    background=Background(800,600)
    barrier=Barrier()
    running = True
    jump = False
    crash=False
    jump_time=0
    isjump=0



def exit():
    global boy,grass,background,barrier
    del(boy)
    del(grass)
    del(background)
    del(barrier)
    close_canvas()

def handle_events():
    global jump
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.quit()
        #if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        #    game_framework.change_state(title_state)
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
            jump=False
        elif (event.type,event.key)==(SDL_KEYUP,SDLK_SPACE):
            jump=True

def update(frame_time):
    global jump,background,grass,barrier,crash
    boy.update()
    background.update(frame_time)
    grass.update(frame_time)
    barrier.update(frame_time)
    if collide(boy,barrier):
        print('collision')


def draw(frame_time):
    clear_canvas()
    background.draw()
    grass.draw()
    barrier.draw()
    #update()
    boy.draw()
    boy.draw_bb()
    barrier.draw_bb()
    handle_events()
    update_canvas()
    delay(0.05)

#def main():
#    enter()
#    while running:
#        handle_events()
#        update()
#        draw()
#    exit()

#if __name__=='__main__':
#    main()
