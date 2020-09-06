import os 
import pygame 
pygame.init()



class Button():
    #the class for my buttons
   
    def __init__(self, pos, color, size, text, text_size):
        self.pos = pos 
        self.size = size
        self.color = color 
        self.text = text 
        self.text_size = text_size


    def draw_button(self, screen):
        pygame.draw.rect( screen, self.color ,(self.pos[0], self.pos[1], self.size[0], self.size[1]) , 0 )
        if self.text != '':
            font = pygame._freetype.Font("C:/Users/Skymil/Desktop/Aymen/python/Ball/images/DK Lemon Yellow Sun.otf", self.text_size)
            text = font.render(self.text, (255,255,255))
            self.BUT = screen.blit(text[0], (self.pos[0] - 1, self.pos[1] - 1)  )
    
    def is_clicked(self, mouse_pos): 
        return  self.BUT.collidepoint(mouse_pos)