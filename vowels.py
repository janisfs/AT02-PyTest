# vowels.py

# Функция для подсчета гласных букв в строке
def count_vowels(s):
    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in s if char in vowels)



#  Вариант подсчета гласных через цикл for
#    count = 0
#    for char in s:
#        if char in vowels:
#            count += 1
#    return count


# Использование функции filter:
# return len(list(filter(lambda char: char in vowels, s)))


# Использование функции reduce:
# from functools import reduce
# return reduce(lambda count, char: count + (1 if char in vowels else 0), s, 0)