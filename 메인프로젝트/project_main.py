from pico2d import *
import random
import game_framework
import title_state

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
        self.image=load_image('쿠키.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=2

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


running=True

def enter():
    global boy,grass,background
    open_canvas()
    boy=Boy()
    grass=Grass()
    background=Background()


def exit():
    global boy,grass,background
    del(boy)
    del(grass)
    del(background)
    close_canvas()

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()

        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)

def update():
    boy.update()

def draw():
    clear_canvas()
    background.draw()
    grass.draw()
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
