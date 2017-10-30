from pico2d import *
import random
import json

font=None
n=0
member=5

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
        self.state=random.randint(0,3)
        if Boy.image==None:
            Boy.image=load_image('animation_sheet.png')

    def handle_event(self,event):
        if(event.type,event.key)==(SDL_KEYDOWN,SDLK_LEFT):
            if self.state in (self.RIGHT_STAND,self.LEFT_STAND):
                self.state=self.LEFT_RUN
                self.dir=-1
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND,self.LEFT_STAND):
                self.state=self.RIGHT_RUN
                self.dir=1
        elif (event.type,event.key)==(SDL_KEYUP,SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir=0
        elif (event.type,event.key)==(SDL_KEYUP,SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state=self.RIGHT_STAND
                self.dir=0

    def update(self):
        self.frame=(self.frame+1)%8
        self.handle_state[self.state](self)
        if self.state==self.RIGHT_RUN:
            self.x=min(800,self.x+5)
        elif self.state==self.LEFT_RUN:
            self.x=max(0,self.x-5)

    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)

def create_team():
    team_data_text='{"Tiffany" : {"StartState":"LEFT_RUN","x":100,"y":100}, "Yuna" : {"StartState":"RIGHT_RUN","x":200,"y":200} ,"Sunny" : {"StartState":"LEFT_STAND","x":300,"y":300},"Yuri" : {"StartState":"RIGHT_RUN","x":400,"y":400},"Jessica" : {"StartState":"LEFT_RUN","x":100,"y":100}}'

    player_state_table={
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN" : Boy.RIGHT_RUN,
        "LEFT_STAND" : Boy.LEFT_STAND,
        "RIGHT_STAND" : Boy.RIGHT_STAND
    }

    team_data=json.loads(team_data_text)

    team=[]
    for name in team_data:
        player=Boy()
        player.name=name
        player.x=team_data[name]['x']
        player.y=team_data[name]['y']
        player.state=player_state_table[team_data[name]['StartState']]
        team.append(player)
    return team

def enter():
    global boy,grass,team
    open_canvas()
    boy = Boy()
    grass = Grass()
    team=create_team()


def handle_events():
    global running,team,n
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif (event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE):
            running=False
        else:
            team[n].handle_event(event)

def handle_mouse_event():
    global running,n,team
    events=get_events()
    for event in events:
        if event.type==SDL_MOUSEMOTION:
            team[n].x,team[n].y=event.x,600-event.y


def update():
    global team
    for i in range(member):
        team[i].update()

def main():
    enter()

    global running
    running=True

    while(running):
        handle_events()
        update()
        clear_canvas()
        grass.draw()
        for i in range(member):
            team[i].draw()
        update_canvas()
        handle_mouse_event()

        delay(0.05)

    close_canvas()

if __name__=='__main__':
    main()