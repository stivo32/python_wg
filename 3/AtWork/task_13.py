numbers = (1, 1, 2, 2, 5, 5, 6, 6, 1, 2)

for i in range(0, len(numbers), 2):
    if numbers[i] != numbers[i+1]:
        print 'No'
        exit()

print 'Yes'


