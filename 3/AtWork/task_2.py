number = raw_input()
try:
    number = float(number)
    result = 'Yes'
except ValueError:
    result = 'No'

print result