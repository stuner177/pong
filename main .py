import pygame 
import pygame._freetype
import os 
from player import Player
from button import Button
from ball import Ball


pygame.init()
pygame.font.init()



#global variables
WIN_HEIGHT = 1024 
WIN_WIDTH = 768 
SPEED = 5 
PX = 956
PY  = 320 
MOVEMENT = 5



screen = pygame.display.set_mode((WIN_HEIGHT,WIN_WIDTH ))
pygame.display.set_caption("Pong")





START_BUTTON =  Button((325,225),(0,0,0) , (215,55),  "Bonjour % ", 60 ) 
EXIT_BUTTON = Button((890,25), (0,0,0), (180,55), "Quitter", 45 )
PLAYER = Player(PX,PY,MOVEMENT, screen)
BALL = Ball(550, 60, screen, .5, .4, PX, PY)


def redraw_screen(): 
  
  
  START_BUTTON.draw_button(screen)
  EXIT_BUTTON.draw_button(screen)
  pygame.display.flip()
  pygame.display.update()



running = True 
while running: 

  redraw_screen()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    mouse_pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN and START_BUTTON.is_clicked(mouse_pos):
      running = False
      playing = True

      while playing: 
        screen.fill((0,0,0))
        BALL.draw_ball()
        PLAYER.draw_player()
        pygame.display.flip()

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
            playing = False 
        
        

       
     



    




