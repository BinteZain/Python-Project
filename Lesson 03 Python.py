# Operators , Keywords and Variables :

x = 8                          # (Unary Operators) (work with one operand)
y = -x

print("y = " , y)

a = True                       # (Logical NOT) 
b = not a

print("Logically b = " , b)

x = 5                          # (Bitwise NOT (~)) (binary operations)
y = ~x

print("y = " , y)                               # (with binary function)

print("bin(x) = " , bin(x) , type(bin(x)))      

my_list : list = [1 , 2 , 3 , 4 , 5]            # (Membership Operators) (in  /  not in)

print("my_list = " , my_list)                   
print("4 in my_list = " , 4 in my_list)
print("9 in my_list = " , 9 in my_list)

my_string : str = "Python Course"

print("my_string = " , my_string)
print("z in my_string = " , "z" in my_string)
print("Course in my_string = " , "Course" in my_string)

import keyword                                 # (Python Keywords)

print("the list of \
keyword is : ")

print(keyword.kwlist)

a , b , c = 1 , 35 , "Python"                 # (Assigning different values)

print(a , b , c)

x = 10                                        # (delete a variable using del keyword)

print("x = " , x)

# del x                             
# print(x)                                    # (NameError because x is delete for use of del keyword)

# << practiced by Bint e Zain >>