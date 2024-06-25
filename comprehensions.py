def square(x) :
    return x**2 

import pprint

printer = pprint.PrettyPrinter()


options  = ["John Coltrane", "Miles Davis", "Jackie McClean", "Grachan Moncur", "Rashaan Roland Kirk", "bob", ""]


#Chaained conditions
valid_strings = [
    string 
    for string in options 
    if len(string) >= 2
    if len(string.split(" ")) >= 2
    if string[0] == "J"
]

print(valid_strings)


#flattening a matrix 
matrix = [[1,2,3], [4,5,6], [7,8,9]]

flattened = []
for row in matrix :
    for num in row :
        flattened.append(num)
print(flattened)

flattened_c = [num for row in matrix for num in row]
print(flattened_c)

#categorize numbers as even or odd 
categories = []

for number in range(10) :
    if number % 2 == 0 :
        categories.append("Even")
    else :
        categories.append("Odd")

print(categories)

categories_c = ["Even" if x % 2 == 0 else "Odd" for x in range(10) ]

print(categories_c)

#nested list comprehension 
#build a 3D list 

lst = []

for a in range(5) :
    l1 = []
    for b in range (5) :
        l2 = []
        for num in range(5) :
            l2.append(num)
        l1.append(l2)
    lst.append(l1)

printer.pprint(lst)



# + is anonymous variable 
lst_c = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]

printer.pprint(lst_c)


#List comp with functions 


squared_numbers = [square(x) for x in range(10)]

print(squared_numbers)

#creating a dictionary 

pairs = [("a", 1), ("b", 2), ("c", 3)]

my_dict = {k: v for k, v in pairs}

print(my_dict)


#set comprehension 
nums = [1, 1, 1, 2, 2, 4, 5, 7, 8 ] 


unique_squared = {x**2 for x in }  #{ } without keys is a set , so unique numbers 
print(unique_squared)

# Generator Comprehension 

sum_of_squares = sum(x**2 for x in range(100000))

###if we did this  --> sum( [ x**2 for x in range(1000000) ] ) we would generate the list first



