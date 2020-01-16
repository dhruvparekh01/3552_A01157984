class Asteroid:
    def __init__(self, circum, pos, vel):
        self.circumference = circum
        self.pos = pos
        self.vel = vel

    def __str__(self):
        return ' currently at' + str(self.pos) + ' and moving at ' + str(self.vel) + ' metres per second ' + '.It has a circumference of ' + str(self.circumference)

    def get_pos(self):
        return self.pos

    def set_pos(self, new_pos):
        self.pos = new_pos

    def get_vel(self):
        return self.pos

    def set_vel(self, new_pos):
        self.pos = new_pos

    position = property(get_pos, set_pos)
    velocity = property(get_vel, set_vel)

