# String Methods :

name = "pakistan"
 
print(type(name))
print(name.capitalize())
print(name.count("a"))
print(len(name))
print(name.index("t"))
print(name.replace("pakistan" ,"karachi".upper()))

print("part 1 complete")

# List Methods :

my_food = ["chips" , "gol gappe" , "biryani" , "paani"]
print(my_food)

my_food.append("chai")
print("Now my food is complete" , my_food)

my_food.insert(1 , "ketchup")
print(my_food)

my_food.pop()
print(my_food)

my_food.reverse()
print("Thats a right way to feed up" , my_food)

my_food.remove("gol gappe")
print(my_food)

my_food.sort(reverse=False)
print(my_food)

new_variety = ["pulao" , "daal" , "khichdi"]
print("This is special for me" , my_food)
print("This is normal food" , new_variety)

my_food.extend("new_variety")
print("Now board and abdomen is full" , my_food , new_variety)

print("part 2 complete")

# Dictionary Methods :

my_dict = {
    "Name"    :     "Miss Zain",
    "Class"   :     "Python",
    "Fees"    :     550000
}

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get("Name"))

new_dict  = {  "City"    :     "Karachi"  }
new_dict2 = { "Country" :     "Pakistan"   }

my_dict.update(new_dict)
my_dict.update(new_dict2)

print(my_dict)

print(my_dict.pop("City"))
print(my_dict)

my_dict.clear()
print(my_dict)

print("part 3 complete")

# << practiced by Bint e Zain>>