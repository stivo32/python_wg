print {x: x * 2 for x in xrange(1, 11)}
print {x: x ** 3 for x in xrange(1, 11)}
import pprint
pprint.pprint({letter: [a + b
                        for a in [letter, letter.upper()]
                        for b in [letter, letter.upper()]]
                for letter in 'abcdef'})
