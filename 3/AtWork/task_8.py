input = raw_input()
final_str = ''
for symbol in input:
    if not symbol.isdigit():
        final_str += symbol
print final_str
