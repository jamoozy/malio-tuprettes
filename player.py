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


class Player:
  '''Represents a player.  Keeps track of player's state.'''
  def __init__(self, pnum, pconfig=None):
    '''Creates a new player with the given ID.'''
    self.number = pnum
    self.config(config)

  def config(self, config):
    '''Sets player config to config.'''
    pass

  def update(self, pressed):
    '''Updates the player based on what all was pressed.'''
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



################################################################################
#                                  Power Ups                                   #
################################################################################

class PowerUp:
  '''Common super-class for all power ups.'''
  def __init__(self):
    pass

class
