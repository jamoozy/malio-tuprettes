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
from tempfile import mkstemp


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


class FileLogger():
  '''A file logger; an object that logs output to a file.'''
  prefix = "mt"
  suffix = ".log"

  def __init__(self, level, prev=None, prefix=None, suffix=None, **kwargs):
    '''Initializes the logger.  Default values are provided.

    Args:
      level, int: The logging level.
      prev, FileLogger: Previously initialized `FileLogger` (if any).
      kwargs, hash: The kwargs to pass to `tempfile.mkstemp`.

    Raises:
      ValueError: If `prev` is anything but a FileLogger or None.
    '''
    self.level = level
    self.prefix = prefix or self.prefix
    self.suffix = suffix or self.suffix
    if prev is None:
      fd, self.fname = mkstemp(self.suffix, self.prefix, **kwargs)
      os.close(fd)
    elif isinstance(prev, FileLogger):
      self.fname = prev.fname
    else:
      raise ValueError("prev:%s not a FileLogger" % prev)

  def log(self, *lines):
    '''Logs the lines.

    Args:
      lines, [str]: List of strings to log (or empy).
    '''
    with open(self.fname, 'a') as f:
      f.writelines([str(e) + '\n' for e in lines])

file_logger = FileLogger()
'''The file logger this module uses to log files.'''


def init_file_logger(**kwargs):
  '''Inits the `file_logger` with the passed `kwargs`.  If this function is
  never called, 

  Args:
    kwargs: The kwargs to pass on to `FileLogger()`.

  Returns:
    The newly-created `file_logger` object.
  '''
  if "level" not in kwargs:
    kwargs["level"] = _level
  file_logger = FileLogger(prev=file_logger, **kwargs)
  return file_logger

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
