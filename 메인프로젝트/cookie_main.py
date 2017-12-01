from pico2d import *
import game_framework
from Cookie import *
from Background import *
from Grass import *
from barrier import *
from collide import *
from ui import *
from jelly import *
import json
import title_state

name="MainState"
main_bgm=None
MAP_SIZE=11000
OBSTACLE,JELLY=0,1
obstacle_list=None
gameEnd=False

def create_world():
    global cookie,background,grass,obstacle,jump,jump_time,isjump,main_bgm,ui
    background=Background(800,600)
    cookie=Player()
    ui=UI()
    grass=Grass(800,60)
    #obstacle=Barrier()
    jump = False
    jump_time = 0
    isjump = 0
    main_bgm=load_music('스테이지1.wav')
    main_bgm.set_volume(32)
    main_bgm.repeat_play()
    load_map_data()

def destroy_world():
    global cookie, background, grass, obstacle,obstacle_list,ui
    del(cookie)
    del(background)
    del(grass)
    del(ui)
    #del(obstacle)
    for i in obstacle_list:
        for j in obstacle_list[i]:
            obstacle_list[i].remove(j)

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
    global jump, jump_time, isjump,obstacle_list,gameEnd

    if gameEnd==True:
        game_framework.change_state(title_state)

    background.update(frame_time)
    cookie.update(frame_time)
    grass.update(frame_time)
    for i in obstacle_list:
        for j in obstacle_list[i]:
            j.update(frame_time)

    for i in obstacle_list:
        for j in obstacle_list[i]:
            if i==0:
                if(collide(cookie,j)):
                    cookie.check_collision()
                    cookie.life-=10.0
                    obstacle_list[i].remove(j)
            elif i==1:
                if(collide(cookie,j)):
                    if j.type==0:
                        cookie.big=True
                        obstacle_list[i].remove(j)
                    elif j.type==1:
                        cookie.jellyCount+=j.skill
                        obstacle_list[i].remove(j)
                    elif j.type==2:
                        cookie.life+=j.skill
                        if cookie.life>300:
                            cookie.life=300




def draw(frame_time):
    global collision,obstacle_list
    clear_canvas()
    background.draw()
    grass.draw()
    for i in obstacle_list:
        for j in obstacle_list[i]:
            j.draw()

    for i in obstacle_list:
        for j in obstacle_list[i]:
            j.draw_bb()

    ui.draw()
    cookie.draw()
    cookie.collision = False
    update_canvas()

def clear_map_data():
    global obstacle_list
    for i in obstacle_list:
        for j in obstacle_list[i]:
            obstacle_list[i].remove(j)

def load_map_data():
    #clear_map_data()
    global obstacle_list
    tempobstacle=Barrier(1000,1,0)

    tempobstacle.enter()

    obstacle_list={OBSTACLE:[tempobstacle],JELLY:[]}

    tempobstacle=Barrier(1300,1,0)
    tempobstacle.enter()
    obstacle_list[OBSTACLE].append(tempobstacle)
    tempobstacle = Barrier(1600, 1, 1)
    tempobstacle.enter()
    obstacle_list[OBSTACLE].append(tempobstacle)
    tempobstacle = Barrier(1900, 0, 0)
    tempobstacle.enter()
    obstacle_list[OBSTACLE].append(tempobstacle)

    tempobstacle = Barrier(2200, 0, 1)
    tempobstacle.enter()
    obstacle_list[OBSTACLE].append(tempobstacle)
    tempobstacle = Barrier(2400, 1, 1)
    tempobstacle.enter()
    obstacle_list[OBSTACLE].append(tempobstacle)
    tempobstacle = Barrier(2700, 0, 1)
    tempobstacle.enter()
    obstacle_list[OBSTACLE].append(tempobstacle)

    tempjelly=Jelly(1000,130,1)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)

    obstacle_list[JELLY].append(tempjelly)
    tempjelly=Jelly(1050,100,1)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)

    obstacle_list[JELLY].append(tempjelly)
    tempjelly = Jelly(1100, 100, 1)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)

    obstacle_list[JELLY].append(tempjelly)
    tempjelly = Jelly(1150, 100, 1)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)

    obstacle_list[JELLY].append(tempjelly)
    tempjelly = Jelly(1200, 100, 1)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)

    obstacle_list[JELLY].append(tempjelly)
    tempjelly = Jelly(1250, 100, 1)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)

    obstacle_list[JELLY].append(tempjelly)
    tempjelly = Jelly(1300, 130, 2)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)

    obstacle_list[JELLY].append(tempjelly)
    tempjelly = Jelly(1350, 130, 1)
    tempjelly.enter()
    obstacle_list[JELLY].append(tempjelly)
