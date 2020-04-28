'''
Generate Parentheses
'''
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]'''

n = 3

def generateParanthesis(N):
	ans = []
	def backtrack(S='', left=0, right=0):
		if len(S) == 2 * N:
			ans.append(S)
			return
		if left < N:
			backtrack(S + '(', left + 1, right)
		if right < left:
			backtrack(S + ')', left, right + 1)

	backtrack()
	return ans

print(generateParanthesis(n))
