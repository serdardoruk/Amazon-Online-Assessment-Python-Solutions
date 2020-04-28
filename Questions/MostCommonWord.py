'''
Most Common Word
'''
'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not
case sensitive.  The answer is in lowercase.
'''
# Example:
#
# Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

from collections import Counter
def mostCommonWord(paragraph, banned):

	for c in "!?',;.":
		paragraph = paragraph.replace(c, " ")

	counter = Counter(word for word in paragraph.lower().split())
	banned_set = set(banned)
	for word, freq in counter.most_common():
		if word not in banned_set:
			return word
	return ''
print(mostCommonWord(paragraph,banned))
