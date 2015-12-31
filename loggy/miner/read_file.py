# -*- coding: utf-8 -*-


import time
import datetime

#from .data_type import CountFrequency
from data_type import CountFrequency

filename = '/usr/local/var/log/nginx/error.log'
file = open(filename,'r')

cf = CountFrequency(1, minutes=1)

where = file.seek(0, 2)
while True:
    line = file.readline()
    if not line:
        time.sleep(1)
        where = file.tell()
        file.seek(where)
    else:
        print '>>> one error'
        cf.add(datetime.datetime.now())
