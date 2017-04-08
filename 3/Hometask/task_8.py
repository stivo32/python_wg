# coding: utf-8

user_input = raw_input()

flag = False
equal_marks_before = 0
equal_marks_after = 0
letters = False
indexes = list()
# if not user_input.count('===') < 2:
#     print 'No'
#     exit()
# for symbol in user_input:
#     if symbol == '=' and not letters:
#         equal_marks_before += 1
#     elif symbol.isalpha() and equal_marks_before >= 3:
#         letters += 1
#     elif symbol == '=' and letters:
#         equal_marks_after += 1
#     else:
#         equal_marks_before = 0
#         equal_marks_after = 0
#         letters = 0
# if equal_marks_before >= 3 and equal_marks_after >= 3 and letters:
#     print 'Yes'
# else:
#     print 'No'
#
j = 0
for i, _ in enumerate(user_input):
    index = user_input.find('===', j)
    if index == -1:
        break
    indexes.append(index)
    j = index + 3
print indexes
for i in range(len(indexes)-1):
    if user_input[indexes[i]+3: indexes[i+1]].isalpha():
        print 'Yes'
        exit()
print 'No'
