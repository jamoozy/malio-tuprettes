#!/usr/bin/python

import pygame, sys
from pygame.locals import *

class Player:
  def __init__(self, pnum):
    self.number = pnum

  def update(self, pressed):
    if pressed[pygame.key.K_s]:
      pass # go left
    elif pressed[pygame.key.K_d]:
      pass # duck
    elif pressed[pygame.key.K_f]:
      pass # go right
    elif pressed[pygame.key.K_e]:
      pass # climb/door
    elif pressed[pygame.key.K_j]:
      pass # action
    elif pressed[pygame.key.K_k]:
      pass # jump
    elif pressed[pygame.key.K_l]:
      pass # special

class Chunk:
  def __init__(self):
    pass

  def paint(self, screen):
    pass

class World:
  def __init__(self):
    self.progress = 0
    self.chunks = []

  def paint(self, screen):
    for i in xrange(max(0, self.progress-1), min(self.progress+1,len(self.chunks))):
      self.chunks[i].paint(screen)

class Game:
  '''The game to run.'''
  def __init__(self, num_players):
    self.players = map(lambda i: Player(i), range(num_players))
    self.world = World()

    pygame.init()

    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Game')
    self.bg_color = pygame.Color(0, 0, 220)

    # Load additional textures and things.

  def run(self):
    while True:
      self.screen.fill(self.bg_color)

      # One-shot events.
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == MOUSEBUTTONUP:
          self.mouse = event.pos
          if event.button in (1, 2, 3):
            print 'left, middle, or right mouse button hit'
          elif event.button in (4, 5):
            print 'mouse scroll'

      # Keyboard state events; e.g., "Is [this] button up or down?"
      pressed = pygame.key.get_pressed()
      for player in self.players:
        player.update(pressed)

      pygame.display.update()
      self.clock.tick(30)

if __name__ == '__main__':
  Game().run()
