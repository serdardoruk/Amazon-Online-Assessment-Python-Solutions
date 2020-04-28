"""Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of
most to least frequently mentioned.

The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews,
sort alphabetically."""


# ----------------ex 1
k1 = 2
keywords1 = ["anacell", "cetracular", "betacellular"]
reviews1 = [  "Anacell provides the best services in the city","betacellular has awesome services","Best services provided by anacell, everyone should use anacell",]

# Output:
# ["anacell", "betacellular"]
#
# Explanation:
# "anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
#
# ----------------ex 2
# Input:
k2 = 2
keywords2 = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews2 = ["I love anacell Best services; Best services provided by anacell","betacellular has great services","deltacellular provides much better services than betacellular","cetracular is worse than anacell","Betacellular is better than deltacellular.",]
#
# Output:
# ["betacellular", "anacell"]
#
# Explanation:
# "betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews,
#  but "anacell" is lexicographically smaller.


import  collections, re, heapq
def topKFrequentMentionedKeywords(keywords, reviews, k):
	data_value_dict = collections.Counter()
	key_value_dict = set(keywords)
	res = []

	for review in reviews:
		temp_list = review.lower().split(" ")

		for value in temp_list:
			value = re.sub('[^a-z]', '', value)

			if value in key_value_dict:
				data_value_dict[value] += 1
	res = heapq.nlargest(k, data_value_dict, key = lambda x: (data_value_dict[x], x))

	return res

print(topKFrequentMentionedKeywords(keywords1, reviews1, k1))
print(topKFrequentMentionedKeywords(keywords2, reviews2, k2))

