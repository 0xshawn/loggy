# -*- coding: utf-8 -*-


import json


class Config(object):

    def __init__(self, config_path):
        with open(config_path) as file_content:
            config_json = json.load(file_content)

        self.pid_file = config_json.get('pid_file', '/tmp/loggy.pid')

        # TODO: config from shell args
        self.debug = True
