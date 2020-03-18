from sympy import FiniteSet
from fractions import Fraction


def my_histogram(inlist=[5, 0, 25, 100, 0, 0, 5, 100, 5]):  # This function returns a dictionary.
    my_dct = {}

    for i in inlist:
        if i in my_dct:
            my_dct[i] += 1

        else:
            my_dct[i] = 1

    return my_dct


def lookup(dict, value):

    try:
        for k in dict:
            if dict[k] == value:
                return k
    except:
        print("Value not found")


# exlist = [2,3,4,5,2,1,4,3,5,5]
# print(lookup(my_histogram(exlist), 2))

known = {0: 0, 1: 1}


def fibo_rec(n):  # This function finds the fibonacci number using known dictionary.

    if n in known:
        return known[n]
    else:
        result = fibo_rec(n - 1) + fibo_rec(n - 2)
        known[n] = result
        return result

s = FiniteSet(1, 1.5, Fraction(1, 5), 1, 1.5, 7, 42)
t = FiniteSet(Fraction(1, 5), 1, 5, 1, 1, 91, 87)

for member in s:
    print(member)

if s == t:
    print("True")
else:
    print("False")


