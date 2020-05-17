guessArray ={'python','java','perl','C++','C#'}
print('guess the correct string from given array : ')
print(guessArray)

str_lucky = 'python'
maxTry = 3
currentTry =1

while currentTry <= maxTry:
    language = input('Enter language of your choice : ')
    if language == str_lucky:
        print('Congratualtions!!!! You guessed it correctly')
        break
    else:
       # language = input('Enter language of your choice : ')
        currentTry+=1

if currentTry > maxTry:
    print('Sorry you are out of try.')
