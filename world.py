# Copyright 2012 Andrew "Jamoozy" Correa
#
# This file is part of Malio Tuprettes.
#
# Malio Tuprettes is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Mali Tuprettes is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Malio Tuprettes. If not, see http://www.gnu.org/licenses/.

import cPickle as pickle

'''This module contains all the things needed to make a world.'''

class Block:
  '''Superclass of all block types.'''
  def __init__(self):
    pass

  def paint(self, screen):
    pass

class Chunk:
  '''One "chunk" of the level, to be loaded at any one time.'''
  def __init__(self):
    pass

  def paint(self, screen):
    pass


class Level:
  '''A level is a series of chunks in a 2D array.'''
  def __init__(self):
    self.pos = (0,0)
    self.chunks = [[]]

  def save(self, fname):
    '''fname: the name of the file stored in ... some format.'''
    pickle.Pickler(self, open(fname, 'w'))

  def paint(self, screen):
    for i in xrange(max(0, self.progress-1), min(self.progress+1,len(self.chunks))):
      self.chunks[i].paint(screen)

  @staticmethod
  def loadFrom(fname):
    '''Loads and creates a new level from the file.'''
    return pickle.Unpickler(open(fname, 'r'))

