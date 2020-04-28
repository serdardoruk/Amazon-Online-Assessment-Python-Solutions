'''
Point of Lattice
'''
'''
https://leetcode.com/discuss/interview-question/396418/
'''
ax = -1
ay = 3
bx = 3
by = 1

import math
def lattice(ax,ay, bx, by):
	dx = bx - ax
	dy = by - ay
	#rotate

	rx = dy
	ry = -dx

	gcd = abs(math.gcd(rx, ry))
	rx /= gcd
	ry /= gcd

	return "{},{}".format(int(bx + rx), int(by + ry))

print(lattice(ax, ay, bx, by))
