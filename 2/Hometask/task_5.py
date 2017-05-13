# coding: utf8
while True:
    first = raw_input()
    first_age_list = first.split()
    if len(first_age_list) != 2:
        print 'Неверное количество аргументов'
        continue
    first_year = first_age_list[0]
    first_month = first_age_list[1]
    if not first_year.isdigit() or not first_year.isdigit():
        print 'Неверный формат ввода'
        continue
    if 2017 < int(first_year) or int(first_year) < 1900:
        print 'Вы ввели неверный год'
        continue
    if 12 < int(first_month) or int(first_month) < 1:
        print 'Месяц должен быть от 1 до 12'
        continue
    break
while True:
    second = raw_input()
    second_age_list = second.split()
    if len(second_age_list) != 2:
        print 'Неверное количество аргументов'
        continue
    second_year = second_age_list[0]
    second_month = second_age_list[1]
    if not second_year.isdigit() or not second_year.isdigit():
        print 'Неверный формат ввода'
        continue
    if 2017 < int(second_year) or int(second_year) < 1900:
        print 'Вы ввели неверный год'
        continue
    if 12 < int(second_month) or int(second_month) < 1:
        print 'Месяц должен быть от 1 до 12'
        continue
    break
sum_of_months_between_ages = (int(first_year)-int(second_year))*12 + (int(first_month)-int(second_month))
if sum_of_months_between_ages < 0:
    older = 'I'
elif sum_of_months_between_ages > 0:
    older = 'II'
else:
    older = 'SAME'
year_dif = abs(sum_of_months_between_ages) / 12
month_dif = abs(sum_of_months_between_ages) % 12
result_list = list()
result_list.append(older)

if year_dif > 0:
    years_ending = '' if (year_dif == 1) else 's'
    result_list.append(' '.join([str(year_dif), 'year{}'.format(years_ending)]))
if month_dif > 0:
    months_ending = '' if month_dif == 1 else 's'
    result_list.append(' '.join([str(month_dif), 'month{}'.format(months_ending)]))


result_string = ', '.join(result_list)
print result_string


