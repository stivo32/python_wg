# coding: utf-8

user_input = raw_input()

if len(user_input) < 2:
    print user_input
    exit()

for i in range(1,len(user_input)):
    print user_input[0:i]+' '+user_input[i:]
