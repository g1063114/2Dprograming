from pico2d import *
import game_framework

name="TitleState"
image=None


def enter():
    global image
    open_canvas()
    image=load_image('title.png')

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

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass