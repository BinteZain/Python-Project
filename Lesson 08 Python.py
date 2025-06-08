#  Modules and Functions :

import math                                   # (Built-in Modules (Standard Library))
print("Square of 100 = " , math.sqrt(100))

import math                                   # (Basic import)
print(math.pi)

import numpy as np                            # (Import with Alias (as))
print(np.array([1 , 2 , 3]))

from math import sqrt , pi                    # (import Specific functions or Variables (from...import...))
print("Square of 16 = " , sqrt(16))
print(pi)

from math import *                            # (import everything) (not recommenden for large Modeules)
print(sin(0))

# (Functions)

def my_function() :                           # (Global function matlab jahan se chahen call karo)
    print("Hello World")
    
my_function()    

import random                                 # (built-in modules)
print("Randomly = " , random.random())

def greetings() :                             # (Syntax of function)
    "its a docstring"
    greet = "Good Performance"
    return greet

message = greetings()
print(message)

def modify_value(x)  :                        # (Pass by refrence vs Value)
     x = 10
     print("Within function = " , x)
    
x = 5                                         # (ye integer badal nahi sakta)    
print("Original = " , x)

modify_value(x)
print("After function = " , x) 

def modify_list(lst) :   
    lst.append(3)
    print("Within  Functin List= " , lst)
    
lst = [1, 2 , 5 , 6]                         # (ye list badal sakti hai)
print("Original List = " , lst)

modify_list(lst)
print("After Function List = " , lst)

def greetings(name) :                        # (function arguements)
    "Most popular languages are here"
    print("Popular language   =  {}".format(name))
    return

greetings("AI")
greetings("Python")
greetings("IT")

def printinfo(name , age) :                  # (Keyword Arguments)
    "This print a passed info into this function"
    print("Name = " , name)
    print("Age = " , age)
    return ;

printinfo(age = 25 , name = "Bint e Zain")

def printinfo(name , age = 25) :              # (default Arguments)
    "This print a passed info into this function"
    print("Now Name = " , name)
    print("Now Age = " , age)
    return ;

printinfo(age = 20 , name = "Bint e Zain")
printinfo(name = "Bint e Zain")

def posfun(x , y , / , z) :                   # (Positional-only arguments)
    print(x + y + z)
    
print("Evaluating positional-only arguments = ")
posfun(2 , 3 , z = 5)

total = 2                                    # (Scope of variables)

def sum(num1 , num2) :
    total = num1 + num2 ;                   
    print("Inside the function called local = "  , total) # (jo sirf function ke andar define wo local)
    return total ;
    
sum(3 , 3) ;
print("Outside the function called global = " , total)  # (jo function ke bahir bhi chale or change bhi ho wo global)  

def infinite_sequence() :                   # (Generator Function)
    num = 2
    while True :
       yield num
       num += 1
       
       
gen = infinite_sequence()       

for _ in range(6) :
    print(next(gen))
    
# << practiced by Bint e Zain >>    