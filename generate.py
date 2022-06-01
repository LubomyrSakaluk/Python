##import os
##h = [9, 8, 7, 6, 5, 3, 2, 1, 5, 5, -2]
##newh = []
##for x in h:
##    newh.append(x*2)
##print(newh)
##звичайне створення нового списку на основі list h

####синтаксис генератора
##n = [x*2 for x in h]
##print(n)
##generate list

##z = {x*2 for x in h}
##print(z)
##generate set

##f = {x: x*2 for x in h}
##print(f)
##generate dictionary
##цей метод швидший для програми

##g = [x for x in h if x % 2 == 0]
##g = [x for x in h if x % 2 == 0 and x > 0]
##print(g)
##print(type(g))
##умова в generate, це ніби фільтр

##g = [os.path.join(z, i)
##     for z, x, c in os.walk('c:\\')
##     for i in c if '.txt' in i]
##print(g)
##розпковка елементів з tuple в generate

##price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

##new_price = {}
##for i in price.keys():
##    new_price[i] = round(price[i] * 0.85, 2)
##print(new_price)
##створення dictionary на основі інщого dictionary
##звичайний
##new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
##print(new_d)
##більш швидкий код
##створення dictionary на основі інщого dictionary в generate


##n =[x for x in os.walk('c:\\')]
##print('here')
####генератор списку
####вест у пам'яті
##z =(y for y in os.walk('c:\\'))
##print('there')
####вираз генератора
####викликає по одному(який обробляється)елементу в пам'ять
##

##def some():
##    list_text = []
##    with open('fgen.txt') as r:
##         for x in r:
##             list_text.append(x)
##    return list_text
####функція завантажує весь текст з файлу по рядку і тримає в памяті
##for i in some():
##     print(i.split())


##def some():
##    list_text = []
##    with open('fgen.txt') as r:
##         for x in r:
##             yield x
####такий метод видає у цикл по одному рядку а не весь список             
##for i in some():
##     print(i.split())


def some():
    list_text = []
    with open('fgen.txt') as r:
         for x in r:
             yield x
 
p = some()

##print(next(p))
##print(next(p))
##print(next(p))
##print(next(p))


for i in p:
    print(i)
##цикл дає можливість обробити помилку коли закінчується інформація














    







