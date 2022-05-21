##t = {'a', 'y', 3, 5, 7, 8, (2,4)}

##y = set()

##може складатися з нехмінних типів даних int,str,tuple
##також set немає індексації, працювати можна тільки за допомогою методів
##якшо створити пусті {} то це буде dict а зі значеннями {1, 2} set
##import time
##
##def f(*args):
##    list_new = []
##    for i in args:
##        for y in i:
##            if y not in list_new:
##                list_new.append(y)
##    return list_new
##
##z = list(range(10000))
##x = list(range(5000, 15000))
##c = list(range(10000, 20000))
##
##start = time.time()
##f(z,x,c)
##stop = time.time() - start
##print(stop)
##
##start2 = time.time()
##r = set(z)
##t = r.union(set(x), set(c))
##stop2 = time.time() - start2
##print(stop2)
##вираховує час за допомогою модуля time 
##на роботу функції зі списками йде значно більше часу ніж на операцію обєднання set за допомогою методів set

z = {1,2,3,4,5}
x = {3,4,5,6,7}
##z.add(6)
##додає значення в set
##z.discard(6)
##видаляє значення і не видає помилки якщо такого значення немає 
##z.remove(8)
##видаляє значення і видає помилки якщо такого значення немає , яку можна обробити. 
##y = z.union(x)
##обєднює та зберігає set у нову перемінну
##z.update(x)
##обєднює та зберігає set
##t = z.intersection(x)
##виводить спільні єлементи у нову перемінну
##e = z.difference(x)
##цей метод показує які є в z але немає в x

new = set()

r = open('textset.txt')
r1 = set(r.read().split())
r.close

r = open('textset2.txt')
r2 = set(r.read().split())
r.close()

new = r1.intersection(r2)

print(new)
##шукає спільні слова у текстових документах за допомогою метода difference(x) можна знайт різницю 


