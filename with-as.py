##r = open('file.txt', 'a')
##try:
##    r.write('something' + '\n')
##    10/0
##    r.write('fender')
##finally:
##    r.close()

##print('ok')
##у такому випадку всі помилки не обробиш, а також такий код вважається неправильним


with open('file.txt', 'a') as r:
    r.write('something' + '\n')
    10/0
    r.write(fender)

print('ok')
##контекстні менеджери(with,as) потрібні для безпечного збереження при помилці
