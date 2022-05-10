##def name(h=1,g=5, *args, key) :
##    print(h)
##    print(g)
##    print(args)
##    print(key)
##
##name(1,2,3,5,6, key=10)
##

####def exclusive_item(*args, key=False) :
####    new_list = []
####    for i in args:
####        for y in i:
####            if y not in new_list:
####               new_list.append(y)
####    if key == True:
####        new_list.sort()
####        return new_list
####
####
####z = [1,2,3,4]
####x = [3,4,5,6,7]
####c = [5,6,4,3,2,6,9,8]
####
####t = exclusive_item(z,x,c, key=True)
####print(t)

##x = 5
##def name():
##    global x
##    x = 100
##    print(x)
##
##name()
##print(x)

##x = 5
##
##def name():
##    y = 10
##    print(x)
##    return y
##h = name()
##print(h)

##x = 5
##
##def name():
##    x = 100
##    return name2(x)
##
##def name2(par):
##    print(par)
##

##x = 5
##def name():
##    x = 10
##    def name2():
##        nonlocal x
##        x = 100
##        print(x)
##
##    name2()
##    print(x)
##
##name()
##print(x)

import math

PI = math.pi

def radius():
    n = float(input('діаметр циліндра у см: '))## функція
    n /= 2
    return n

def height():
    m = float(input('висота ціліндру у см: '))
    return m

def volume():
    r = radius() #запуск функції
    h = height()
    s = PI*r**2
    v = s*h
    return v

print('обєм циліндру', volume(), 'см3: ') ## запуск функції

def massa(g):
    n = float(input('питома вага г/см3: '))
    return g*n/1000
print('вага циліндру в кг: ', massa(volume()))

##всі перемінні є створенні у функціях це дає можливість
##працювати у локальній області коли викликана функція.
##у такому випадку в оперативні памяті не залишаються значення
##всіх перемінних, а тількі кінцевих у глобальні області.

#також не потрібно слідкувати за перемінним
#
#


