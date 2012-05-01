#!/usr/bin/python
#
# Copyright 2012 Andrew "Jamoozy" Correa
#
# This file is part of Malio Tuprettes.
#
# Malio Tuprettes is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Foobar is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Malio Tuprettes. If not, see http://www.gnu.org/licenses/.


import pygame, sys
from pygame.locals import *

class Player:
  '''Represents a player.  Keeps track of player's state.'''
  def __init__(self, pnum):
    self.number = pnum

  def update(self, pressed):
    if pressed[pygame.K_s]:
      self._left()
    elif pressed[pygame.K_d]:
      self._down()
    elif pressed[pygame.K_f]:
      self._right()
    elif pressed[pygame.K_e]:
      self._up()
    elif pressed[pygame.K_j]:
      self._action()
    elif pressed[pygame.K_k]:
      self._jump()
    elif pressed[pygame.K_i]:
      self._special()
    elif pressed[pygame.K_l]:
      self._spin()

  def draw(self, window):
    pass

class Chunk:
  def __init__(self):
    pass

  def paint(self, screen):
    pass

class World:
  def __init__(self):
    self.pos = (0,0)
    self.chunks = [[]]

  def load(self, fname):
    '''fname: the name of the file stored in ... some format.'''
    pass

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
  Game(1).run()
