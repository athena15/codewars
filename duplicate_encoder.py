# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    c = Counter(word)
    new_str = ''

    for letter in word:
        if c[letter] > 1:
            new_str += ')'
        else:
            new_str += '('

    return new_str


duplicate_encode('success')
