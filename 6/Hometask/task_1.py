# coding: utf-8

finish_dict = {
    line.split('-')[0]: line.split('-')[1]
    for line in raw_input().split(';')
}
print finish_dict
