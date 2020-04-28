'''
https://leetcode.com/problems/search-suggestions-system/  1268. Search Suggestions System
Product Suggestions
'''
'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.

'''

# Example 1:
#
# Input:
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
#
#
# Example 2:
#
# Input:
# products = ["havana"]
# searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
#
#
# Example 3:
#
# Input:
# products = ["bags","baggage","banner","box","cloths"]
# searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
#
#
# Example 4:
#
# Input:
# products = ["havana"]
# searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]


import bisect
def suggestedProducts(products, searchWord):
	# prods = sorted(products)
	# current_location = bisect.bisect_left(prods, searchWord[0])
	# return current_location
	if not searchWord:
		return []

	prods = sorted(products)

	current_location = bisect.bisect_left(prods, searchWord[0])
	results = []

	for idx in range(len(searchWord)):
		current_search = searchWord[:idx + 1]

		while current_location < len(products):
			p = prods[current_location][:idx + 1]
			if p == current_search:
				break

			if p > current_search:
				current_location = len(prods)
			current_location += 1

		temp_results = []
		for d in range(3):
			if len(prods) <= current_location + d:
				break
			p = prods[current_location + d]
			if p[:idx + 1] == current_search:
				temp_results.append(p)
			else:
				break

		results.append(temp_results)
	return results

print(suggestedProducts(products, searchWord))
