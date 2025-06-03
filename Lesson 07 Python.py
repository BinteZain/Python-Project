# The Set Data Type :

my_set : set = {10 , 12 , 15 , 20 , "a"}
my_set2 : set = set([10 , 12 , 15 , 20 , "a"])
unknown :set = {}
empty : set = set()
empty2 : set = ()

print("my_set  = " , my_set)
print("my_set2 = " , my_set2)
print("unknown : set type   = " , type(unknown))
print("empty : set type     = " , type(empty))
print("empty2 : set type    = " , type(empty2))

for item in {10 , 12 , 15 , 20 } :
    my_set.discard(item)
    
print("discard list = " , my_set)    

set1 = {2 , 4 , 6 , 8}                              # (Unique Elements)
print("set1 = " , set1)

set1.add("a")
print("add different value = " , set1)

set1.add(4)                                        # (ignored same values)
print("add same  value = " , set1)

# << practiced by Bint e Zain >>