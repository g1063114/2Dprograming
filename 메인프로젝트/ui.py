from pico2d import *
import cookie_main

class UI:
    def __init__(self):
        self.number0_image=load_image('0.png')
        self.number1_image = load_image('1.png')
        self.number2_image = load_image('2.png')
        self.number3_image = load_image('3.png')
        self.number4_image = load_image('4.png')
        self.number5_image = load_image('5.png')
        self.number6_image = load_image('6.png')
        self.number7_image = load_image('7.png')
        self.number8_image = load_image('8.png')
        self.number9_image = load_image('9.png')

        self.jelly_image=load_image('젤리아이콘.png')
        self.hp_image = load_image('hpbar.png')
        self.big_image=load_image('big.png')
        self.hpup_image=load_image('회복.png')

        self.playerscore=0

    def exit(self):
        del(self.hp_image)
        del (self.jelly_image)
        del (self.big_image)
        del (self.hpup_image)
        del (self.number0_image)
        del (self.number1_image)
        del (self.number2_image)
        del (self.number3_image)
        del (self.number4_image)
        del (self.number5_image)
        del (self.number6_image)
        del (self.number7_image)
        del (self.number8_image)
        del (self.number9_image)


    def enter(self):
        pass

    def update(self,frame_time):
        pass

    def draw(self):
        if cookie_main.cookie.life>0:
            rate=(int)(300*(cookie_main.cookie.life/500))
            self.hp_image.clip_draw(0,0,rate*2,64,rate+50,550)

            self.playerscore=(int)(cookie_main.cookie.jellyCount)

            self.jelly_image.draw(80,480)

    def score_draw(self,number,x,y):
        if number==0:
            self.number0_image.draw(x,y)
        elif number==1:
            self.number1_image.draw(x,y)
        elif number==2:
            self.number2_image.draw(x,y)
        elif number==3:
            self.number3_image.draw(x,y)
        elif number==4:
            self.number4_image.draw(x,y)
        elif number==5:
            self.number5_image.draw(x,y)
        elif number==6:
            self.number6_image.draw(x,y)
        elif number==7:
            self.number7_image.draw(x,y)
        elif number==8:
            self.number8_image.draw(x,y)
        elif number==9:
            self.number9_image.draw(x,y)