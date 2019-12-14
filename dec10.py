import numpy as np
import math

inputAsteroids = """#..#....#...#.#..#.......##.#.####
#......#..#.#..####.....#..#...##.
.##.......#..#.#....#.#..#.#....#.
###..#.....###.#....##.....#...#..
...#.##..#.###.......#....#....###
.####...##...........##..#..#.##..
..#...#.#.#.###....#.#...##.....#.
......#.....#..#...##.#..##.#..###
...###.#....#..##.#.#.#....#...###
..#.###.####..###.#.##..#.##.###..
...##...#.#..##.#............##.##
....#.##.##.##..#......##.........
.#..#.#..#.##......##...#.#.#...##
.##.....#.#.##...#.#.#...#..###...
#.#.#..##......#...#...#.......#..
#.......#..#####.###.#..#..#.#.#..
.#......##......##...#..#..#..###.
#.#...#..#....##.#....#.##.#....#.
....#..#....##..#...##..#..#.#.##.
#.#.#.#.##.#.#..###.......#....###
...#.#..##....###.####.#..#.#..#..
#....##..#...##.#.#.........##.#..
.#....#.#...#.#.........#..#......
...#..###...#...#.#.#...#.#..##.##
.####.##.#..#.#.#.#...#.##......#.
.##....##..#.#.#.......#.....####.
#.##.##....#...#..#.#..###..#.###.
...###.#..#.....#.#.#.#....#....#.
......#...#.........##....#....##.
.....#.....#..#.##.#.###.#..##....
.#.....#.#.....#####.....##..#....
.####.##...#.......####..#....##..
.#.#.......#......#.##..##.#.#..##
......##.....##...##.##...##......"""
asteroids = np.zeros((34,34), dtype='U')

# inputAsteroids = """.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##"""
# asteroids = np.zeros((20,20), dtype='U')

#############################################################################################
for i, line in enumerate(inputAsteroids.split("\n")):
    for j, col in enumerate(line):
        asteroids[i,j] = col

# part 1
maximum = (0,(0,0))
for originRow, originCol in np.ndindex(asteroids.shape):
    if asteroids[originRow, originCol] == '#':
        seen = set()
        for row, col in np.ndindex(asteroids.shape):
            if asteroids[row,col] == '#' and (row, col) != (originRow, originCol):
                y = originRow - row
                x = col - originCol
                angle = math.atan2(y,x)
                seen.add(angle)
        maximum = max(maximum, (len(seen),(originCol, originRow)))
print(maximum)

#part2
def get200(angles, seen):
    total = 0
    counter = 0
    curr = 0
    while total < 200:
        angle = angles[counter % len(angles)]
        if angle in seen:
            coords = list(seen[angle])
            curr = coords.pop(0)
            if coords == []:
                del seen[angle]
            else:
                seen[angle] = np.array(curr)
            total += 1
        counter += 1
    return curr

bestLoc = maximum[1]
seen = {}
for row, col in np.ndindex(asteroids.shape):
    if asteroids[row,col] == '#' and (col, row) != bestLoc:
        y = bestLoc[1] - row
        x = col - bestLoc[0]
        angle = math.atan2(y,x)
        seen.setdefault(angle,[]).append((col, row))

# sort angles 
npBestLoc = np.array(bestLoc)
for k, v in seen.items():
    arr = np.array(v)
    newList = arr - npBestLoc
    dist = np.sum(np.power(newList, 2), axis=1)
    seen[k] = arr[dist.argsort()]


angles = sorted(seen.keys(),reverse=True)
startIndex = angles.index(math.pi/2)
angles = angles[startIndex:] + angles[:startIndex]
print(get200(angles,seen))