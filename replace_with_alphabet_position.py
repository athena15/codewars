# https://www.codewars.com/kata/replace-with-alphabet-position/train/python

def alphabet_position(text):
    # Dictionary comprehension, yeah!!
    d = {v: i + 1 for i, v in enumerate('abcdefghijklmnopqrstuvwxyz')}
    return ' '.join([str(d[i.lower()]) for i in text if i.isalpha()])


alphabet_position("The sunset sets at twelve o' clock.")

