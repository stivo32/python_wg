import string
import sys

alphabet = string.ascii_lowercase
text = raw_input()
offset = 1
mapping = {}

for ch in text:
    translated = alphabet[(alphabet.index(ch) + offset) % len(alphabet)]
    mapping[ch] = translated
    mapping[ch.upper()] = translated.upper()

for i in range(10):
    mapping[str(i)] = str((i+1) % 10)
for i in mapping:
    print i, mapping[i]

exit()

coded_text = []
for ch in text:
    ch = ch.lower()
    if ch.isalpha():
        ch = alphabet[alphabet.index(ch) + offset]
    coded_text.append(ch)

print ''.join(coded_text)