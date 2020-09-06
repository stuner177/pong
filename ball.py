import pygame 
import os 
 
ball = pygame.image.load(os.path.join("images", "ball.png"))

class Ball(): 

    def __init__(self, bx, by, sc, speedx, speedy, px , py ): 
        self.bx = bx 
        self.by = by 
        self.sc = sc 
        self.speedx = speedx
        self.speedy = speedy 
        self.px = px 
        self.py = py

    def draw_ball(self): 
        self.sc.blit(ball, (self.bx,self.by))
        self.bx += self.speedx
        self.by += self.speedy

        if self.bx >= 1000:#check goals
            self.bx = 250
            self.by = 340

        if self.bx <= 38: #check coalision
            self.speedx *= -1
        if self.by<= 12: 
            self.speedy *= -1
        if  self.by>= 725: 
            self.speedy *= -1
        
        #check coalision with the paddle 
        if self.bx > (self.px - 35) and (self.by < (self.py + 196) and  (self.by + 38) > self.py) : 
            self.speedx = -abs(self.speedx)
            


    

