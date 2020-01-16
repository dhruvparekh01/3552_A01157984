import math
import random
import time

from Labs.Lab1.asteroid import Asteroid
from Labs.Lab1.vector import Vector


class Controller:
    NO_OF_ASTEROIDS = 100
    MAX_RADIUS = 5
    POSITION_RANGE = 100

    def __init__(self):
        """
        Initializes a controller object. It contains a list of 100 asteroids.
        """

        self.asteroids = []
        for _ in range(1, Controller.NO_OF_ASTEROIDS+1):
            radius = random.randint(1, Controller.MAX_RADIUS+1)
            circum = 2*math.pi*radius
            pos = Controller.init_pos()
            vel = Controller.init_vel()

            self.asteroids.append(Asteroid(circum, pos, vel))

    def simulate(self, seconds):
        start = time.time()
        time.sleep(math.ceil(start) - start)  # pause the thread until time is nearly in an integer value
        start = time.time()
        print('Simulation start time:', start)

        count = 1
        for asteroid in self.asteroids:
            print('Asteroid', count, 'Moved! Old pos:', asteroid.position, '-> New pos:', end=' ')

            for i in range(seconds):  # will be executed same number of times as value of seconds
                asteroid.position.add(asteroid.vel)  # add velocity to position every time executed

            print(asteroid.position)

            print('Asteroid ', count, end='')
            print(asteroid)
            count += 1

    @staticmethod
    def init_pos():
        """
        Helper method to initialize position of an asteroid to a random vector
        :return: position -> Vector
        """
        x = random.randint(0, Controller.POSITION_RANGE+1)
        y = random.randint(0, Controller.POSITION_RANGE+1)
        z = random.randint(0, Controller.POSITION_RANGE+1)

        return Vector((x, y, z))

    @staticmethod
    def init_vel():
        """
        Helper method to initialize velocity of an asteroid to a random vector
        :return: velocity -> Vector
        """
        x = random.randint(-Controller.MAX_RADIUS, Controller.MAX_RADIUS+1)
        y = random.randint(-Controller.MAX_RADIUS, Controller.MAX_RADIUS+1)
        z = random.randint(-Controller.MAX_RADIUS, Controller.MAX_RADIUS+1)

        return Vector((x, y, z))

