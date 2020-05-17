
courses =['Bengali','English','History','Geography','Maths']
# To print a whole list
print(courses)
# get the length of list
print('Length of the list course is : ')
print(len(courses))
# getting a range of value
print(courses[:2])
print(courses[2:4])
print(courses[2:])
# getting the last element of the list
print(courses[-1])
# Add another item
courses.append('Arts')
print(courses)
# Add another item in a specific position
courses.insert(1,'Science')
print(courses)
# merge two different lists
courses_1 = ['compSci','LifeSci']
    # Make list of lists
# add whole list as a first element of another list
courses.insert(0,courses_1)
print(courses)
courses.append(courses_1)
print(courses)
# add only the list values at the end of a list
courses.extend(courses_1)
print(courses)
# remove items from list
courses.remove(courses_1)
print(courses)
# it will by default remove the last item
popped=courses.pop()
print(courses)
print(popped)
courses_1.sort()
print(courses_1)
# sort list
courses.reverse()
print(courses)
