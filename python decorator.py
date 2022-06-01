##def decor(f):
##    def wrapper():
##        print('first code')
##        f()
##        print('second code')
##    return wrapper
##
##
##
##@decor  # make = decor(make)
##def make():
##    enter = input('enter someting... ')
##    print(enter)
##
##
##print('here')
##make()
##
####decorator дозваляє модифікувати функцію не вмішуючись в її код


def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print('one more time ')
            h = f()
        return h
    return wrapper

@decor
def make():
    enter = float(input('enter number: '))
    return enter
@decor
def make2():
    enter = float(input('enter number2: '))
    return enter

make2()
make()
###Обробка помилок у decorator










    






            
