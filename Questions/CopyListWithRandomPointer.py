'''
Copy List with Random Pointer
'''
'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val

random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
'''
# Example 1:
# Input:
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]


# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
# Example 2:
# Input:
# head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
# Example 3:
# Input:
# head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
# Example 4:
# Input:
# head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.

class Node:
	def __init__(self, val, next, random):
		self.val = val
		self.next = next
		self.random = random

def createLinkedList(head):
	h = Node("dummy", None, None)
	hh = h
	for i in range(len(head) - 1):
		h.next = Node(head[i + 1][0], None, None)
		h.random = head[i][1]
		h = h.next
	return hh.next

# print(createLinkedList(head))

def copyRandomList(head):
	if not head:
		return None
	head = createLinkedList(head)
	nodes = {}
	copy = head

	while copy:
		nodes[copy] = Node(copy.val, None, None)
		copy = copy.next

	copy = head

	while copy:
		if copy.next:
			nodes[copy].next = nodes[copy.next]
		else:
			nodes[copy].next = None

		if copy.random:
			nodes[copy].random = nodes[copy.random]
		else:
			nodes[copy].random = None
		copy = copy.next
	return nodes[head]

print(copyRandomList(head))
