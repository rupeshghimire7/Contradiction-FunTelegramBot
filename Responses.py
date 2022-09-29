def poppin(list1):
    return list1.pop()


def something():
    list1 = ['a','b','c','d']
    for i in list1:
        print(len(list1))
        print(list1)
        x = list1.pop()
        # x = poppin(list1)
        print(x)      
    print(list1)

something()
