from pico2d import *
import game_framework
import title_state
import cookie_main
import ui

name="ResultState"
image=None
bgm=None
jelly_image=None

def enter():
    global image,bgm,result
    image = load_image('결과화면.png')
    bgm = load_music('결과음악.wav')
    bgm.set_volume(64)
    bgm.repeat_play()
    result=0
    pass

def exit():
    global image,bgm,jelly_image
    del(image)
    del(bgm)
    del(jelly_image)
    pass

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(title_state)
    pass

def draw(frame_time):
    global result,jelly_image
    clear_canvas()
    image.draw(400,300)
    jelly_image = ui.load_image('젤리아이콘.png')
    jelly_image.draw(400, 300)
    update_canvas()
    pass

def update(frame_time):
    pass

def pause():
    pass

def resume():
    pass