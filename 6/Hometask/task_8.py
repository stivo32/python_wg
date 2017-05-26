# coding: utf-8

dataset = 'X:CS:5 X:CS:3 Y:CS:5 Y:Math:4'.split()
dataset = [
    x.split(':')
    for x in dataset
]
print dataset
students = {
    student.setdefault(subject, [])
    for student, subject, mark in data
}

print students
students = {
    students[student].update([subject, []])
    for student, subject, mark in data
}

print students
print '1'
for row in data:
    students[row[0]][row[1]] = []

for row in data:
    students[row[0]][row[1]].append(row[2])

print students