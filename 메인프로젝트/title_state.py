from pico2d import *
import game_framework
import main_state
import project_main

name="TitleState"
image=None


def enter():
    global image
    open_canvas()
    image=load_image('시작화면7.png')

def exit():
    global image
    del(image)
    close_canvas()

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(project_main)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass