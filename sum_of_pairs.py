from itertools import combinations


def sum_pairs(ints, s):
	x = list(combinations(ints, 2))
	y = [i for i in x if i[0] + i[1] == s]
	if len(y) == 0:
		return None

	lowest = 9999
	answer = []
	print(y)
	for match in y:
		if match[0] == match[1]:
			match_one = [i for i, n in enumerate(ints) if n == match[0]][0]
			match_two = [i for i, n in enumerate(ints) if n == match[0]][1]
			print(f'Matches are: {match_one}, {match_two}')
			if match_two < lowest:
				print(f'match_2 = {match_two}, is less than lowest = {lowest}')
				lowest = match_two
				answer = list(match)
				print(f'Answer is now {answer}')

		else:
			match_one = [i for i, n in enumerate(ints) if n == match[0]][0]
			match_two = [i for i, n in enumerate(ints) if n == match[1]][0]
			print(f'Matches are: {match_one}, {match_two}')
			if match_two < lowest:
				print(f'match_2 = {match_two}, is less than lowest = {lowest}')
				lowest = match_two
				answer = list(match)
				print(f'Answer is now {answer}')

	print(answer)


# sum_pairs([2, 13, 12, 4, 3, 6, 7, 3, 1, 1], 10)

# sum_pairs([10, 5, 2, 3, 7, 5], 10)

sum_pairs([1, 2, 3, 4, 1, 0], 2)
