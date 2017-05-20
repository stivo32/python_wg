import string
print ['x' * x for x in xrange(5, 0, -1)]
alphabet = string.ascii_letters
print [alphabet[:x] for x, _ in enumerate(alphabet, start=1)]
print [x * (-1) ** (x + 1) for x in xrange(1, 101)]
print [x if x % 2 != 0 else -x for x in range(1, 101)]
