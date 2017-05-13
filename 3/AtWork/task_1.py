number = raw_input()
# count_of_point = 0
# answer = 'No'
# parts = input.split('.')
# flag = 0
# if len(parts) == 2:
#     if parts[1].isdigit():
#         flag += 1
#         print parts[1]
#     print parts[0]
#     if '+' == parts[0][0]:
#         parts[0] = parts[0].replace('+', '')
#         print parts[0]
#     elif '-' == parts[0][0]:
#         parts[0] = parts[0].replace('-', '')
#         print parts[0]
#     if parts[0].isdigit():
#         flag += 1
# print 'Yes' if flag == 2 else 'No'

# <float>e[-+]<float>

number = number.split('e', 1)
if len(number) == 1:

    if number.count('.') != 1:
        print 'No'
        exit()

    if number.startswith('+') or number.startswith('-'):
        number = number[1:]
    part1 , part2 = number.split('.')
    print 'YES' if (part1+part2).isdigit() else 'No'

else:
    number1, number2 = number
    ...