# coding: utf-8
import tasks
import sys


if __name__ == '__main__':
    user_input = raw_input('What task to execute?\n')
    try:
        tasks.get_task(user_input)
    except KeyError:
        print 'Wrong task name'
