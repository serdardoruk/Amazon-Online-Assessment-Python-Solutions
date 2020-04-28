'''
Spiral Matrix
'''
'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
'''

# Example:
# Input:
n = 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

def generateMatrix(n):
	
	if not n:
		return []
	
	matrix = [[0 for i in range(n)] for j in range(n)]

	num = 1
	
	left = 0
	right = n - 1

	top = 0
	down = n - 1

	while left <= right and top <= down:
		
		for i in range(left, right + 1):
			matrix[top][i] = num
			num += 1
		top += 1

		for i in range(top, down + 1):
			matrix[i][right] = num
			num += 1
		right -= 1

		for i in range(right, left - 1, -1):
			matrix[down][i] = num
			num += 1
		down -= 1

		for i in range(down, top - 1, -1):
			matrix[i][left] = num
			num += 1
		left += 1
	return matrix

print(generateMatrix(n))
