import os 
import pygame  
pygame.init()


player = pygame.image.load(os.path.join("images", "38px.png"))

#global variables



#bar object 
class Player(): 

    def __init__(self, x, y, mvt, s): 
        self.x = x 
        self.y = y
        self.mvt = mvt 
        self.s = s 
        
    def draw_player(self): 
        self.s.blit(player, (self.x,self.y))
        #movement of the player
        if self.y > 562: 
          self.y = 562
        if self.y < 12: 
          self.y = 12
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
          self.y -= self.mvt 
        if pressed[pygame.K_DOWN]:
          self.y += self.mvt
        return self.y


