# Solution for 'Directions Reduction' Kata [5 kyu], Codewars:
# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dirReduc(arr):
	pairs = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
	i = 0
	while i < (len(arr) - 1):
		if arr[i+1] == pairs[arr[i]]:
			arr.pop(i)
			arr.pop(i)
			i = 0
		else:
			i += 1
	return(arr)


dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
dirReduc(['EAST', 'WEST'])
