# String Methods :

name = "pakistan"

print(name.capitalize())                                            # (a kitni bar hai)
print(name.count("a"))

new_name = "My name is Miss Zain and my nationality is Pakistan."    # ("is" konse index no per hai)
print(new_name.find("is"))
print(new_name.find("is" , 30 , 60))                                 # (starting and ending position)
print(new_name.find("good"))                                         # (agar ye word nahi hoga to -1 result hoga)

new_name = "My name is Miss Zain     and     My nationality is Pakistan."
name_count = len(new_name)
print(name_count)

new_name : str = "My name is Miss Zain and my nationality is Pakistan."
print(new_name.replace("Miss" , "Binte"))

print(new_name.index("name"))

print("part 1 complete")

# List Methods :

my_list = ["Ali" , "Asad" , "Saad"]                       # (akhir mien add karega)
my_list2 = [1 , 2 , 3]
print(my_list)
print(my_list2)

my_list.append("Zain")
my_list2.append(4)
print(my_list , my_list2)

my_list.append(my_list2)                                  # (pehli list ke andar hi dosri list ayegi)
print(my_list)

my_list.insert(3 , "Yasir")
print(my_list)

my_list.insert(-3 , "Sabir")
print(my_list)

my_list.reverse()
print(my_list)

num_list = [10 , 11 , 12 , 13]
num_list.reverse()
print(num_list)

my_list.pop()                                               # (last element hat jayega)
print(my_list)

for element in my_list :                                    # (line ba line likhega)
    print(element)

my_list = ["Ali" , "Asad" , "Saad"]
new_list = ["Sara" , "Farah" , "Nida"]          
my_list.extend(new_list)
print(my_list)

my_list.remove("Nida")
print(my_list)

num_list = [10 , 21 , 9 , 3]
print(num_list)

num_list.reverse()
print(f" reverse list{num_list}")
num_list.sort(reverse = False)
print(f"sort list{num_list}")

student = {
    "name"      :       "Hasnain",
    "age"       :       22,
    "course"    :       "agentic ai"
}

print(student.keys())

print(student.values())
print(student.items())

for item in student.items() :
    print(item)

# Destructuring : 

for key , value in student.items() : 
    print(f"key {key} and value {value}")

student.update({"age" : 23})
print(student)

student.clear()
print(student)

print("part 2 complete")

# Exception Handling / Error Handling / try except : 

num : int = 10 
num2 :int = 0

user_input = input("Enter your number..")

try:
    result = num / num2
    print(result)
except Exception as e :
    print(e)

print("Good Practice")
 
#Types : 

list = ["Ali" , "Anus"]
try :
    result = list[3]
    print(result)
except IndexError:
    print("list index out of range")                 # (index error)
except ZeroDivisionError :
    print("this is error for zero value")            # (ZerDivisionError)

a = int(input("Enter the number"))
print(a)

try : 
     result = a[str]                                 # (value error)
     print("this is string")

except Exception as e:
    print("its a number")         

dict = {                                            # (key error)
    "Course"   :    "Python",
    "fees"     :     50000
}

try : 
    result = dict[fee]
    print(result)
except Exception as e :
    print(e)

try :                                               # (import error)
    from time import DateTime
    print("file is here")
except ImportError as e :
    print(e)

print("part 3 complete")

# << practiced by Bint e Zain>>