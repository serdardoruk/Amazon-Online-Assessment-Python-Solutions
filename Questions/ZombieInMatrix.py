"""
Zombie In Matrix
BFS SOLUTION
"""
"""
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]

 """


def minHour(grid):
	rows = len(grid)
	columns = len(grid[0])

	if not rows or not columns:
		return 0

	q = [[i,j] for i in range(rows) for j in range(columns) if grid[i][j]==1]
	directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
	time = 0

	while True:
		new = []
		for [i, j] in q:
			for d in directions:
				ni, nj = i + d[0], j + d[1]
				if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
					grid[ni][nj] = 1
					new.append([ni, nj])
		q = new
		if not q:
			break
		time += 1

	return time


grid = [[0, 1, 1, 0, 1],[0, 1, 0, 1, 0],[0, 0, 0, 0, 1],[0, 1, 0, 0, 0]]

print(minHour(grid))





def zombiesTrans(grid):
	rows = len(grid)
	cols = len(grid[0])

	zombies = [(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 1]
	directions = [(0,1), (0,-1), (1,0), (-1,0)]
	times = 0

	while True:
		new = []

		for i, j in zombies:
			for r, c in directions:
				di, dj = i + r, j + c
				if 0 <= di < rows and 0 <= dj < cols and grid[di][dj] == 0:
					grid[di][dj] = 1
					new.append((di,dj))
		zombies = new
		if not zombies:
			break
		times += 1

	return times
grid = [[0, 1, 1, 0, 1],[0, 1, 0, 1, 0],[0, 0, 0, 0, 1],[0, 1, 0, 0, 0]]
print(zombiesTrans(grid))














