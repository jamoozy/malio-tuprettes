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


import mock
import nose

from pygame import *

import config



################################################################################
#                       More Sohpisticated Mock Objects                        #
################################################################################


class PMPlayerConfig(config.PlayerConfig):
  '''Partical mock of `PlayerConfig`.'''
  def __init__(self, **kwargs):
    '''Initializes this object.'''
    self.kwargs = kwargs
    for kw in kwargs:
      setattr(self, kw, kwargs[kw])

  def patch(self, kwargs):
    '''Patches all the attributes of this object with the names enumerated in
    the args.

    Args:
      args, str: Names of the attributes.

    Returns:
      `self`, for convenience.
    '''
    return self.kwargs.update(kwargs)

  def __getattr__(self, attr):
    try:
      return self.kwargs[attr]
    except KeyError:
      return super(object).__getattribute__(attr)


################################################################################
#                                 PlayerConfig                                 #
################################################################################

player_config_objs = {
  # Real-ish config.
  "real": (["up", "down", "left", "right", "ctrl", "space", "z", "x"],
           [K_UP, K_DOWN, K_LEFT, K_RIGHT, KMOD_CTRL, K_SPACE, K_z, K_x]),

  # "real" with all caps
  "REAL": (["UP", "DOWN", "LEFT", "RIGHT", "CTRL", "SPACE", "Z", "X"],
           [K_UP, K_DOWN, K_LEFT, K_RIGHT, KMOD_CTRL, K_SPACE, K_z, K_x]),

  # Same as above, but altered a bit.
  "altered": (["e", "d", "s", "r", "j", "k", "l", "i"],
              [K_e, K_d, K_s, K_r, K_j, K_k, K_l, K_i]),

  # "altered" with all caps
  "ALTERED": (["e", "d", "s", "r", "j", "k", "l", "i"],
              [K_e, K_d, K_s, K_r, K_j, K_k, K_l, K_i]),

  # The numerical codes for a-h (97 - 104).
  "numeric": (range(97, 97 + 8), [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h]),

  # The string values "a"-"h".
  "letter": (map(chr, range(97, 97 + 8)),
             [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h]),

  # The string values "A"-"H" (wrong case -- should work anyway)
  "LETTER": (map(chr, range(65, 65 + 8)),
             [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h]),

  # The string values "K_a"-"K_h".
  "K_letter": (["K_" + chr(i) for i in range(97, 97 + 8)],
               [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h]),

  # The string values "K_A"-"K_H" (wrong case -- should work anyway).
  "K_LETTER": (["K_" + chr(i) for i in range(65, 65 + 8)],
               [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h]),

  # The string values "pygame.K_a"-"pygame.K_h".
  "pygame": (["pygame.K_" + chr(i) for i in range(97, 97 + 8)],
             [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h]),

  # The string values "pygame.K_a"-"pygame.K_h".
  "PYGAME": (["pygame.K_" + chr(i) for i in range(65, 65 + 8)],
             [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h])
}

# ---- PlayerConfig.__init__() ----

def test_player_config___init__():
  '''Tests all the types of keycode values this should accept.'''
  for obj, exp in player_config_objs.itervalues():
    arg = dict(zip(config.PlayerConfig.attrs, obj))
    exp = zip(config.PlayerConfig.attrs, exp)
    yield _player_config___init__, arg, exp

def test_player_config___init___ParseError():
  '''Tests other keycode values throw `ParseError`s.'''
  bogus_values = "wut", [], {}, [K_a], 
  for bogus_value in bogus_values:
    obj = { attr: bogus_value for attr in config.PlayerConfig.attrs }
    yield _player_config___init__ParseError, obj, bogus_value

def _player_config___init__(obj, exp):
  '''Tests the config.PlayerConfig constructur.  Assumes the letters "a"-"h" are
  being assigned to the variables in `config.PlayerConfig.attrs` in the order
  they appear in the list.

  Args:
    objs, dict: The object to initialize a config.PlayerConfig with.
    exp, [(str, keycode)]: The expected relation between attributes and
                           keycodes.

  Returns:
    The created `PlayerConfig` (for error messages).
  '''
  pc = config.PlayerConfig(obj)
  for attr, pyvar in exp:
    assert getattr(pc, attr) == pyvar, "attr:%s exp:%s was:%s" % (
      attr, pyvar, getattr(pc, attr))
  return pc

def _player_config___init__ParseError(obj, bogus_value):
  try:
    pc = _player_config___init__(obj, None)
    assert 0, 'Did not throw ParseError for "%s", got %s' % (bogus_value, pc)
  except config.ParseError:
    pass # expected


# ---- PlayerConfig._to_dict() ----

good_pm_dicts = [
  dict(zip(config.PlayerConfig.attrs, player_config_objs["real"][1])),
  dict(zip(config.PlayerConfig.attrs, player_config_objs["REAL"][1])),
]

def test_player_config__to_dict():
  for pm_dict in good_pm_dicts:
    pm = PMPlayerConfig(**pm_dict)
    yield _player_config__to_dict, pm, pm_dict


def _player_config__to_dict(pm, pm_dict):
  '''Compares the dictionary returned by `pm._to_dict` and `pm_dict`.

  Args:
    pm, PMPlayerConfig: The PLayerConfig to test.
    pm_dict, dict: The expected dictionary.
  '''
  rtn = pm._to_dict()
  assert rtn == pm_dict, 'Returned:%s expected:%s' % (rtn, pm_dict)

if __name__ == '__main__':
  nose.main()
