'''
Merge Two Sorted Lists
'''
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Example:
# Input: 1->2->4, 1->3->4
list1 = [1,2,4]
list2 = [1,3,4]

def createLinkedList(lst):
	head = ListNode("dummy")
	h = head
	for item in lst:
		head.next = ListNode(item)
		head = head.next
	return h.next
# Output: 1->1->2->3->4->4

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def mergeTwoLists(l1, l2):
	l1 = createLinkedList(l1)
	l2 = createLinkedList(l2)
	res = ListNode(-1)
	pre = res
	while l1 and l2:
		if l1.val <= l2.val:
			pre.next = l1
			l1 = l1.next
		else:
			pre.next = l2
			l2 = l2.next
		pre = pre.next
	if l1:
		pre.next = l1
	if l2:
		pre.next = l2
	return res.next

lst = mergeTwoLists(list1,list2)
while lst:
	print(lst.val)
	lst = lst.next
