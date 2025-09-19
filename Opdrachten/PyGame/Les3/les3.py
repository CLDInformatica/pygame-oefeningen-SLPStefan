'''
Voeg de volgende 2 dingen aan de game toe:

  - Laat de auto aan de linkerkant van het scherm terugkomen als de auto aan de rechterkant van het scherm af rijdt HINT: Gebruik een ```if``` met daarin de ```x_pos```
  - Laat een aantal regendruppels van de bovenkant van het scherm naar beneden vallen

Slides: https://docs.google.com/presentation/d/16rz2C4Pqhx4YNCokEU_5mc3rtQXXNEoi7gFAGzv9s_A/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((612, 408))
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

road = pygame.image.load("Opdrachten/PyGame/Les3/graphics/weg.jpg")

background_surface = pygame.Surface((800, 400))
background_surface.fill("white")

regen_surface = pygame.image.load("Opdrachten/PyGame/Les3/graphics/regen.png")

regen_y_pos = -300

reger_surface = pygame.image.load("Opdrachten/PyGame/Les3/graphics/regen.png")

reger_y_pos = 0

auto_surface = pygame.image.load("Opdrachten/PyGame/Les3/graphics/autoecht.png").convert_alpha()
DEFAULT_IMAGE_SIZE = (auto_surface.get_width() // 4, auto_surface.get_height() // 4)
autoecht_surface = pygame.transform.scale(auto_surface, DEFAULT_IMAGE_SIZE)

autoecht_x_pos = 200

while running:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False

    
    screen.blit(road, (0, 0))

    autoecht_x_pos += 4
    regen_y_pos += 3
    reger_y_pos += 3
    screen.blit(autoecht_surface, (autoecht_x_pos, 200))
    screen.blit(regen_surface, (0, regen_y_pos))
    screen.blit(reger_surface, (0, reger_y_pos))
    if regen_y_pos >= 408:
      regen_y_pos -= 800
    if reger_y_pos >= 408:
      reger_y_pos -= 800
    if autoecht_x_pos >= 600:
      autoecht_x_pos -= 700

    pygame.display.update()
    clock.tick(60)