import sys - імпорт модудя

import newmod #імпорт модудя
print(newmod.k) #виклик перемінної з модуля
print(newmod.nef(3)) #виклик функції з модуля
print(dir(newmod)) #показує імена в модулю
print(help(newmod)) #покаже всю інфу по цьому модулю
print(help(newmod.newf)) #інфа по конкретні функції з модулю
newmod.path #виклик у модулі певного елементу

from newmod import * #все знаходиться у області видимості
print(dir()) #показує імена в модулю
print(k)
print(nef(3))
#такий імпорт при створенні одинакової перемінної буде заміна значення

from newmod imort newf, k













