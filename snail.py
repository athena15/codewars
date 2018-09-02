# Codewars Snail Solution <4 kyu>
# https://www.codewars.com/kata/snail


def snail(array):
	path = []

	# RIGHT
	while len(array) > 0:
		side = len(array[0])
		for i in range(side):
			path.append(array[0][i])
		array.pop(0)

		if len(array) == 0:
			break

		# DOWN
		for i in range(side - 1):
			path.append(array[i][-1])
			array[i].pop(-1)

		# LEFT
		for i in array[-1][::-1]:
			path.append(i)
		array.remove(array[-1])

		if len(array) == 0:
			break

		# UP
		for i in range(len(array) - 1, -1, -1):
			path.append(array[i][0])
			array[i].pop(0)

	return path


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
c = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25, ]]

snail(a)
snail(b)
snail(c)
