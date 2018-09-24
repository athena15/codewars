"""
CodeWars: Your Order, Please - Solution [6 kyu]
Your task is to sort a given string. Each word in the String will contain a single number.
This number is the position the word should have in the result.
"""


def order(sentence):
	if len(sentence) == 0:
		return ''
	else:
		sentence = sentence.split(' ')
		solution = [''] * len(sentence)
		for word in sentence:
			for letter in word:
				if letter.isdigit():
					solution[int(letter) - 1] = str(word)
					break
				else:
					pass
		solution = ' '.join(solution)
	return solution


def test_1():
	assert order('is2 Thi1s T4est 3a') == 'Thi1s is2 3a T4est'


def test_2():
	assert order('1 3 2 6 4 5 8 7 9') == '1 2 3 4 5 6 7 8 9'
