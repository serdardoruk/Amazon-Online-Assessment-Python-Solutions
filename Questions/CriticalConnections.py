'''
Critical Connections
'''
'''
Given an underected connected graph with n nodes labeled 1..n. A bridge (cut edge) is defined as an edge which,
when removed, makes the graph disconnected (or more precisely, increases the number of connected components
in the graph). Equivalently, an edge is a bridge if and only if it is not contained in any cycle. The task is to
find all bridges in the given graph. Output an empty list if there are no bridges.

Input:

n, an int representing the total number of nodes.
edges, a list of pairs of integers representing the nodes connected by an edge.
'''
# Example 1:
# Input:
# n = 5
# edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
# Output: [[1, 2], [4, 5]]
# Explanation:
# There are 2 bridges:
# 1. Between node 1 and 2
# 2. Between node 4 and 5
# If we remove these edges, then the graph will be disconnected.
# If we remove any of the remaining edges, the graph will remain connected.
#
# Example 2:
# Input:
# n = 6
# edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
# Output: []
# Explanation:
# We can remove any edge, the graph will remain connected.
#
# Example 3:
# Input:
n = 9
edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
# Output: [[3, 4], [3, 6], [4, 5]]

import collections
def criticalConnections(n, connections):
	dic = collections.defaultdict(set)
	for u, v in connections:
		dic[u].add(v)
		dic[v].add(u)
	steps = [-1 for i in range(n + 1)]
	res = []
	helper(1, -1, 0, steps, dic, res)
	return res

def helper(cur, par, level, steps, dic, res):
	steps[cur] = level
	for child in dic[cur]:
		if child == par:
			continue
		if steps[child] == -1:
			min_step = helper(child, cur, level + 1, steps, dic, res)
			steps[cur] = min(steps[cur], min_step)
		else:
			steps[cur] = min(steps[child], steps[cur])
	if steps[cur] == level and cur != 0 and par != -1:
		res.append([cur, par])
	return steps[cur]

# n = 4
# edges = [[0,1],[1,2],[2,0],[1,3]]
print(criticalConnections(n, edges))
