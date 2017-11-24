from pico2d import *
import game_framework
from Cookie import *
from Background import *
from Grass import *
from barrier import *
from collide import *

name="MainState"
main_bgm=None


def create_world():
    global cookie,background,grass,obstacle,jump,jump_time,isjump,main_bgm
    background=Background(800,600)
    cookie=Cookie()
    grass=Grass(800,60)
    obstacle=Barrier()
    jump = False
    jump_time = 0
    isjump = 0
    main_bgm=load_music('스테이지1.wav')
    main_bgm.set_volume(32)
    main_bgm.repeat_play()

def destroy_world():
    global cookie, background, grass, obstacle
    del(cookie)
    del(background)
    del(grass)
    del(obstacle)

def enter():
    global jump,jump_time,isjump,collision
    jump = False
    jump_time = 0
    isjump = 0
    collision=False
    create_world()

def exit():
    destroy_world()

def pause():
    pass

def resume():
    pass

def handle_events():
    events=get_events()
    for event in events:
        if (event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()
        else:
            cookie.handle_event(event)

def update(frame_time):
    global jump, jump_time, isjump
    background.update(frame_time)
    cookie.update(frame_time)
    grass.update(frame_time)
    obstacle.update(frame_time)

def draw(frame_time):
    global collision
    clear_canvas()
    background.draw()
    grass.draw()
    obstacle.draw()
    if collide(cookie,obstacle):
        cookie.check_collision()
        print("collision")
    cookie.draw()
    cookie.collision = False
    update_canvas()
