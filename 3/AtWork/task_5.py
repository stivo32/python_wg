result = True

try:
    1 / 0
except ZeroDivisionError:
    result = False
finally:
    print 'Ok' if result else 'Exception'