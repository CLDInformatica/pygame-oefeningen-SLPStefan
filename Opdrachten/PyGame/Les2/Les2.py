'''
Gegeven zijn: een horror font dat "voetbal game" op het scherm zet en een plaatje van een bal.

We gaan de game aanpassen zodat het er beter uit ziet.

Doe het volgende:

  - Download een toepasselijk font en maak hiermee een scoreboard
  - Download 2 plaatjes van voetballers en zet deze tegenover elkaar op het scherm
  - Zet de bal in het midden van de scherm

Extra tijd:

  - Voeg 2 goals toe (links en rechts)
  - Voeg een toepasselijke achtergrond toe
  - Schrijf de namen van de spelers ergens op het scherm

Slides: https://docs.google.com/presentation/d/1c4C94q8OcMGCIFefVo18Xac4WIFJacq5Eutj1gY6rCg/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((960, 639))
pygame.display.set_caption('Portugal O - O Argentinië')
clock = pygame.time.Clock()
running = True
test_font = pygame.font.Font("Opdrachten/PyGame/Les2/fonts/Snacker.ttf", 50)
Lato = pygame.font.Font("Opdrachten/PyGame/Les2/fonts/Lato.ttf", 25)

scoreboards = pygame.Surface((300, 30))
scoreboards.fill("gray")
scoreboards2 = pygame.Surface((80, 30))
scoreboards2.fill("white")
scoreboards3 = pygame.Surface((70, 30))
scoreboards3.fill("blue")
voetbalveld = pygame.image.load("Opdrachten/PyGame/Les2/graphics/veld.jpg")
voetbal = pygame.image.load("Opdrachten/PyGame/Les2/graphics/voetbal.png")
scorebord = Lato.render("Por     6-7     No", False, "black")
minuten = Lato.render("67:16", False, "white")
naamronaldo = test_font.render("Ronaldo", False, "black")
naammessi = test_font.render("Messi", False, "black")
Nor = pygame.image.load("Opdrachten/PyGame/Les2/graphics/Nor.png")
DEFAULT_IMAGE_SIZE = (Nor.get_width() // 63, Nor.get_height() // 63)
Nor_small = pygame.transform.scale(Nor, DEFAULT_IMAGE_SIZE)

por = pygame.image.load("Opdrachten/PyGame/Les2/graphics/Portugal.png")
DEFAULT_IMAGE_SIZE = (por.get_width() // 13, por.get_height() // 13)
por_small = pygame.transform.scale(por, DEFAULT_IMAGE_SIZE)


deronaldo = pygame.image.load("Opdrachten/PyGame/Les2/graphics/deronaldo.png")
DEFAULT_IMAGE_SIZE = (deronaldo.get_width() // 2, deronaldo.get_height() // 2)
deronaldo_small = pygame.transform.scale(deronaldo, DEFAULT_IMAGE_SIZE)

messi = pygame.image.load("Opdrachten/PyGame/Les2/graphics/messi.png")
DEFAULT_IMAGE_SIZE = (messi.get_width() // 1.4, messi.get_height() // 1.4)
messi_small = pygame.transform.scale(messi, DEFAULT_IMAGE_SIZE)

goalrechts = pygame.image.load("Opdrachten/PyGame/Les2/graphics/goalrechts.png")
goallinks = pygame.image.load("Opdrachten/PyGame/Les2/graphics/goallinks.png")

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(voetbalveld,  (0, 0))
  screen.blit(scoreboards3, (320, 0))
  screen.blit(scoreboards, (20, 0))
  screen.blit(scoreboards2, (130, 0))
  screen.blit(scorebord, (88, 0))
  screen.blit(minuten, (320, 0))
  screen.blit(voetbal, (460, 500))
  screen.blit(Nor_small, (280, 0))
  screen.blit(por_small, (20, 0))
  screen.blit(deronaldo_small, (200, 300))
  screen.blit(messi_small, (400, 300))
  screen.blit(goalrechts, (850, 200))
  screen.blit(goallinks, (-200, 200))
  screen.blit(naamronaldo, (300, 250))
  screen.blit(naammessi, (540, 250))
  
  pygame.display.update()
  clock.tick(60)
