# -*- coding=utf-8 -*-
# Library: pyFFmpeg
# Author: dongrixinyu
# License: MIT
# Email: dongrixinyu.66@gmail.com
# Github: https://github.com/dongrixinyu/pyFFmpeg
# Description: a simple Python wrapper for FFmpeg.'
# Website: http://www.jionlp.com

import os
import pdb
import time
import ctypes

__version__ = '1.0.1'

HOME_DIR = os.path.expanduser('~')
LOG_DIR = os.path.join(HOME_DIR, '.cache/pyFFmpeg')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

from pyFFmpeg.stream_parser import StreamParser
