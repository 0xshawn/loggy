# -*- coding: utf-8 -*-


import datetime


class ArgumentError(Exception):
    pass


class CountFrequency(object):

    def __init__(self, count, days=None, hours=None, minutes=None):
        """
        Count frequency of n/t, n for count, and t for duration
        """
        if not (days or hours or minutes):
            return ArgumentError('At least one argument is required.')

        self.max_items = 0
        if days:
            self.max_items += days * 24 * 60
        if hours:
            self.max_items += hours * 60
        if minutes:
            self.max_items += minutes

        self.threshold_count = count
        self.data = {}
        self.timedelta = datetime.timedelta()
        if days:
            self.timedelta += datetime.timedelta(days=days)
        if hours:
            self.timedelta += datetime.timedelta(hours=hours)
        if minutes:
            self.timedelta += datetime.timedelta(minutes=minutes)

    def add(self, time):
        time = "%s-%s-%s %s:%s" % (time.year, time.month, time.day,
                                   time.hour, time.minute)
        if time in self.data:
            self.data[time] += 1
        else:
            self.data[time] = 1

        self.clean()
        self.check()

    def clean(self):
        start = datetime.datetime.now()
        end = start - self.timedelta
        will_clean = []
        for i in self.data:
            i_date = datetime.datetime.strptime(i, "%Y-%m-%d %H:%M")
            if i_date < end:
                will_clean.append(i)

        for i in will_clean:
            del self.data[i]

    def check(self):
        count = 0
        for i in self.data:
            count += self.data[i]

        if count >= self.threshold_count:
            self.alert()

        print count

    def alert(self):
        print '!!! do alert'
