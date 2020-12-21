import re

class Ship():
    def __init__(self, facing):
        self.facing = facing
        self.compass = {
            0: 'N',
            90: 'E',
            180: 'S',
            270: 'W'
        }
        self.north_south = 0
        self.east_west = 0

    def __str__(self):  
        return f'facing: {self.compass[self.facing]}, north: {self.north_south}, east: {self.east_west}, distance: {self.distance()}'

    def move(self, direction, distance):
        if direction == 'N':
            self.north_south += distance
        if direction == 'S':
            self.north_south -= distance
        if direction == 'E':
            self.east_west += distance
        if direction == 'W':
            self.east_west -= distance
        if direction == 'F':
            self.move(self.compass[self.facing], distance)
        if direction == 'R':
            self.facing += distance
            self.facing %= 360
        if direction == 'L':
            self.facing -= distance
            self.facing %= 360
    def distance(self):
        return abs(self.north_south) + abs(self.east_west)

s = Ship(90)

with open("./input.txt", "r") as f:
    for line in f:
        s.move(line[0:1], int(line[1:len(line)]))

# s.move('N', 3)
# s.move('F', 3)
# s.move('R', 90)
# s.move('F', 10)
print(s)
