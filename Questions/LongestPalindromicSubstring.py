'''
Longest Palindromic Substring
'''
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
# Example 1:
# Input:
s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
# Input: "cbbd"
# Output: "bb"

def longestPalindrome(s):
	if len(s) < 2 or s == s[::-1]:
		return s
	n = len(s)
	start = 0
	maxLen = 1
	for i in range(n):
		odd = s[i - maxLen - 1 : i + 1]
		even = s[i - maxLen : i + 1]
		if i - maxLen - 1 > 0 and  odd == odd[::-1]:
			start = i - maxLen - 1
			maxLen += 2
			continue
		if i - maxLen >= 0 and even == even[::-1]:
			start = i - maxLen
			maxLen += 1
	return s[start : start + maxLen]

print(longestPalindrome(s))
