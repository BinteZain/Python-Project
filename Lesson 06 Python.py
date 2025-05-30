# Lists , Tuples and Dictionary :

needed_products = ["comb" , "nail cutter" , "clips"]        # (list are  mutable matlab ke change ho sakti hai)
print(needed_products)

needed_products[-2] = "lipstick"                           # (modifying yani kisi element ko change karna hai)
print(needed_products)

print(needed_products[0:2])                                # (List Slicing)

numbers : list[int] = [8 , 4 , 9 , 1 , 2 , 3 , 7 , 5]      # (Sorted List yani list ko tarteebwar banayen (ascending order))
numbers.sort()

print(numbers)

grammer = ["you" , "me" , "i" , "they" , "my" , "we"]      # (Sorting by string length)
grammer.sort(key=len) 

print(grammer)

grammer.sort(key=lambda word : word[-1])                  # (Sorted by last character)
print(grammer)

squared : list = [x ** 2 for x in [1 , 2 , 3 , 4 , 5]]    # (List Comprehension)

print("Squared =" , squared)

squared : list = [x ** 2 for x in [1 , 2 , 3 , 4 , 5] if x > 20 or x > 4]    # (List Comprehension with if condition)

print("Squared =" , squared)

person : dict = {                                         # (Dictionary)
       "name"     :      "Boy" ,         
       "age"      :       20 ,    
       "hobby"    :      "more and more knowledge"      
}

print(person)

name : int = input("Enter your name = " )                # (Type Hint Language) 

print(name , type(name))

# << practiced by Bint e Zain >>