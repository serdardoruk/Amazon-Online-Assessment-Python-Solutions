'''
Favorite Genres
'''
'''
Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user
has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within
that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the
user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre
if he/she has listened to the same number of songs per each of the genres.

'''
# Example 1:
# Input:
userSongs = {  "David": ["song1", "song2", "song3", "song4", "song8"],"Emma":  ["song5", "song6", "song7"]}
songGenres = {  "Rock":    ["song1", "song3"],"Dubstep": ["song7"],"Techno":  ["song2", "song4"],"Pop":     ["song5", "song6"],"Jazz":    ["song8", "song9"]}
# Output: {  "David": ["Rock", "Techno"],"Emma":  ["Pop"]}
# Explanation:
# David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
# Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
#
# Example 2:
# Input:
# userSongs = {  "David": ["song1", "song2"],"Emma":  ["song3", "song4"]}
# songGenres = {}
# Output: {  "David": [],"Emma":  []}

import collections


def favGenres(userSongs, songGenres):
	output = {}
	for song in userSongs:
		songs = userSongs[song]
		count = collections.defaultdict(int)
		for track in songs:
			for genre, songg in songGenres.items():
				if track in songg:
					count[genre] += 1
		output[song] = [key for key, val in count.items() if val == max(count.values())]

	return output

print(favGenres(userSongs, songGenres))
