# Comparison (Relational) Operators :

# Identity Operators  /  is vs == :

list1 = [1 , 2 , 3 , 4 , 5]
list2 = [1 , 2 , 3 , 4 , 5]

print("list =" , list1 is list2)             # (compares the identity of two objects / exact location of object in memory)
print("list =" , list1 == list2)             # (compares the value of the objects)

a = 3 
b = 3

print(a is b)                                # (both are true because computer does not waste memory)
print(a == b)

x = 4
y = "4"

print(x is y ,"," , x == y)

print("part 1 complete")

# List Comprehension :

def get_sqr_list(n : int) :
    for num in range(n) :
        print(num)

get_sqr_list(5)

list = [n for n in range(20) if n % 2 == 0]

print(list)

print("part 2 complete")

# Generators :

def get_generated_values() :
    for num in range(0 , 11) :
        yield num

result = get_generated_values()

print("result" , result.__next__())
print("result" , result.__next__())

def gen(n) :
    for i in range(n) :
        yield i

g = gen(3)

print(g.__next__())        
print(g.__next__())      
print(g.__next__())      

print("part 3 complete")

# << practiced by Bint e Zain >>