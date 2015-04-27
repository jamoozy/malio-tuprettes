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
    for attr in main.PlayerConfig.attrs:
      setattr(self.controls, attr, getattr(config, attr))

  def update(self, pressed):
    '''Updates the player's state based on which buttons were pressed.

    Args:
      The buttons that were pressed.
    '''
    for attr in main.PlayerConfig.attrs:
      if pressed[getattr(self.controls, attr)]:
        getattr(self, '_' + attr).__call__()

  def draw(self, window):
    '''Draws the user.'''
    pass



################################################################################
#                                  Power Ups                                   #
################################################################################

class PowerUp:
  '''Common super-class for all power ups.'''
  def __init__(self):
    pass
