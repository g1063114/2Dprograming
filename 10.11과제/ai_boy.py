from pico2d import *
import random

font=None
n=0

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    image=None
    global n
    LEFT_RUN,RIGHT_RUN,LEFT_STAND,RIGHT_STAND=0,1,2,3

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def __init__(self):
        self.x,self.y=random.randint(100,700),random.randint(90,500)
        self.frame=random.randint(0,7)
        self.stand_frames=random.randint(0,7)
        self.run_frames=random.randint(0,7)
        self.dir=1
        self.state=self.RIGHT_RUN
        self.number=random.randint(0,1000)
        if Boy.image==None:
            Boy.image=load_image('animation_sheet.png')

    def update(self):
        if self.state==self.RIGHT_RUN:
            self.frame=(self.frame+1)%8
            self.x+=(self.dir*5)

        elif self.state==self.LEFT_RUN:
            self.frame=(self.frame+1)%8
            self.x+=(self.dir*5)

        if self.x>800:
            self.dir=-1
            self.x=800
            self.state=self.LEFT_RUN
        elif self.x<0:
            self.dir=1
            self.x=0
            self.state=self.RIGHT_RUN

    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)
        font.draw(700,30,'Number='+str(n))

def enter():
    global boy,grass,team,font
    open_canvas()
    boy = Boy()
    grass = Grass()
    team = [Boy() for i in range(1000)]
    font = Font('BMHANNA_11yrs_ttf.TTF', 20)


def handle_events():
    global running
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False

        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False

def handle_mouse():
    global n,team
    events=get_events()
    for event in events:
        if event.type==SDL_MOUSEMOTION:
            team[n].x,team[n].y=event.x,600-event.y
        elif event.type==SDL_KEYDOWN and event.key==SDLK_UP:
            n+=1

        elif event.type==SDL_KEYDOWN and event.key==SDLK_DOWN:
            n-=1




def update(self):
    self.frame=(self.frame+1)%8
    self.handle_state[self.state](self)

def main():
    enter()

    global running
    running=True

    while(running):
        handle_events()
        for boy in team:
            update(boy)
        clear_canvas()
        grass.draw()
        for boy in team:
            boy.draw()
        update_canvas()
        handle_mouse()

        delay(0.05)

    close_canvas()

if __name__=='__main__':
    main()