# coding: utf-8

user_input = raw_input('>').split()

# numbers = [int(i) for i in user_input if int(i) >= 0]
# print ' '.join([i for i in raw_input().split() if int(i) >= 0])
numbers = []

for number in user_input:
    number = int(number)
    numbers.append(number)


for number in numbers[:]:
    if number < 0:
        numbers.remove(number)

print numbers