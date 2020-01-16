import math
import random
import time

from Labs.Lab1.asteroid import Asteroid
from Labs.Lab1.vector import Vector


class Controller:
    def __init__(self):
        self.asteroids = []
        for _ in range(1, 5):
            radius = random.randint(1, 5)
            circum = 2*math.pi*radius
            pos = Controller.init_pos()
            vel = Controller.init_vel()

            self.asteroids.append(Asteroid(circum, pos, vel))

    def simulate(self, seconds):
        start = time.time()
        time.sleep(math.ceil(start) - start)
        start = time.time()
        print('Simulation start time:', start)

        count = 1
        for asteroid in self.asteroids:
            print('Asteroid', count, 'Moved! Old pos:', asteroid.get_pos(), '-> New pos:', end=' ')

            for i in range(seconds):
                asteroid.pos.add(asteroid.vel)

            print(asteroid.get_pos())
            count += 1

    @staticmethod
    def init_pos():
        x = random.randint(0, 101)
        y = random.randint(0, 101)
        z = random.randint(0, 101)

        return Vector((x, y, z))

    @staticmethod
    def init_vel():
        x = random.randint(-5, 6)
        y = random.randint(-5, 6)
        z = random.randint(-5, 6)

        return Vector((x, y, z))

