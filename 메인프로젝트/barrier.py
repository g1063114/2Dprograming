from pico2d import *

class Barrier:
    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 36000.0  # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self,px,ptype,pimage_type):
        self.x,self.y=px,80
        self.dir=0
        self.type=ptype
        self.imagetype=pimage_type
        #self.image = load_image('장애물.png')
        #self.speed = 0
        #self.width = 0
        #self.screen_width = w
        #self.screen_height = h
    def exit(self):
        del(self.image)

    def enter(self):
        if self.type==0:
            if self.imagetype==0:
                self.sizeX,self.sizeY=80,540
                self.image=load_image('포크.png')
            elif self.imagetype==1:
                self.sizeX,self.sizeY=80,540
                self.image=load_image('포크2.png')

            self.y=600-(self.sizeY/2)

        elif self.type==1:
            if self.imagetype==0:
                self.sizeX,self.sizeY=30,60
                self.image=load_image('장애물.png')
            elif self.imagetype==1:
                self.sizeX,self.sizeY=42,100
                self.image=load_image('장애물2.png')
            elif self.imagetype==2:
                self.sizeX,self.sizeY=30,60
                self.image=load_image('장애물3.png')

            self.y=45+(self.sizeY/2)

    #def draw(self):
    #    x = int(self.width)
    #    w = min(self.image.w - x, self.screen_width)
    #    self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
    #    self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    #def update(self, frame_time):
    #    self.speed = Barrier.RUN_SPEED_PPS
    #    self.width = (self.width + frame_time * self.speed) % self.image.w

    def update(self,frame_time):
        distance = Barrier.RUN_SPEED_PPS * frame_time
        self.x-=(self.dir*distance)
        self.dir=1

    def draw(self):
        if self.type==0:
            self.image.draw(self.x,self.y)
        elif self.type==1:
            self.image.draw(self.x,self.y)

    def exit(self):
        del(self.image)

    def get_bb(self):
        if self.type==1:
            return self.x-8,self.y-20,self.x+8,self.y+20
        elif self.type==0:
            return self.x-20,self.y-200,self.x+20,self.y+200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())