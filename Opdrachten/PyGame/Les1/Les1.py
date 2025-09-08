'''
Maak het plaatje dat in dit mapje staat na.

Slides: 
https://docs.google.com/presentation/d/1YwoUdeWABUYJkSfNzzZzDbCKvCVmWoo9Z5Uu7f_Y_K4/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Super gevorderde game')
clock = pygame.time.Clock()
running = True

surface = pygame.Surface((800, 400))
surface.fill("blue")

surface2 = pygame.Surface((45, 200))
surface2.fill("green")

surface3 = pygame.Surface((45, 70))
surface3.fill("green")

surface4 = pygame.Surface((45, 240))
surface4.fill("green")

surface5 = pygame.Surface((45, 70))
surface5.fill("green")

surface6 = pygame.Surface((45, 300))
surface6.fill("green")

surface7 = pygame.Surface((45, 70))
surface7.fill("green")



while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (0, 0))
  screen.blit(surface2, (200, 0))
  screen.blit(surface3, (400, 0))
  screen.blit(surface4, (600, 0))
  screen.blit(surface5, (200, 330))
  screen.blit(surface6, (400, 170))
  screen.blit(surface7, (600, 330))

  
  pygame.display.update()
  clock.tick(60)
