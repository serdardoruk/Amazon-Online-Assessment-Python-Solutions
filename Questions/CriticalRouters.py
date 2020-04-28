"""
Critical Routers
"""
"""
You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges,
makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.

Output:
Return a list of integers representing the critical nodes.

Example:

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

Output: [2, 3, 5]
"""

def criticalConnections(n, connections):
	graph = [[] for _ in range(n)]
	currentRank = 0
	lowestRank = [0 for i in range(n)]
	visited = [False for _ in range(n)]
	for connection in connections:
		graph[connection[0]].append(connection[1])
		graph[connection[1]].append(connection[0])
	res = []
	prevVertex = -1
	currentVertex = 0
	_dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
	return sorted(res)

def _dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):
	visited[currentVertex] = True
	lowestRank[currentVertex] = currentRank
	for nextVertex in graph[currentVertex]:
		if nextVertex == prevVertex:
			continue

		if not visited[nextVertex]:
			_dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)

		lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
		if lowestRank[nextVertex] >= currentRank + 1:
			res.append(currentVertex)

connections = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
n = 7

print(criticalConnections(n, connections))
