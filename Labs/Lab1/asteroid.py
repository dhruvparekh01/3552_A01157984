from Labs.Lab1.vector import Vector
import time
import math
import random


class Asteroid:
    def __init__(self, circum, pos, vel):
        self.circumference = circum
        self.pos = pos
        self.vel = vel

    def __str__(self):
        return 'currently at', self.pos, 'and moving at', self.vel, 'metres per second', '.It has a circumference of', self.circumference

    def get_pos(self):
        return '(' + str(self.pos.x) + ', ' + str(self.pos.y) + ', ' + str(self.pos.z) + ')'

