# Homework2
В первой задаче была поставлена цель перевода цены. Изначально для осуществления такого перевода был импортирован модуль Decimal с помощью записи from decimal import Decimal
Далее в ходе задачи были отсеяны значения, которые не являются строчными с помощью функции type()==str: return False. В последствии также были отсеяны входящие отрицательные значения в рамках переменных. 

def common_price(m, n, s, l):
    from decimal import Decimal
    if type(m)==str or type(n)==str or type(s)==str or type(l)==str: #создаем условие, чтобы строчные переменные не участвовали в функции
        return False
    elif m<0 or n<0 or s<=0 or l<0: #убираем отрицательные значения из выборки
        return False
    elif s==0:
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
