'''
Search a 2D Matrix II
'''
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''
def searchMatrix(matrix, target):
	if not matrix:
		return False

	def search_rec(left, up, right, down):
		# this submatrix has no height or no width.
		if left > right or up > down:
			return False
		# `target` is already larger than the largest element or smaller
		# than the smallest element in this submatrix.
		elif target < matrix[up][left] or target > matrix[down][right]:
			return False

		mid = left + (right - left) // 2

		# Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
		row = up
		while row <= down and matrix[row][mid] <= target:
			if matrix[row][mid] == target:
				return True
			row += 1

		return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

	return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

print(searchMatrix(matrix,target))


# NOT EFFICIENT
# def searcgMatrix(matrix, target):
#
# 	if len(matrix) == 0:
# 		return False
#
# 	row = len(matrix) - 1
# 	col = 0
#
# 	while row >= 0 and col < len(matrix[0]):
# 		if matrix[row][col] == target:
# 			return True
#
# 		elif matrix[r][c] > target:
# 			row -= 1
#
# 		else:
# 			col += 1
#
# 	return False
