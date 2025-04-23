# Strings and Type Casting :

my_string = """I want                 
to become
a developer"""

print(my_string)                 # (triple quotes for multiple lines string)

my_str = "Python Coding"

words = my_str.split()
print(words)

words = my_str.split(" ")
print(words)

words = my_str.split("n")                     # (n hat jayega)
print(words)

name  :str = "John"                          # (str.forrmat())
age :int = 30

my_data : str = "My name is {} and i am {} years old".format(age , name) # (order matters)
print("Wrong information = " , my_data)

my_data :str = "My name is {1} and i am {0} years old".format(age , name) # (use index no)
print("Write information = " , my_data)

my_data :str = f"My name is {name} and i am {age} years old."              # (with F-String) 
print("Write information = " , my_data)

a : str = "Continue"                     # (Pool of String Literals in Python)
b : str = "Continue"

print(id(a))
print(id(b))                            # (dono ki same id hai memory bhi same hi ayegi)

c : str = a + ""                        # (khali string hai ye bhi same memory dikhayega)
d : str = a + " "

print(id(c))
print(id(d))

import sys                             # (Interning) 

a = sys.intern("Hy")
b = sys.intern("Hy")

print(a is b)                          # (q ke same memory mein hai)

base_string = " Hy "                   # (String Repetition)
repetition_count = 3

repeated_string = base_string * repetition_count

print(f"Original String: {base_string}")
print(f"Repetiton_count: {repetition_count}")
print(f"repeated_string: {repeated_string}")

word = "Mango"                                 # (Comparison operators in an if staement)

if word > "Apple" :
    print(f"{word} comes after apple in alphabetical order.")
    
else :
    print(f"{word} comes before apple in alphabetical order.")    
    
num_str = "100"                                # (Implicit Type Casting (Automatic Conversion))
num_int = 5

print(int(num_str) + num_int)
print(num_str + str(num_int))

print("bool(1)          = " , bool(1))            # (Boolean Conversion bool())
print("bool(0)          = " , bool(0))
print("bool(-10)        = " , bool(-10))          # (Non-zero numbers are true)
print("bool("")         = " , bool(""))           # (Empty string)
print("bool(`Hello`)    = " , bool("Hello"))      # (Non-empty string)
print("bool([])         = " , bool([]))           # (Empty list)
print("bool([1,2])      = " , bool([1,2]))        # (Non-empty list)

tup : tuple = (1 , 2.7 , 3 , "abc")               # (List , Tuple , Set  and Dict Conversion)
lst = list(tup)

print("Converted in list = " , lst , type(lst))

lst : list = [1 , 2 , 3 , 4 , 5 , 4 , "Python practice"]
s = set(lst)

print("Converted in set = " , s , type(s))

lst : list = [("name" , "Guard" , "age" , 30)]
d = dict(lst)

print("Converted is dictionary = " , d , type(d))

# << practiced by Bint e Zain >>