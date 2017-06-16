#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""

log mod
"""

import threading
import logging
from config.log_config import log_path
from config.log_config import log_datefmt
from config.log_config import log_format
from config.log_config import log_level
from config.log_config import log_filemode
class LogMod:

    def tests(self):
        logging.basicConfig(level=logging.DEBUG,
                            format=log_format,
                            datefmt=log_datefmt,
                            filename=log_path,
                            filemode=log_filemode)

        logging.warning("check check check")


LogMod().tests()