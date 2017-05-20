# coding: utf-8
import tasks
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        task = args[0]
    else:
        task = raw_input('What task to execute?\n')
    try:
        tasks.get_task(task)
    except KeyError:
        print 'Wrong task name'
