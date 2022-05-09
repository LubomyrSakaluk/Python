##def name(h=1,g=5, *args, key) :
##    print(h)
##    print(g)
##    print(args)
##    print(key)
##
##name(1,2,3,5,6, key=10)
##

####def exclusive_item(*args, key=False) :
####    new_list = []
####    for i in args:
####        for y in i:
####            if y not in new_list:
####               new_list.append(y)
####    if key == True:
####        new_list.sort()
####        return new_list
####
####
####z = [1,2,3,4]
####x = [3,4,5,6,7]
####c = [5,6,4,3,2,6,9,8]
####
####t = exclusive_item(z,x,c, key=True)
####print(t)

##x = 5
##def name():
##    global x
##    x = 100
##    print(x)
##
##name()
##print(x)

##x = 5
##
##def name():
##    y = 10
##    print(x)
##    return y
##h = name()
##print(h)

##x = 5
##
##def name():
##    x = 100
##    return name2(x)
##
##def name2(par):
##    print(par)
##

##x = 5
##def name():
##    x = 10
##    def name2():
##        nonlocal x
##        x = 100
##        print(x)
##
##    name2()
##    print(x)
##
##name()
##print(x)




