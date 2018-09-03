# CodeWars Sum of Pairs Solution <5 kyu>
# Given a list of integers and a single sum value, return the first two values in order of appearance that add up to form the sum.
# https://www.codewars.com/kata/sum-of-pairs/train/python


def sum_pairs(ints, s):
	seen_numbers = set()
	needed_nums = set()
	for num in ints:
		if num in needed_nums:
			return [s - num, num]
		else:
			needed_nums.add(s - num)



sum_pairs([2, 13, 12, 4, 3, 6, 7, 3, 1, 1], 10)

sum_pairs([10, 5, 2, 3, 7, 5], 10)

sum_pairs([1, 2, 3, 4, 1, 0], 2)
