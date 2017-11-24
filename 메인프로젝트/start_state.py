from pico2d import *
import game_framework
import title_state

name="StartState"
image=None
logo_time=0.0

def enter():
    global image
    open_canvas(sync=True)
    image=load_image('kpu_credit.png')
    pass

def exit():
    global image
    del(image)
    close_canvas()
    pass

def update(frame_time):
    global logo_time

    if(logo_time>1.0):
        logo_time=0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time+=0.01
    pass

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events=get_events()
    pass

def pause():
    pass

def resume():
    pass