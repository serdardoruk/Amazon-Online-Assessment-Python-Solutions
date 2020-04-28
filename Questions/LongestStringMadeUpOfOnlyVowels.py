'''
Longest string made up of only vowels
'''
'''
You are given with a string . Your task is to remove atmost two substrings of any length from the given string
such that the remaining string contains vowels('a','e','i','o','u') only. Your aim is the maximise the length of
the remaining string. Output the length of remaining string after removal of atmost two substrings.
NOTE: The answer may be 0, i.e. removing the entire string.

Sample Input
2
earthproblem
letsgosomewhere
Sample Output
3
2
'''
"""
Test cases checked:
case # 1
input_string = "earthproblem"
number_of_substring_can_be_removed = 2
output = 3

case # 2
input_string = "letsgosomewhere"
number_of_substring_can_be_removed = 2
output = 2

case # 3
input_string = "aaabaa"
number_of_substring_can_be_removed = 2
output = 5

case # 4
input_string = "letsgosomewhere"
number_of_substring_can_be_removed = 3
output = 3
"""

def formLongestStringWithVowelAfterNRemoval(input_string, number_of_substring_can_be_removed):
	start, end = 0, len(input_string) - 1
	vowels = "aeiou"

	while (start < len(input_string)):
		if input_string[start] in vowels:
			start += 1
		else:
			break

	# Entire string is with vowels. So, return the entire string length
	if start == len(input_string):
		return start

	"""
	We don't need to check less then starting points. We've established in above that, start is the first consonant index.
	So, no need to further check in the same index.
	"""
	while (end > start):
		if input_string[end] in vowels:
			end -= 1
		else:
			break

	res = start + (len(input_string) - 1 - end)

	vowels_count_in_middle = []
	count = 0
	while (start < end):
		if input_string[start] in vowels:
			count += 1
		else:
			if count > 0:
				vowels_count_in_middle.append(count)
			count = 0
		start += 1

	"""
	We need to find the max (number_of_substring_can_be_removed - 1) items from the vowel count to list.
	Why number_of_substring_can_be_removed-1?
	Let's say, we are allowed to remove 2 substrings.
	It means we can actually take at most 1 consecutive vowel substring from the original string.
	If 3 removal is allowed, we can take 2 vowels substring from the middle.
	"""
	return res + sum(sorted(vowels_count_in_middle, reverse=True)[:(number_of_substring_can_be_removed - 1)])
