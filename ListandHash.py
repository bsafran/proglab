from sympy import FiniteSet

def my_h(list1):
    my_d ={}
    for item in list1:
        if item not in my_d:
            my_d[item] = 1
        else:
            my_d[item] = item+1
    return my_d

def lookup(d,v):
    for key in d:
        if(d[key] == v):
            return key
    else:
        return -1

list_1 = [1,4,7,84,3,62,33]
my_d=dict()
my_d={1:'bir',2:2,'3':'three'}
for key in my_d.keys():
    print(key,my_d[key])

print(5 in my_d) # 5 my_d içinde var mı yokmu ?

if -10 not in my_d: # -10 var mı diye bakar. yoksa girer.
    my_d[-10] = 50
print(my_d)

print(my_h([2,3,4,6,2,5,6,5,6,6,6,6,2]))

#print(lookup(my_d),2)
# 6 Mart Cuma
def probability(space,event):
    return len(event)//len(space)

def check_prime(number):
    if(number!=1):
        for factor in range(2,number):
            if(number%factor == 0):
                return False
    else:
        return False
    return True
space = FiniteSet(*range(1,20))
primes = []
for num in space:
    if check_prime(num):
        primes.append(num)
event = FiniteSet(*primes)
p = probability(space,event)
print(p)