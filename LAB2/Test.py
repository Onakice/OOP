# Creating a List
List = []
print("Blank List : ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers : ")
print(List)

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Computer', 4, 'Eng', 6, 'KMITL']
print("\nList with the use of Mixed Values : ")
print(List)

print('########################################')
####################################################

# creating lisdt
nested_list = [1, 2, ['a', 1], 3]

print('nested_list = ', nested_list)
print('nested_list[0] = ', nested_list[0])
print('nested_list[2] = ', nested_list[2])
print('nested_list[2][0] = ', nested_list[2][0])
print('nested_list[-1] = ', nested_list[-1])
print('nested_list[-3] = ', nested_list[-3])


languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[-1])    # C++

# access item at index 2
print(languages[-3])    # Python

print('########################################')
###########################################

# List can Slicing

list1 = ['physics', 'chemistry', 'calculas', 'biology']
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0] : ", list1[0])
print("list1[-1] : ", list1[-1])
print("list2[3] : ", list2[3])
print("list2[-4] : ",  list2[-4])
print("list2[1:5] : ", list2[1:5])
print("list2[::2] : ", list2[::2])
print("list2[2::2] : ", list2[2::2])
print("list2[2:7:2] : ",list2[2:7:2])
print("list2[:7] : ", list2[:7])
print("list2[4:] : ", list2[4:])

print('########################################')
##############################################

# Command creating list

x = list('abcde')
print("x = ", x)

y = list('fghij')
f = [1,2,3]
b = [1,2,3]
c = b
d = list(b)
print("y = ", y)
print("f = ", f)

print('########################################')
##############################################

# + list

flowers = ['Rose', 'Lily', 'Tulip']
flowers += ['Jasmine']
print('flowers = ', flowers)

flower = ['Rose', 'Lily', 'Tulip']
flower += 'Jasmine'
print('flower = ', flower)

print('########################################')
###############################################

# List is Object can + by method append

# Appending and Extending lists in Python
# append
odd = [1, 3, 5]

odd.append(7)

print('odd.append : ', odd)

# extend
odd = [1, 3, 5]
odd.extend([9, 11, 13])
print('odd.extend : ', odd)

print('########################################')
##################################################

odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

print('change the 1st item odd : ', odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print('Change 2nd to 4th items odd : ', odd)

print('########################################')
##################################################

# delete data from List

flowers = ['Rose', 'Lily', 'Tulip', 'Sunflower']
print(flowers)

del flowers[2]
print(flowers)

flowers.pop(0)
print(flowers)

flowers.clear()
print(flowers)

print('########################################')

################################################

# compare List

flowers = ['Rose']
print('Rose' in flowers)

print('########################################')

##############################################

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print( h_letters )

# Shorter than
j_letters = [ letter for letter in 'human']
print( j_letters )

print('########################################')

###############################################

newlist = ["three" if x == 3 else x \
           for x in range(1,10)]
print(newlist)

print('########################################')

##############################################

number_list = [ x for x in range(20) \
               if x % 2 == 0]
print(number_list)

num_list = [ y for y in range(100) \
            if y % 2 == 0 if y % 5 == 0]
print(num_list)

print('########################################')

################################################

