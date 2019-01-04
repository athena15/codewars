from collections import Counter

import regex as re


def top_3_words(text):
    match = r"""[\'\"]*[A-Za-z]*[\'\"]*[A-Za-z]+"""
    matches = [i.lower() for i in re.findall(match, text) if i != '']
    c = Counter(matches)
    return [i for i, v in c.most_common(3) if len(i) > 0]


top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")
