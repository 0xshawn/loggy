# -*- coding: utf-8 -*-

from .system.daemon import Daemon
from .core import Loop


class Loggy(Daemon):

    def run(self, config):
        app = Loop(config)
        app.start()
