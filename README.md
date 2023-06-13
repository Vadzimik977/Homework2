# Homework2
# Первая задача 
В первой задаче была поставлена цель перевода цены. Изначально для осуществления такого перевода был импортирован модуль Decimal с помощью записи from decimal import Decimal
Далее в ходе задачи были отсеяны значения, которые не являются строчными с помощью функции type()==str: return False. В последствии также были отсеяны входящие отрицательные значения в рамках переменных. Также в случае, если рубли и копейки на входе были равны 0, то также функция возвращает False. Для этого была реализована запись elif m==0 and n==0.
Далее, когда все лишние значения были отсеяны происходит подсчет сразу общей цены всей продукции в копейках с помощью cost=Decimal(m*100/s+n/s)
Далее полученное значение округляется с помощью  cost=cost.quantize(Decimal(0))
Далее также определяются новые значения m и n (то есть значения за то количество единиц, которое требуется найти, то есть новая цена за количество).
Также оба данных значения округляются аналогичным образом с общей стоимостью в копейках
На выход был возврат функции:


        return "Общая цена составляет " + str(m) + " рублей и " + str(n) + " копеек за " + str(l) + " товаров"
# Вторая задача
Во второй задаче было следующее условие 
Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
Если нет, вывести False.
Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.

Сразу была импортирована библиотека math для вычисления корня из числа в последующем import math.
Далее были убраны из выборки нецелые значения if not type(a)==int or not type(b)== int or not type(c)== int:
После этого подобным образом были убраны недробные значения (то есть если значение не целое и не дробное, то такой формат не должен идти дальше в обработку). 
После этого была проверка на то, является ли фигура треугольником посредством  elif a+b<c or a+c<b or c+b<a:       
Далее для целых и нецелых значений была рассчитана площадь через запись p=float(a+b+c)/2 (рассчитан полупериметр);  s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),4) (определена площадь). 
 
# Третья задача
В третьей задаче требуется найти самое длинное слово.
Для начала импортируем библиотеку для использования значения string.punctuation с помощью записи import string
Далее отсеиваем значения, где строка пустая или не строка вовсе.  if sentence=='' or not type(sentence)==str
Далее убираем пунктуацию в строке с помошью оператора .translate(str.maketrans)
Создаем пустую строку  longest_word=''.
Далее создаем цикл и проходим через все значения входящей строки (строка разделена split). Если элемент обладает длиной больше, чем слово в пустой строке, то в пустую строку помещается он. Далее возвращается самое длинное слово. 
    

# Четвертая задача
Сразу были убраны варианты, когда на входе не строчные значения if not type(repeating_string) ==str: return False
Далее с помощью оператора .replace были убраны пробелы в предложении. 
После эьтого создана пустая строка к.
Далее с помощью цикла в пустую строку помещены все не повторяющиеся элементы. 
В цикле прописано if el not in k: k +=el.
Далее возвращена переменная к. 
        
# Пятая задача 
Сразу 

def count_string_capitalization(mixed_string):
    if type(mixed_string) == str: #убираем все результаты кроме строчных
        big = 0 #создаем пустые переменные
        small = 0
        for i in mixed_string: #создаем цикл, в котором создаем условие для подсчета строчных и прописных букв. Помещаем маленькие в одну переменную, а большие в другую
            if i.islower():
                small += 1
            elif i.isupper():
                big += 1

        return f"В строке '{mixed_string}' {big} большие и {small} маленькие буквы"
    else:
        return False

