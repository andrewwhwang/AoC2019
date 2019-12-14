from itertools import combinations
from functools import reduce
from math import gcd

class Moon:
    def __init__(self, x, y, z):
        self.pos = [x,y,z]
        self.vel = [0,0,0]

    def update(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def getEnergy(self):
        potential = sum([abs(self.pos[i]) for i in range(3)])
        kinetic = sum([abs(self.vel[i]) for i in range(3)])
        return potential * kinetic

def oneStep(moons):
    for moon1, moon2 in combinations(moons, 2):
        for i in range(3):
            if moon1.pos[i] < moon2.pos[i]:
                moon1.vel[i] += 1
                moon2.vel[i] -= 1
            elif moon1.pos[i] > moon2.pos[i]:
                moon1.vel[i] -= 1
                moon2.vel[i] += 1

    for moon in moons:
        moon.update()

    return moons

def lcm(num1, num2):
    return (num1*num2) // gcd(num1, num2)

def parse(raw):
    lines = raw.split("\n")
    locs = [line[1:-1].split(", ") for line in lines]
    moons = [Moon(*[int(pos[2:]) for pos in loc])for loc in locs]
    return moons

raw= """<x=17, y=-7, z=-11>
<x=1, y=4, z=-1>
<x=6, y=-2, z=-6>
<x=19, y=11, z=9>"""

# part 1###################################################
moons = parse(raw)

for t in range(1000):
    moons = oneStep(moons)

totalEnergy = sum([moon.getEnergy() for moon in moons])
print(totalEnergy)

# part 2###################################################
moons = parse(raw)
initial = [[moon.pos[i] for moon in moons] for i in range(3)]
cycles = [0,0,0]
t = 0

while not all(cycles):
    moons = oneStep(moons)
    t += 1
    for i in range(3):
        if cycles[i] != 0:
            continue
        poss = [moon.pos[i] for moon in moons]
        vels = [moon.vel[i] for moon in moons]
        if poss == initial[i] and vels == [0] * len(moons):
            cycles[i] = t

print(reduce(lcm,cycles))