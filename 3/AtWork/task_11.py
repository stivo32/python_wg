input = 'abca'
input = input.replace(' ', '').lower()
pal = True
for i in range(len(input) / 2):
    if input[i] != input[-1-i]:
        pal = False
        break
print pal
