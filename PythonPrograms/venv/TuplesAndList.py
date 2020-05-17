print('-----------------------Here we are using list--------------------------------')
# Mutable
list_1 = ['Course1','Course2','Course3','Course4','Course5']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

# As list_1 and list_2 are pointed to same mutable reference hence the value change will reflect in both the cases
print(list_1)
print(list_2)

print('-----------------------Here we are using tuple--------------------------------')
# Immutable
tuple_1 = ('Course1','Course2','Course3','Course4','Course5')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0]='Art' --> can not happen and will trow an error while execution as tuple does not support modification

print(tuple_1)
print(tuple_2)