import os
import re
all_list = []
output_list = []
len_all_list = 0
output = "180401038_hw_1_output.txt"

def get_output(input_list):
    output = open(os.getcwd() + "\\180401038_hw_1_output.txt", "a", encoding="utf-8")

    output.write("\n----------------------------- \n")
    output.write("-->" + input_list)

def get_hist(list,search):
    my_hist = {}
    i = 0
    for w in list:
        i+= 1
        temp = i
        j = 0
        if w == search[j]:
            j += 1
            while (j != len(search)):
                if(list[i] == search[j]):

                    i+=1
                    j+=1
                else:
                    i = temp
                    break
            else:
                if list[i] in my_hist.keys():

                    my_hist[list[i]] += 1
                    i = temp
                else:

                    my_hist[list[i]] = 1
                    i = temp
    return my_hist

def get_words2(my_file):
    my_list=[]
    f=open(my_file,"r+")
    contents=f.readlines()
    for line in contents:

        words=line.split(" ")
        for word in words:
            my_list.append(word)
    f.close()
    return my_list

txt_list=os.listdir(os.getcwd()+"\\data_files")
for txt in txt_list:
    all_list.extend(get_words2(os.getcwd()+"\\data_files\\"+txt))

text = open(os.getcwd() + "\\180401038_hw_1_output.txt", "r+", encoding="utf-8")
contents = text.readlines()
for line in contents:
    text_list = []
    words = line.split(" ")
    for word in words:
        text_list.append(word)
    if(len(text_list) <= 5):
        for w in range(len(text_list)):
            text_list[w] = re.sub('\n', '', text_list[w])
        else:
            output_list = get_hist(all_list, text_list)
            max_key = max(output_list)
            get_output(max_key)
    else:
        get_output("Hata. En fazla 5 kelime girebilirsiniz.")
text.close()



