# https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python

def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) > 4 else i for i in sentence.split(' ')])


spin_words('Hey fellow warriors')
spin_words('   hello    all  out there   ')
