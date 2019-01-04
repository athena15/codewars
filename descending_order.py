# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def Descending_Order(num):
    return int(''.join(sorted(str(num), reverse=True)))


Descending_Order(7342)  # returns 7432
