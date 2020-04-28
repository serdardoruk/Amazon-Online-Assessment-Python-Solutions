'''
Merge Intervals
'''
'''
Given a collection of intervals, merge all overlapping intervals.
'''

# Example 1:
# Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
# Input:
# intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
	if not intervals:
		return []
	intervals = sorted(intervals, key=lambda x: x[0])
	ans = [intervals[0]]
	for i in range(1, len(intervals)):
		if ans[-1][1] < intervals[i][0]:
			ans.append(intervals[i])
		elif ans[-1][1] < intervals[i][1]:
			ans[-1][1] = intervals[i][1]
	return ans

print(merge(intervals))
