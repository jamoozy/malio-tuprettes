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
import json

from pygame import *

from debug import debug as dbg
from debug import warning as wrn
from debug import error as err


DEFAULT_PATH = os.path.join(os.path.expanduser('~'), '.malio-tuprettes')
'''The default path to the config file.'''

DEFAULT_CONFIG = {
  "players": [ {
    "up": K_e,
    "down": K_d,
    "left": K_s,
    "right": K_f,
    "action": K_j,
    "jump": K_k,
    "special": K_i,
    "spin": K_l
  } ]
}
'''The default configuration for Malio Tuprettes.'''

class PlayerConfig():
  '''Configs a player.'''

  attrs = ["up", "down", "left", "right", "action", "jump", "special", "spin"]
  '''The attributes in that relate to player controls.'''

  def __init__(self, obj):
    '''Builds a config object for a player.  Creates and returns an object.  The
    following object describes the hash expected:

    {
      "up": keycode,
      "down": keycode,
      "left": keycode,
      "right": keycode,
      "jump": keycode,
      "action": keycode,
      "special": keycode,
      "spin": keycode,
    }

    For the above examples, `keycode` can either be the key code value returned
    by, e.g., `pygame.K_a` (which is 97), the name of the letter (e.g., "a",
    which is treated as the same keycode), the name of the python event (e.g.,
    "K_a"), or the full name of the python variable (e.g., "pygame.K_a").

    Args:
      obj, dict: A player config file as described above.

    Returns:
      The config.
    '''
    for attr in self.attrs:
      val = obj[attr]
      if isinstance(val, int):
        setattr(self, attr, val)
      elif isinstance(val, str):
        if val.startswith("pygame."):
          setattr(self, attr, eval(val[7:]))
        elif val.startswith("K_"):
          setattr(self, attr, eval(val))
        else:
          setattr(self, attr, eval("K_" + val))
      elif val is None:
        setattr(self, attr, None)
        wrn('player config is blank: "%s"' % attr)
      else:
        raise ValueError("Unrecognized key code: %s" % val)


  def _to_dict(self):
    return { attr: getattr(self, attr) for attr in self.attrs }


class Config:
  '''Represents a config file for this game.'''

  def __init__(self, obj):
    '''Initializes the config file.

    Args:
      obj, dict: The configuration object.
    '''
    # Build all four players.
    PLAYER_KEYS = ['p1', 'p2', 'p3', 'p4']
    for i, key in enumerate(PLAYER_KEYS):
      if key not in obj:
        break

      self.p[i] = PlayerConfig(obj[key])

    if obj.keys():
      print 'Warning: %d unused values detected:\n %s' % (len(obj), obj.keys())

  def _to_dict(self):
    return {
      "players": [p._to_dict() for p in self.p],
      "debug": debug.mode
    }

  def save(self, fname=None):
    '''Saves this config to the file.  If no file given, uses this `Config`'s
    internal fname.

    Args:
      fname, str: The file name to save to.
    '''
    with open(fname, 'w') as f:
      f.writelines(json.dumps(c))


def load(cls, fname=None):
  '''Loads a config file from the specified file name, `fname`.  If `fname` is
  not specified, uses `DEFAULT_PATH`.

  Args:
    fname, str: The file name.

  Throws:
    ValueError: If the config file was malformatted.
  '''
  fname = fname or DEFAULT_PATH

  with open(args.cf) as f:
    file_contents = "".join(f.readlines())
  dbg('got', file_contents)

  c = config.Config(json.loads(file_contents))
