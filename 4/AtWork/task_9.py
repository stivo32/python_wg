
number = int(raw_input())
passports = dict()
for i in xrange(number):
    line = raw_input().split(': ')
    passports[line[0]] = line[1].strip()

for number in sorted(passports):
    print number, passports[number]

del passports['MORE-003']

passports['AGILE-017'] = 'Mr. Smart'

num_to_delete = ''
for number, name in passports.items():
    if name == 'Mr. Switch':
        del passports[number]
        break
#del passports[num_to_delete]
passports['SECRET-007'] = 'Mr. Smith'

for number, name in passports.items():
    if name == 'Mr. X':
        del passports[number]
        break
#del passports[num_to_delete]
print '6'
for number, name in passports.items():
    print number, name

