from pico2d import *
import random
import game_framework
import title_state

class Barrier:
    def __init__(self):
        self.x,self.y=400,80
        self.image = load_image('장애물.png')

    def enter(self):
        self.sizeX,self.sizeY=80,440
        self.y=600-(self.sizeY/2)

    def draw(self):
        self.image.draw(self.x,self.y)

    def exit(self):
        del(self.image)

class Background:
    def __init__(self):
        self.image=load_image('배경.png')

    def draw(self):
        self.image.draw(400,300)

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x,self.y=50,90
        self.frame=0
        self.jump_frame=0
        self.image=load_image('쿠키.png')
        self.jump_image=load_image('점프.png')

    def update(self):
        global jump,limit
        self.frame=(self.frame+1)%8
        self.jump_frame=(self.jump_frame+1)%4
        limit=150

        if(jump==True):
            boy.y+=60

        elif(boy.y>=limit and jump==False):
            boy.y-=60


    def draw(self):
        if(jump==False):
            self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        elif(jump==True):
            self.jump_image.clip_draw(self.jump_frame*100,0,100,100,self.x,self.y)


def enter():
    global boy,grass,background,jump,running,barrier
    open_canvas()
    boy=Boy()
    grass=Grass()
    background=Background()
    barrier=Barrier()
    running = True
    jump = False


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
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
            jump=True
        elif (event.type,event.key)==(SDL_KEYUP,SDLK_SPACE):
            jump=False
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)

def update():
    global jump
    boy.update()

def draw():
    clear_canvas()
    background.draw()
    grass.draw()
    barrier.draw()
    boy.draw()
    update_canvas()
    delay(0.05)

def main():
    enter()
    while running:
        handle_events()
        update()
        draw()
    exit()

if __name__=='__main__':
    main()
