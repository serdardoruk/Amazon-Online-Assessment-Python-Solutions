'''
Battleship
'''
'''
https://leetcode.com/discuss/interview-question/538068/
'''
N = 12
s = "1A 2A,12A 12A"
t = "12A"
# return "1,0"

def battleship(N, s, t):
	matrix = [[0] * N for _ in range(N)]

	ships = s.split(",")
	hits = t.split(" ")
	for i in range(len(ships)):
		ships[i] = ships[i].split(" ")

	original = set()
	for i in range(len(ships)):
		top_left = ships[i][0]
		bottom_right = ships[i][1]
		top_x = int(top_left[:-1]) - 1
		top_y = ord(top_left[-1]) - 65
		bottom_x = int(bottom_right[:-1]) - 1
		bottom_y = ord(bottom_right[-1]) - 65
		vertical = bottom_x - top_x + 1
		horizonal = bottom_y - top_y + 1
		for m in range(top_x, top_x + vertical):
			for n in range(top_y, top_y + horizonal):
				matrix[m][n] = i + 1
		original.add(i + 1)

	hitted = set()
	for hit in hits:
		x = int(hit[:-1]) - 1
		y = ord(hit[-1]) - 65
		if matrix[x][y] != 0:
			hitted.add(matrix[x][y])
			matrix[x][y] = 0

	updated = set()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] != 0:
				updated.add(matrix[i][j])

	sunk = len(original - updated)
	hitted_but_not_sunk = len(hitted & updated)

	return '{},{}'.format(sunk,hitted_but_not_sunk)

print(battleship(N,s,t))
