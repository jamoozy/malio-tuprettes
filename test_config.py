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


import nose

from pygame import *

import config



################################################################################
#                                 PlayerConfig                                 #
################################################################################

player_config_objs = {
  # The numerical codes for a-h (97 - 104).
  "numeric": dict(zip(config.PlayerConfig.attrs, range(97, 97 + 8))),

  # The string values "a"-"h".
  "letter": dict(zip(config.PlayerConfig.attrs, map(chr, range(97, 97 + 8)))),

  # The string values "K_a"-"K_h".
  "K_letter": dict(zip(config.PlayerConfig.attrs,
                       ["K_" + chr(i) for i in range(97, 97 + 8)])),

  # The string values "pygame.K_a"-"pygame.K_h".
  "pygame": dict(zip(config.PlayerConfig.attrs,
                     ["pygame.K_" + chr(i) for i in range(97, 97 + 8)]))
}


def test_player_config_init():
  # Test all the types of configurations this should accept.
  for obj in player_config_objs.itervalues():
    yield _player_config_init, obj


def _player_config_init(obj):
  '''Tests the config.PlayerConfig constructur.  Assumes the letters "a"-"h" are
  being assigned to the variables in `config.PlayerConfig.attrs` in the order
  they appear in the list.

  Args:
    objs, dict: The object to initialize a config.PlayerConfig with.
  '''
  pc = config.PlayerConfig(obj)
  for attr, pyvar in zip(pc.attrs, [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h]):
    assert getattr(pc, attr) == pyvar, "attr:%s exp:%s was:%s" % (
      attr, pyvar, getattr(pc, attr))




if __name__ == '__main__':
  from sys import stderr, exit
  nose.main()
