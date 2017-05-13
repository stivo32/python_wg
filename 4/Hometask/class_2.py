# coding: utf-8

# names = raw_input('Enter names').split(';')

names = ['Ann', 'Baddy', 'Robert', 'Ashley']

vowels = 'AEUOIY'

dict_with_result = {'start_with_vowel': [0, 0, 0], 'start_with_consonant': [0, 0, 0]}

for name in names:
    if name[0] in vowels:
        dict_with_result['start_with_vowel'][0] += 1
        if len(name) % 2 == 0:
            dict_with_result['start_with_vowel'][1] += 1
        else:
            dict_with_result['start_with_vowel'][2] += 1
    else:
        dict_with_result['start_with_consonant'][0] += 1
        if len(name) % 2 == 0:
            dict_with_result['start_with_consonant'][1] += 1
        else:
            dict_with_result['start_with_consonant'][2] += 1

print 'Vowel: {}, even: {}, odd: {}'.format(dict_with_result['start_with_vowel'][0],
                                            dict_with_result['start_with_vowel'][1],
                                            dict_with_result['start_with_vowel'][2])
print 'Consonant: {}, even: {}, odd: {}'.format(dict_with_result['start_with_consonant'][0],
                                                dict_with_result['start_with_consonant'][1],
                                                dict_with_result['start_with_consonant'][2])
