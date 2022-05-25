##while True:
##    try:
##        enter = float(input('enter number '))
##        print(100/enter)
##        
##    except ValueError:
##        print('you enter not number!!!')
##    except ZeroDivisionError:
##        print('cannot be divided by zero')
##        #обробка помилок
##    else:
##        print('from the first time it turned out')
##        #додатковий необовязковий оператор, його код виконається якшо не буде помилки у блоці try
##    finally:
##        print('finally')
##        #спрацьовує завжди для того щоб необробленна помилка не завалила програму
##
##print('everything ok')


import sys
url_list = ['error3.txt', 'error1.txt', 'error2.txt', 'error25.txt']
list_defect = []
list_info = []
try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            print('here')
            
        except Exception:
                list_defect.append(url)
                print('there')
                continue
finally:
    r = open('save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close
    print('i make all')
##приклад обробки помилок
    
    







