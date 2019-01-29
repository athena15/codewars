# https://www.codewars.com/kata/vector-class/train/python

class Vector:

    def __init__(self, points):
        self.points = points
        # etc, etc.

        if type(points) is not type(list):
            raise ValueError('Not a list')

    def check_valid_vectors(self, other=None):
        assert type(self) == Vector

        if other is not None:
            if not len(self) == len(other):
                raise ValueError('Length of vectors does not match.')

    def __str__(self):
        x = []
        for i in self.points:
            if not str(i).isspace():
                x.append(i)
        return str(tuple(x)).replace(' ', '')

    def __len__(self):
        return len(self.points)

    def __add__(self, other):
        if not len(self) == len(other):
            raise ValueError('Length of vectors does not match.')
        return Vector([x + y for x, y in zip(self.points, other.points)])

    def add(self, other):
        if not len(self) == len(other):
            raise ValueError('Length of vectors does not match.')
        return Vector([x + y for x, y in zip(self.points, other.points)])

    def subtract(self, other):
        return Vector([x - y for x, y in zip(self.points, other.points)])

    def dot(self, other):
        return int(sum([x * y for x, y in zip(self.points, other.points)]))

    def norm(self):
        return sum([x ** 2 for x in self.points]) ** (1 / 2)

    def equals(self, other):
        return self.points == other.points


if __name__ == '__main__':
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([10, 20, 30])
    vector1.add(vector2)
