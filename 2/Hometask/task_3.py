input = '1Madam im Adam1'
input = input.replace(' ', '').lower()
print (input)
len_input = len(input)
first = input[0:len(input)/2]
second = input[len(input)/2:][::-1] if len_input % 2 == 0 else input[len(input)/2+1:][::-1]
print first
print second
if first == second:
    print True
else:
    print False