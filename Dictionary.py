d1 = {'a': 7}#ці дужки позначають dictionary у цих дужках позначають через :
d2 = dict(a = 7)
d3 = dict.fromkeys('[1, 2, 3, 4, 5]')

price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
#ключ: значення ключем може бути (int,float,str,tuple) 
users = {
    'Alex7': {'password': 9856214, 'id': 1957},
    'Jimmy99': {'password': 1236487, 'id': 9654},
    'Bob33': {'password': 9546752, 'id': 6453}
    }

def buy():
    pay = 0
    while True:
        enter = input('Whats buy???\n')
        if enter == 'end':
            break
        pay += price[enter]
        return pay
    
