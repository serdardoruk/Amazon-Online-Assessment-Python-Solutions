'''
Count substrings with exactly K distinct chars
'''
'''
Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k
 distinct characters. If the given string doesn't have k distinct characters, return 0.
'''
# Example 1:
# Input:
s = "pqpqs"
k = 2
# Output: 7
# Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
#
# Example 2:
# Input:
# s = "aabab"
# k = 3
# Output: 0

import collections
def subStringsWithKDistinctCharacters(s, k):
	s = list(s)
	def atMost(k):
		count = collections.defaultdict(int)
		left = 0
		ans = 0
		for right, x in enumerate(s):
			count[x] += 1
			print(count, len(count))
			while len(count) > k:
				count[s[left]] -= 1
				if count[s[left]] == 0:
					del count[s[left]]
				left += 1
			ans += right - left + 1
			print(ans)
		return ans
	return atMost(k) - atMost(k - 1)

print(subStringsWithKDistinctCharacters(s,k))
