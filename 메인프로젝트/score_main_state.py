from pico2d import *
import game_framework
import score_state
import time

name='ScoreMainState'

def enter():
    pass

def doGameOver(score):
    entry=score_state.Entry(score,time.time())
    score_state.add(entry)
    game_framework.push_state(score_state)

def handle_event():
    events=get_events()
    for event in events:
        if (event.type)==(SDL_MOUSEBUTTONDOWN):
            game_framework.push_state(score_state)
        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_x):
            print('x Pressed')
