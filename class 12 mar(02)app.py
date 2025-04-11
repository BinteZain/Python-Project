# Recursive Functions  /  Recursion :

def count_down(num : int) -> int :
    if num == 0 :
        print("Count down done")

    else :
        print("num >> " , num)
        count_down(num - 1)    

count_down(10)        

print("part 1 complete")

#  Lambda Functions :

add = lambda a , b : a + b                          # (lambda parameters  : expressions / statement :)

result = add(5 , 6)
print("add = " , result)

mul = lambda x : x * 2

print("multiply = " , mul(10))

cube = lambda x : x * x * x

print("cube = " , cube(4))

print("part 2 complete")

# Map :

numbers = [1 , 2 , 3 , 4 , 5]

def square(num : int) :
    return num * num

new_list = list(map(square , numbers))
               
print("numbers" , numbers)               
print("new_list" , new_list)                

print("part 3 complete")

import os 

print("cwd" , os.getcwd())                                # (current working directory)
print("list dir" , os.listdir)                            # (list directory)
#print("new folder" , os.mkdir("test"))                   # (make directory)
#print("rename" , os.rename("test new" , "test new2"))    # (rename directory)
os.rmdir("test new2")                                     # (remove directory)

file = open("text.txt")
print(file.read())
file.close()

file = open("text2.txt" , "w")
file.write("Hi , how are you ")
file.close()

file = open("text2.txt" , "a")
file.write("\ni am fine")
file.close()

with open("text2.txt" , "a") as file :
    file.write("kesa laga mera mazaq?")

print("part 4 complete")

# << practiced by Bint e Zain >>