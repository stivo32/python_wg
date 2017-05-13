# coding: utf8
input = raw_input()
counts = dict()
counts['0'] = input.count('0')
counts['1'] = input.count('1')
counts['2'] = input.count('2')
max_count = max(counts.values())
numbers_with_max_count = list()
for key, value in counts.items():
    if value == max_count:
        numbers_with_max_count.append(key)
print ''.join(sorted(numbers_with_max_count))