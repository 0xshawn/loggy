# -*- coding: utf-8 -*-

from time import sleep


class Loop(object):

    def __init__(self, config):
        pass

    def start(self):
        while(True):
            print 'one loop'
            sleep(5)
