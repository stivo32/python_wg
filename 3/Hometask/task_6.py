# coding: utf-8

user_input = raw_input()

max_spaces = 0
local_max_space = 0

for i in range(0, len(user_input)):
    if user_input[i] == ' ':
        local_max_space += 1
    else:
        local_max_space = 0
    if max_spaces < local_max_space:
        max_spaces = local_max_space
print max_spaces if max_spaces != 0 else 'No spaces'

