import string
print {(letter, letter.upper()) for letter in string.ascii_lowercase}

print {
	number % 9 for number in xrange(1, 101) if number % 3 == 0
}

