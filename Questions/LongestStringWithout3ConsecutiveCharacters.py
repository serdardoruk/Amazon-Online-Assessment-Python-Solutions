'''
Longest string without 3 consecutive characters
'''
'''
Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same.
There can be at max A 'a', B 'b' and C 'c'.
'''
# Example 1:
# Input:
A = 1
B = 1
C = 6
# Output: "ccbccacc"

# Example 2:
# Input:
A = 1
B = 2
C = 3
# Output: "acbcbc"
import heapq
def ls3(A, B, C):
    pq = []
    res = ""
    for letter, amount in ('a', A), ('b', B), ("c", C):
        heapq.heappush(pq, (-amount, letter))
    preamount, preletter = 0, ""
    amount, letter = heapq.heappop(pq)
    while pq:
        amount, letter = heapq.heappop(pq)
        if preamount:
            heapq.heappush(pq, (preamount, preletter))
            preamount, preletter = 0, ''
        if res[-2:] == letter * 2:
            preamount, preletter = amount, letter
        else:
            res += letter
            if amount != -1:
                heapq.heappush(pq, (amount + 1, letter))
    return res

A, B, C = 1, 1, 6
print(ls3(A, B, C))
# A, B, C = 1, 2, 3
# print(ls3(A, B, C))
