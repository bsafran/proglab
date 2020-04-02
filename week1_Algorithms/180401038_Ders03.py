import random
def get_n_random_numbers(n=10,min_= -5,max_=5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers

#lineer search on list
def my_linear_search(my_list,item_search):
    found = (-1,-1) #default eğer listede yoksa
    n = len(my_list)
    for indis in range(n):
        if my_list[indis] == item_search:
            found = (my_list[indis],indis)
    return found
# mean of list
def my_mean(my_list):
    s, t =0,0
    for item in my_list:
        s = s+1
        t = t+item
    mean_ = t/s
    return mean_
# sort the list
def my_sort(my_list):
    n = len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j] < my_list[j+1]):
                # print("swap")
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list
# binary search on a sorted list
def my_binary_search(my_list,item_search):
    found = (-1,-1)
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low+high) // 2

        if my_list[mid] == item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    return found
# median of list
def my_median(my_list):
    n = len(my_list)
    if n%2 == 1:
        middle = int(n/2)
        median = my_list[middle]
        #print(median)
    else:
        middle_1 = int(n/2)
        middle_2 = int(n/2)+1
        median = (my_list[middle_1-1]+my_list[middle_2-1])/2
        #print(median)
    return median
my_list1 = get_n_random_numbers(10,-5,5)
print(my_list1,my_linear_search(my_list1,4))
print("Ortalama:",my_mean(my_list1))
print("Sıralı Dizi:",my_sort(my_list1))
print(my_binary_search(my_list1,4))
print("Median:",my_median(my_list1))