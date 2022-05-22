##s = 'sTroka texta'
##
##s1 = s.upper() #все у верхній регістр
##print(s1)
##s2 = s.lower() #все у нижній регістр
##print(s2)
##s3 = s.capitalize() #перша у верхній регістр
##print(s3)
##
##path = 'c:/Users/Desktop/Python' #заміна
##path1 = path.replace('/', '\\')
##print(path1)
##
##r = path1.split('\\') #розбити по розділу
##print(r)
##print(r[-1])
##
##q = open('textstr.txt')
##r1 = q.read()
##list_signs = ['(',')', '"', '(', ')', '\n']
##for i in list_signs:
##    r1 = r1.replace(i, '')
##print(r1)
##
##r2 = r1.split()
##print(r2)
##
##new_text = '_*_'.join(r2)
##print(new_text)



enter = input('your name: ') #добавляє прямо у строку
##s = 'Hello %s, I am %s' % (enter, 'Python')  
##print(s)

##s1 = 'Hello {1}, I am {0}'.format(enter, 'Python')
##print(s1)

var = 'string' #новий спосіб форматування str  f-string
s2 = f'Hello {enter}, I can do it in f-string {2+2, len(var)}' 
print(s2)



