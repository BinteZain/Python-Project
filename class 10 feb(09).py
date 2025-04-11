# # Global Variable :

x = "global"

def hello() :                     # (global variable function , class ke andar or bahir bhi chalega)
    print("x inside function : " , x)

hello()    
print("x outside function : " , x)

# Local Variable :

def hello() :                     # (local variable hamesha function , class ke andar hi define hoga)
    y = "y inside function"
    print(y)

hello()    
print("good practice")
#print(y)                        # (function ke bahir dene se error ayega)

# Global and Local Variable both together :

x = 5

def hello() :
    x = 10
    print("This is local x.." , x)

hello()    
print("This is global x.." , x)

# Global Variable and Local Variable with same name :

x = 50

def hello() :
    global a
    a = "this is global variable"
    x = 100
    print("a.." , a)
    print("local x.." , x)

hello()
print("global x.." , x)
print("a.." , a)

print("part 1 complete")

# DocString / Documentation String :

def square(n) :
    """Takes in a number n , returns the square of n """

    print(n**2)
square(3)

print(square.__doc__)

def add_numbers(a , b) :
    """Takes two parameters and returns sum"""

    return(a + b)
print(add_numbers(10 , 5))
print(add_numbers.__doc__)

print("part 2 complete")

# Set :

s = {10 , 20 , 30 , 40}

print(s), 

for a in s :                                # (iterating through a set)
    print(a)

# Sets Methods :

l = [5 , 10 , 15 , 20]                      # (set)
s = set(l)

print("list convert in set =" , s)
 
s = {10 , 20 , 30 , 40 , 50}               # (remove)
s.remove(50)

print("remove no 50 =" , s)

s = {1 , 2 , 3 , 4 , 5}                    # (discard)
s.discard(5)

print("discard no 5 =" , s)

s = {1 , 2 , 3 , 4 , 5}                    # (discard with mistake and without error)
s.discard(8)

print("no 8 not found = " , s)

s = {9 , 19 , 29 , 39 ,49}                 # (randomly delete)
s.pop()

print(s)

s ={1 , 2 , 3 , 4 , 5}                     # (clear)
s.clear()

print(s)

l = [1 , 2 , 3]                            # (update)
s = {3 , 4 , 5}
s.update(l)

print("updated elements =" , s)

set1 = {1 , 2 , 3, 4}                      # (union)
set2 = {4 , 5 , 6 , 7}

print("union value =" , set1 | set2)

set1 = {1 , 2 , 3, 4}                      # (intersection)
set2 = {4 , 5 , 6 , 7}

print("intersection value =" , set1 & set2)

set2.copy()                                # (copy)
 
print("copy =" , set2)

print("part 3 complete")

# << practiced by Bint e Zain >>