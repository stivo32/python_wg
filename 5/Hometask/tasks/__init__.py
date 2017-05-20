# coding: utf-8
import task1
import task2
import task3
import task4

TASKS = {
    'lucky_generator': task1.main,
    'list_shifter': task2.main,
    'rectangle_square': task3.main,
    'recursive_print': task4.main
}


def get_task(task_name):
    return TASKS[task_name]

__all__ = ('get_task',)
