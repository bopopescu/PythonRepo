

list = [23,45,12,67,32,54,98,76,11,19,56]



def sort(list):
    for i in range(len(list) - 1):
        flag = False
        for j in range(len(list) - i - 1):
            temp = 0;
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
                flag = True
        if flag == False:
            break
    print(list)

sort(list)

