"""
Number of Clusters
https://leetcode.com/problems/number-of-islands/ 200. Number of Islands
"""
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
'''
# Example 1:
# Input:
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# Output: 1
#
# Example 2:
# Input:
# grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# Output: 3


def numOfIslands(grid):
	visited = set()
	count = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if (i, j) not in visited and  grid[i][j] == "1":
				count += 1
				queue = [(i, j)]
				while queue:
					(x, y) = queue.pop()
					visited.add((x, y))
					if x - 1 >= 0 and (x - 1, y) not in visited and grid[x - 1][y] == "1":
						queue.append((x - 1, y))
					if x + 1 < len(grid) and (x + 1, y) not in visited and grid[x + 1][y] == "1":
						queue.append((x + 1, y))
					if y - 1 >= 0 and (x, y - 1) not in visited and grid[x][y - 1] == "1":
						queue.append((x, y - 1))
					if y + 1 < len(grid[0]) and (x, y + 1) not in visited and grid[x][y + 1] == "1":
						queue.append((x, y + 1))

	return count

print(numOfIslands(grid))
