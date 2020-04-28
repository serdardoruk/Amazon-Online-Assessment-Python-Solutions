'''
Treasure Island 2a
'''
'''
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a
shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the
starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island
is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any
of the treasure islands.
'''
# Example:
# Input:
sea = [['S', 'O', 'O', 'S', 'S'], ['D', 'O', 'D', 'O', 'D'], ['O', 'O', 'O', 'O', 'X'], ['X', 'D', 'D', 'O', 'O'], ['X', 'D', 'D', 'D', 'O']]
# Output: 3
# Explanation:
# You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0).
# Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

from collections import deque
def sailToTreasure(matrix):
	if len(sea) == 0 or len(sea[0]) == 0:
		return -1
	q = deque([((0, 0 ), 0)])
	for i in range(len(sea)):
		for j in range(len(sea[0])):
			if sea[i][j] == "S":
				q.append(((i, j), 0))
	matrix[0][0] = "D"
	while q:
		(x, y), step = q.popleft()
		for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
			i = x + dx
			j = y + dy
			if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
				if matrix[i][j] == "X":
					return step + 1
				elif matrix[i][j] == "O":
					matrix[i][j] = "D"
					q.append(((i, j), step + 1))
	return -1

print(sailToTreasure(sea))
