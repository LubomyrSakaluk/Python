##'r' відкриває для читання (по дефолту)
##'t' відкриває у текстовому режимі (по дефолту)
##'w' відкриває для запису, вміст видаляє, якщо немає файлу, стаорюється новий
##'a' відкриває для дозапису в кінці файлу,якщо немає файлу, стаорюється новий 
##'b' відкриває в бінарному режимі
##'+' відкриває для читання та запису 'r+', 'w+', 'a+'

##import os
##
##list_paths = []
##
##for adress, papka, file in os.walk('c:\\'):
##    for i in file:
##        full_path = os.path.join(adress, i)
##        list_paths.append(full_path)
##
##
##r = open('text.txt', 'w')
##for x in list_paths:
##    r.write(x + '\n')
##
##r.close()
##генеріція шляхів у файл

##r = open('text.txt')

##for i in r:
##    if 'read.py' in i :
##        print(i)
##
##r.close()
##виводимо з файла все що має read.py за допомогою циклу



##r = open('text.txt', 'w')  
##r.write('YOUR TEXT')
##r.close()
## створення файлу та доданий у нього текст

##r = open('text.txt')  
##a = r.read()
##print(a)
##r.close()
##тут ми прочитали текст з файлу


##r = open('video_one.mp4', 'rb')
##y = open('copy video_one.mp4', 'wb')
##
##while True:
##    var = r.read(1048576)
##    print(var.__sizeof__())
##    if var.__sizeof__() == 33:
##        break
##
##    y.write(var)
##
##print('control')
##r.close()
##y.close()
##
####копіювання у бінарному режимі можна задати кількість обєму в ОП


##r = open('text2.txt', 'w', encoding='utf-8')
##r.write('stroka тексту')
##
##r.close()
##
##h = open('text2.txt, 'encoding='utf-8')
##print(h.read())
##файли можуть мати різне кодування і некоректно відкриватися або взагалі, тому потрібно вказувати кодування
##

















