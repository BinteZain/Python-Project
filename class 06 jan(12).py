 # Range :

for num in range(1,6) :
      print(num)                              # (starting point with condition)

print("Table of 2")

for num in range(1,11):
      print("2*" , num , "=" , 2*num)         #(with increment)

print("part 1 complete")     

# # While Loop :

# num = 1

# while num <= 10 :
#       print(num , "Welcome to AI")                            # (syntax 1)

# num = 1

# while num <= 10 :
#       print("count {num}")      
#       num = num + 1

# print("part 2 complete")      

# Variable Tuple :

t = (10 , 20 , 30 , 40 , 50 )

a =t[3]
print(a)

t = (1,2,3,4,5)

l=len(t)
for a in range(l):
      print(t[a])

t = (1,2,3,4,5)                         

a = min(t)                               # (minimum value)
print("minimum" , a)

a = max(t)                               # (maximum vlue)
print("maximum" , a)

a = t.count(2)                           # (how many times "2" here)
print("count" , a)                       

a = t.index(5)                           # (5 ka index no kya hai)
print("5 of index no is:" , a)

a = sum(t)                               # (sare no jama ho jayen)
print("sum" , a)

a = sum(t , 10)
print("sum" , a)

print(" part 3 complete")

# <<practiced by Bint e Zain>>