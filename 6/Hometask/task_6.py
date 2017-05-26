# coding: utf-8
import os
file_name = raw_input()
number_of_files = int(raw_input())

size = os.path.getsize(file_name)
part = size / number_of_files + 1
with open(file_name) as f:
    [
        open('{}.{}'.format(file_name, i), 'w').write(f.read(part))
        for i in range(number_of_files)
    ]
