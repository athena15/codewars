# https://www.codewars.com/kata/split-and-then-add-both-sides-of-an-array-together/train/python

def split_and_add(numbers, n):
    if n == 0 or len(numbers) == 1:
        print(numbers)
        return numbers

    length = len(numbers) // 2
    top = numbers[length - 1::-1]
    bottom = numbers[:length - 1:-1]

    new_numbers = [sum(i) for i in zip(bottom, top)]
    if len(numbers) % 2 == 1:
        new_numbers.append(bottom[-1])

    return split_and_add(new_numbers[::-1], n - 1)


split_and_add([1, 2, 3, 4, 5], 2)
