# https://www.codewars.com/kata/only-readable-once-list

class SecureList(list):

    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def __getitem__(self, item):
        x = self.arr[item]
        del self.arr[item]
        return x

    def __str__(self):
        x = str(self.arr)
        del self.arr
        return x

    def __repr__(self):
        x = str(self.arr)
        del self.arr
        return x

    def __len__(self):
        return len(self.arr)


if __name__ == '__main__':
    base = [1, 2, 3, 4]
    a = SecureList(base)
    print(a[0])
    print(a[0])
    print(len(a))
