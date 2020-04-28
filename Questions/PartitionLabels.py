'''
Partition Labels
'''
'''
A string S of lowercase letters is given. We want to partition this string into as many parts as
possible so that each letter appears in at most one part, and return a list of integers representing
the size of these parts.
'''
# Example 1:
# Input:
S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

def partitionLabels(S):
	indices = {}
	last = 0
	ans = []
	maxLen = 0
	for letter, idx  in enumerate(S):
		indices[idx] = letter
	for i, idx in enumerate(S):
		maxLen = max(maxLen, indices[idx])
		if maxLen == i:
			ans.append(i - last + 1)
			last = i + 1
	return ans

print(partitionLabels(S))
