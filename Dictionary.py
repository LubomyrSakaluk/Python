##d1 = {'a': 7}
####ці дужки позначають dictionary у цих дужках позначають через :
##d2 = dict(a = 7)
##d3 = dict.fromkeys('[1, 2, 3, 4, 5]' 'value')
##
##price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
####ключ: значення ключем може бути (int,float,str,tuple) 
##users = {
##    'Alex7': {'password': 9856214, 'id': 1957},
##    'Jimmy99': {'password': 1236487, 'id': 9654},
##    'Bob33': {'password': 9546752, 'id': 6453}
##    }
##
##def buy():
##    pay = 0
##    while True:
##        enter = input('Whats buy???\n')
##        if enter == 'end':
##            break
##        pay += price[enter]
##    return pay
    
##d1 = {'a': 7, 'b': 9}
##d2 = dict([[1,2],[3,4],[5,6]])
##d3 = dict.fromkeys('[1, 2, 3, 4, 5]' 'value')

##d5 = d1
##цей випадок передає посилання і всюди буде вказаний один dictionary 

##d5 = d1.copy()
##стаорює копію dictionary

##print(d1.items())
##повкртає нам list зроблений з tuple потрібно для того щоб працювати з циклом for

##print(d1.keys())
##повертає ключі dictionary у вигляді list потрібно для того щоб працювати з циклом for

##print(d1.values())
##повертая значення dictionary у вигляді list потрібно для того щоб працювати з циклом for

##d1.update(d2)
##print(d1)
##добавляє пару ключ значення з іншого dictionary


##if 'c' in d1:
##    d1['c']
##y = d1.get('c', 'value')
##print(y)
##повертає значення в перемінну по ключу якого там немає і замість помилки напише none або добавлене вами значення


##t = d1.pop('a')
##print(t, d1)
##дозваляє видалити пару ключ значення видалити з dictionary а також повернути у значення у перемінну 



price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

##new_price = {}
##for i in price:
##    new_price[i] = round(price[i] * 0.85, 2)

##print(price)
##print(new_price)
##ітерація dictionary по ключам


##for i in price.items():
##    print(i)
##
##for key, value in price.items():
##    print(key)
##    print(value)
##ітерація dictionary методом items поаертає уявленний обєкт 
##new = {}
##for key, value in price.items():
##    new[value] = key
##print(new)
####реверс dictionary методом items


##for value in price.values():
##    print(value)
##метод values дає змогу працювати зі зніченнями нерухаючи ключі, ітерація проведена по значенню


price.keys()
## проводить ітерацію по ключах







