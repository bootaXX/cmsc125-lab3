import os
import time


class Job(object):
    """docstring for Job"""
    def __init__(self, jobstream, time, jobsize):
        super(Job, self).__init__()
        self.jobstream = jobstream
        self.time = time
        self.jobsize = jobsize


class Block(object):
    """docstring for Block"""
    def __init__(self, name, size):
        super(Block, self).__init__()
        self.name = name
        self.size = size
