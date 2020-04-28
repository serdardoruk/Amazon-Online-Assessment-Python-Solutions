'''
Treasure Island
'''
'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and
dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure.
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from
the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island
is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks
or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other
areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get
to the treasure.
'''

# Example:
# Input:
sea =[['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'],['X', 'D', 'D', 'O']]
# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

from collections import deque
def sailToTreasure(matrix):
	q = deque([((0, 0 ), 0)])
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
# def dail(sea):
# 	if len(sea) == 0 or len(sea[0]) == 0:
# 		return -1
# 	r = len(sea)
# 	c = len(sea[0])
# 	queue = deque([((0,0), 0)])
# 	sea[0][0] = "D"
#
# 	while queue:
# 		(x, y), step = queue.popleft()
# 		for i, j in [[0,1],[0,-1],[1,0],[-1,0]]
# 			if 0 <= x + i < r and 0 <= y + j < c:
# 				if sea[x + i][y + j] == "X":
# 					return step + 1
# 				elif sea[x + i][y + j] == "0":
# 					sea[x + i][y + j] = "D"
# 					queue.append((x + i, y + j), step + 1)
# 	return -1
