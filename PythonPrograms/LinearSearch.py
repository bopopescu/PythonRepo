
list = [4,5,6,7,1,2,3]
n = 7
pos = -1

# one way of implementing
for i in list:
    if i == n:
        pos = list.index(i)
        print('Match found at {} position'.format(pos+1))
        break;
else:
    print('Match not found')

# 2nd way of implementation
def search(list,n):
    i = 0
    while(i < len(list)):
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i += 1
    return False

if search(list,n):
    print('Found at {} position'.format(pos+1))
else:
    print('Not Found')