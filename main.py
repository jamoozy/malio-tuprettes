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
# Malio Tuprettes is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Malio Tuprettes. If not, see http://www.gnu.org/licenses/.


import os
import sys

import pygame
from pygame.locals import *

import config
import logger
from logger import debug as dbg


class Game(object):
  '''The game to run.'''
  def __init__(self, config):
    self.config = config
    self.players = [Player(pconf) for pconf in config.players]
    self.world = World()

    pygame.init()

    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Game')
    self.bg_color = pygame.Color(0, 0, 220)

    # TODO Load additional textures and things.

  def run(self):
    '''Runs the game.'''
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


def main(args):
  import json
  from argparse import ArgumentParser

  parser = ArgumentParser(description="")
  parser.add_argument("-f", "--config-file", dest="cf",
                      help="Read config from FILE", metavar="FILE",
                      default=config.DEFAULT_PATH)
  parser.add_argument("-d", "--debug", help="Turn on debugging info.",
                      type=bool, default=False)
  args = parser.parse_args(args)

  # Set up debugging state.
  if args.debug:
    debug.enable()

  # Load config file.
  if os.path.isfile(args.cf):
    try:
      c = config.load(args.cf)
    except config.ParseError as ve:
      print 'Could not decode the config file: "%s" \n:%s.\nContents:\n%s' % (
              args.cf, ve.message, file_contents)
      sys.exit(-1)
  else:
    c = config.load()
    c.save()

  Game(config).run()


if __name__ == '__main__':
  main(sys.argv[1:])
