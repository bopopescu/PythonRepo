

def fibonacciLengthWise(len):
    a=0
    b=1
    if len<=0:
        print("Not valid input. Enter positive number only.")
    elif len==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,len):
            temp = a+b
            a=b
            b=temp
            print(temp)

def fibonacciRangeWise(lstNum):
    a = 0
    b = 1
    if lstNum <= 0:
        print("Not valid input. Enter positive number only.")
    elif lstNum == 1:
        print(a)
    else:
        print(a)
        print(b)
        while((a+b)<=lstNum):
            temp = a + b
            a = b
            b = temp
            print(temp)

fibonacciRangeWise(145)