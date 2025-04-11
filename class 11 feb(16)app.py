# Short Hand If Else /  Ternary Operators :

a = 15 
b = 10

print( "a is larger than b" if a > b else "b is larger than a" )

num = 5

num2 = 20 if num < 10 else 5

print("num2 =" , num2)

print("part 1 complete")

# Enumerated Function :

marks = [55 , 78 , 99 , 64 , 87]                         # (enumerated with integers)

for index , mark in enumerate(marks) :
    print(mark)
    if (index == 2) :
        print("Good Performance")                        # (achi percentage ke pass hi print ho)


names = ["ali" , "badar" , "siyam"]                      # (enumerated with string)

for index , name in enumerate(names) :
    print(name)
    if (index == 2):
        print("Good Boy")


names = ["Ali" , "Badar" , "Siyam"]

for index , name in enumerate(names) :
     print("Good Boy")
     if names[1] == "Badar" :
       

        print(f"name{index} , {name}")

print("part 2 complete")

# Map Function :

numbers = [1 , 2 , 3 , 4 , 5]

def square(num : int) :
    return num * num

square_list = list(map(square,numbers))

print("numbers =" , numbers)
print("square_list =" , square_list)


def cube(x):
    return x * x * x 

print(cube(2))

l = [ 1 , 2 , 4 , 6 , 4 , 3]
newl = list(map(cube,l))

print(newl)

# Filter Function :

def filter_function(a) :                  # (agar a bara hai to 4 se bare elements print karo)
    return a > 4

newlist = list(filter(filter_function , l))

print(newlist)

# Reduce Function :

from functools import reduce

numbers = [1 , 2 , 3 , 4 , 5]

sum = reduce(lambda x , y : x + y , numbers)

print(sum)

print("part 3 complete")

# << practiced by Bint e Zain >>