from collections import Counter
from collections import defaultdict


def valid(a):
    group_sizes = 0
    d = defaultdict(str)
    n = 0
    all_golfers = []

    for i, v in enumerate(a):
        all_golfers.append(''.join([i for i in v]))

        if n == 0:
            group_sizes = len(v)
            n += 1
        else:
            if len(v) != group_sizes:
                return False

        for group in v:
            for golfer in group:
                d[golfer] += ''.join([i for i in group if i != golfer])

        golfers = ''.join(v)
        c = Counter(golfers)
        if len(set(c.values())) > 1:
            return False

        for combo in d.values():
            if len(combo) != len(set(combo)):
                return False

    if not all(set(x) == set(all_golfers[0]) for x in all_golfers):
        return False

    return True


valid([
    ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
    ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
    ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
    ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
    ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']
]
)
