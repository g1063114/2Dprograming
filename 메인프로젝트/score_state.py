from pico2d import *
import game_framework
import json
import pickle

class Entry:
    def __init__(self,score,time):
        self.score=score
        self.time=time

scores=[]


name='ScoreState'

usesPickle=True
if (usesPickle):
    filename='score.pickle'
else:
    filename='score.json'

def loadScores():
    scores=[]
    if (usesPickle):
        f=open(filename,'w')
        pickle.dump(scores)
        f.close()

def saveScores():
    pass

def add(score):
    scores.append(score)
    print('Now Scores has' + str(len(scores))+"entries.")
    saveScores()

def enter():
    pass

def exit():
    pass

loadScores()

