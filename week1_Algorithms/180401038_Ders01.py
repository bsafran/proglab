import random
def my_freqeuency_with_list_of_tuples(list_1):
    frequency_list = []
    for i in range(len(list_1)):
        s = False
        for j in range(len(frequency_list)):
            if(list_1[i] == frequency_list[j][0]):
                frequency_list[j][1] += 1
                s = True
        if(s == False):
            frequency_list.append([list_1[i],1])
    return frequency_list

def my_frequency_with_dict(list):
    frequency_dict = {}
    for item in list:
        if (item in frequency_dict):
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

def get_n_random_numbers(n=10,min_= -5,max_=5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers
my_list = [2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
print(my_frequency_with_dict(my_list),my_freqeuency_with_list_of_tuples(my_list))