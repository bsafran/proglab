import csv,sys

arg1 = sys.argv[1]
path = arg1 + "\\input_hw_2.csv"
arg2 = sys.argv[2]
receiver = arg2 + "\\180401038_hw_2_output.txt"

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
# mean of list
def my_mean(my_list):
    s, t =0,0
    for item in my_list:
        s = s+1
        t = t+item
    mean_ = t/s
    return mean_
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

#file = open("input_hw_2.csv",'r',encoding="utf-8")
with open(path,'r',encoding="utf-8") as file:
    contents = file.read()
    i = 0
    history_list = []
    history_dict = {}
    words = contents.split(";")

    for i in range(3,len(words),3):
        #print(words[i])
        history_list.append(words[i].split("-"))
    for item in range(len(history_list)):
        #print(history_list[item][1])
        if history_list[item][1] in history_dict.keys():
            history_dict[history_list[item][1]] += 1
        else:
            history_dict[history_list[item][1]] = 1

    control = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for j in control:
        if not j in history_dict.keys():
            history_dict[j] = 0

value_list = [(k) for k in history_dict.values()]
value_list = my_sort(value_list)
print(value_list)
median = my_median(value_list)
mean = my_mean(value_list)
output = ["Medyan : ",str(median),"Ortalama : ", str(mean)]

with open(receiver,"w",encoding="utf-8") as write_file:
    for i in range(0,len(output),2):
        write_file.write(output[i] + " " + output[i+1] + "\n")
write_file.close()