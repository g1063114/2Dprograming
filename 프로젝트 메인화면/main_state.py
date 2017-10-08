from pico2d import *
import random
import game_framework
import title_state

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),random.randint(90,500)
        self.frame=random.randint(0,7)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=2

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


running=True

def enter():
    global boy,grass,team
    open_canvas()
    boy=Boy()
    grass=Grass()
    team = [Boy() for i in range(11)]

def exit():
    global boy,grass,team
    del(boy)
    del(grass)
    del(team)
    close_canvas()

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            boy.x, boy.y = event.x, 600 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            team[0].x, team[0].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            team[1].x, team[1].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            team[2].x, team[2].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            team[3].x, team[3].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            team[4].x, team[4].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_5:
            team[5].x, team[5].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_6:
            team[6].x, team[6].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_7:
            team[7].x, team[7].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_8:
            team[8].x, team[8].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_9:
            team[9].x, team[9].y = boy.x, boy.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_KP_1:
            team[10].x, team[10].y = boy.x, boy.y
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)

def update():
    for boy in team:
        boy.update()

def draw():
    clear_canvas()
    grass.draw()
    for boy in team:
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
