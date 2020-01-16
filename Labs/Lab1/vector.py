class Vector:
    def __init__(self, v):
        self.x = v[0]
        self.y = v[1]
        self.z = v[2]

    def add(self, v2):
        self.x += v2.x
        self.y += v2.y
        self.z += v2.z

    def __str__(self):
        x = str(self.x)
        y = str(self.y)
        z = str(self.z)
        s = '(' + x + ', ' + y + ', ' + z + ')'

        return s
