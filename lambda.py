##def some(x):
##    return x/5
####звичайна функція
##
##
##var = lambda x: x/5
####функція lambda (анонімна)
##
##print(some(7))
##
##print(var(7))
##
##
####інтерпритатор бачить їх одинаково


##Example of lambda:
##комфортна для орієнтування в коді
##також економить місце, запис в один рядок 
list_of = [['adam', 29], ['jonny', 3*1/12], ['jess', 25]]
##r = sorted(list_of, key=lambda x: x[1])
##print(r)

x = list(filter(lambda x: x[1] > 18, list_of))
print(x)
##функція фільтр: створення на основі цього спису нового з виключенням деяких значень 













