import random

import self as self


class Item(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
        + ', ' + str(self.weight) + '>'
        return result

def maxVal(toConsider, avail):
    """Consider itemler, available çantanın sahip olduğu kapasite"""
    if toConsider == [] or avail == 0:
        result = (0,())
    elif toConsider[0].getWeight() > avail:
        # Listenin ilk elemanı çıkar kalanları gönder.
        result = maxVal(toConsider[1:],avail)
    else:
        #çantaya aldığı kısım
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #çantaya almadığı kısım
        withoutVal, withoutToTake = maxVal(toConsider[1:],avail)
        if withVal > withoutVal:
            result = (withVal, withoutToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def smallTest():
    names = ['a','b','c','d']
    vals = [6,7,8,9]
    weights = [1,1,1,2]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)
print(smallTest())

