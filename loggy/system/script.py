# -*- coding: utf-8 -*-

"""
    Provide command `loggy`
"""

import os

from loggy import Loggy
from loggy.config.config import Config


def main():
    print 'Start loggy daemon...'
    config = Config('/etc/loggy.json')
    pid_file = config.pid_file
    loggy_daemon = Loggy(pid_file)

    # whether daemon or not
    if config.debug:
        loggy_daemon.run(config)
    else:
        if os.path.isfile(pid_file):
            loggy_daemon.stop()
        else:
            loggy_daemon.start(config)


if __name__ == '__main__':
    main()
