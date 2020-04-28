grid = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

# Output: 2

import collections
def zom(grid):
    zombies = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]

    time = 0
    neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

    while True:
        newZombies = []
        for (i, j) in zombies:
            for x, y in neighbors:
                di = i + x
                dj = j + y
                if 0 <= di < len(grid) and 0 <= dj < len(grid[0]) and grid[di][dj] == 0:
                    grid[di][dj] = 1
                    newZombies.append((di, dj))
                    
        zombies = newZombies
        if not zombies:
            break
        time += 1
    print(time)



zom(grid)