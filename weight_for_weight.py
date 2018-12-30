# https://www.codewars.com/kata/weight-for-weight/train/python

class Solution:
    def order_weight(self, strng):

        t = [int(i) for i in strng.split()]

        print(t)

        indices = []

        for i in t:
            ix = 0
            if len(str(i)) == 1:
                indices.append(int(i))
            else:
                for num in str(i):
                    ix += int(num)
                indices.append(ix)

        print(indices)

        return (' ').join([str(x) for _, x in sorted(zip(indices, t))])


solution = Solution()
# solution.order_weight('5 6 12 66')
