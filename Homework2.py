# VADZIM ZHURAULIOU
# Date: 05/06/2023
# Description: Homework 2
# Grodno IT Academy Python 3.9.5

# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов

# пример названия репозитория для гитхаба: kazukevich_homework2
# добавьте в репозиторий с домашним задание файл readme с датой сдачи, фамилией и именем выполнившего и кратким описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown

#Напишите программу, ĸоторая считает общую цену.
#Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
#Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
#Уточнение:
#Используйте функцию return чтобы ответ был в рублях и копейках.
#Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"
def common_price(m, n, s, l):
    from decimal import Decimal
    if type(m)==str or type(n)==str or type(s)==str or type(l)==str: #создаем условие, чтобы строчные переменные не участвовали в функции
        return False
    elif m<0 or n<0 or s<=0 or l<0: #убираем отрицательные значения из выборки
        return False
    elif m==0 and n==0:
        return False
    else:
        cost=Decimal(m*100/s+n/s) #определяем стоимость в копейках
        cost=cost.quantize(Decimal(0))
        m=Decimal(cost*l//100)
        n=Decimal(cost*l%100)
        m=m.quantize(Decimal(0))
        n=n.quantize(Decimal(0))

       
        return "Общая цена составляет " + str(m) + " рублей и " + str(n) + " копеек за " + str(l) + " товаров"

# Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если нет, вывести False.
# Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.
def triangle(a, b, c):
    import math #импортируем библиотеку для расчета корня
    if not type(a)==int or not type(b)== int or not type(c)== int: #убираем из выборки значения нецелые
        if not type(a)==float or not type(b)== float or not type(c)== float: #убираем из выборки недробные значения
            return False
        elif a+b<c or a+c<b or c+b<a: #убираем условие о треугольнике для дробных
            return False
        else:
            p=float(a+b+c)/2 #считаем для варианта с дробным значением результат
            s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),4)
            return s
    elif a+b<c or a+c<b or c+b<a: #условие о треугольнике для целых значений
        return False
    else:
        p=float(a+b+c)/2 #делаем расчет по целым значениям по площади
        s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),4)
        return s

# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если введено "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"
def longest_word(sentence):
    import string #импортируем библиотеку для использования значения string.punctuation
    if sentence=='' or not type(sentence)==str: #убираем результаты, где входные значения не строка или строка пустая
        return False
    else:
        k=sentence.translate(str.maketrans('','',string.punctuation)) #убираем пунктуацию в предложении
        longest_word='' #создаем пустую строку
        for word in k.split(' '): #итерируем разделенную строку к и сравниваем поочередно длины слов. Помещая самое длинное в
            if len(word) >=len(longest_word):
                longest_word=word
        return longest_word

# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
def uniques(repeating_string):
    if not type(repeating_string) ==str:
        return False
    else:
        m=repeating_string.replace(' ','') #убираем пробелы в предложении
        k='' #создаем пустую строку
        for el in m: #создаем цикл, в ходе которого помещаем в пустую строку все не повторяющиеся элементы
            if el not in k:
                k +=el
        return k

# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.

def count_string_capitalization(mixed_string):
    if type(mixed_string) == str: 
        big = 0 
        small = 0
        for i in mixed_string: 
            if i.islower():
                small += 1
            elif i.isupper():
                big += 1

        return f"В строке '{mixed_string}' {big} большие и {small} маленькие буквы"
    else:
        return False

#%%

#%%
