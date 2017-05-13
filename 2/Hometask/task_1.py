input = raw_input()
list = input.split()
a = int(list[0])
b = int(list[1])
result = True if (a * b) % 2 == 0 else False
print result
