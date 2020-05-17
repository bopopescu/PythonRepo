from math import sqrt

user_input = 'Y'
# check primes withing sqRoot_num
while (user_input != 'N') :
    num = int(input('Enter any integer to check if the number is Prime.'))
    sqRoot_num = int(sqrt(num));
    for i in range(2,sqRoot_num):
        if sqRoot_num % i == 0 :
            print(num,' Not Prime')
            break
    else:
        print(num, " Is Prime.")
    user_input = input("If you not want to continue enter 'N'")