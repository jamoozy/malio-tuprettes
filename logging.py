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


LEVEL_SILENT = -2
'''Do not print anything.  Not ever.'''
LEVEL_QUIET = -1
'''Only print error messages.'''
LEVEL_DEFAULT = 0
'''Only print error and warning messages.'''
LEVEL_VERBOSE = 1
'''Print verbose messages.'''
LEVEL_DEBUG = 2
'''Print debugging messages.'''

_level = LEVEL_DEBUG
'''The logging level.  This value dictates when this module prints. the
arguments passed to its methods.'''


def error(*args):
  '''Prints the message(s) with the string "Error:" prepended unless the current
  level is set to `LEVEL_SILENT`.

  Args:
    args, list: The argument to print.
  '''
  if _level > LEVEL_SILENT:
    print 'Error:', ' '.join(args)

def warning(*args):
  '''Prints the message(s) with the string "Warning:" prepended iff the current
  level is set to `LEVEL_QUIET` or greater.

  Args:
    args, list: The argument to print.
  '''
  if _level >= LEVEL_DEFAULT:
    print 'Warning:', ' '.join(args)

def verbose(*args):
  '''Prints the message(s) iff the current level is set to `LEVEL_VERBOSE` or
  greater.

  Args:
    args, list: The argument to print.
  '''
  if _level >= LEVEL_VERBOSE:
    print ' '.join(args)

def debug(*args):
  '''Prints the message(s) iff the current level is set to `LEVEL_DEBUG` or
  greater.

  Args:
    args, list: The argument to print.
  '''
  if _level >= LEVEL_DEBUG:
    print ' '.join(args)

def set_level(lvl):
  '''Sets the debugging value.

  Args:
    lvl, int: The printing level.

  Raises:
    ValueError: iff `lvl` is not a valid logging level.
  '''
  if lvl not in [
      LEVEL_SILENT, LEVEL_QUIET, LEVEL_DEFAULT, LEVEL_VERBOSE, LEVEL_DEBUG]:
    raise ValueError("Invalid logging level: %d" % lvl)
  _level = lvl
