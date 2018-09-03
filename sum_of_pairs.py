# CodeWars Sum of Pairs Solution <5 kyu>
# Given a list of integers and a single sum value, return the first two values in order of appearance that add up to form the sum.
# https://www.codewars.com/kata/sum-of-pairs/train/python

from itertools import combinations


def sum_pairs(ints, s):
	x = list(combinations(ints, 2))
	y = [i for i in x if i[0] + i[1] == s]
	if len(y) == 0:
		return None

	lowest = 9999
	answer = []
	for match in y:
		if match[0] == match[1]:
			match_two = [i for i, n in enumerate(ints) if n == match[0]][1]

			if match_two < lowest:
				lowest = match_two
				answer = list(match)


		else:
			match_two = [i for i, n in enumerate(ints) if n == match[1]][0]

			if match_two < lowest:
				lowest = match_two
				answer = list(match)

	return answer


sum_pairs([2, 13, 12, 4, 3, 6, 7, 3, 1, 1], 10)

sum_pairs([10, 5, 2, 3, 7, 5], 10)

sum_pairs([1, 2, 3, 4, 1, 0], 2)
