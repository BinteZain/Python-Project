# Control Flow  and Desicion Making in Python :

num : int = 10                           # (The if statement)

if num > 5 :
    print("10 number is greater than 5")

num : int = -5                          # (The else Statement)

if num > 5 :
    print("5 number is greater than -5")
    
else :
    print("-5 is lesser than 5")
    
num : int = 0                          # (elif check multiple conditions)
    
if num > 0 :
    print("zero is bigger")
    
elif num < 0 :
    print("zero is smaller")
    
else :
    print("zero is equals to zero")
    
operation : str = input("Enter the operation(+ , - , * , /) : ") # (Simple calulator)   

num1 : float = float(input("Enter the first number :"))
num2 : float = float(input("Enter the second number :"))

if operation == '+' :
    result = num1  +  num2
    
elif operation == '-' :
    result = num1 - num2
    
elif operation == '*' :
    result = num1 * num2
    
elif operation == '/' :
    result = num1 / num2
    
    if num2 != 0 :
        result = num1 / num2                 
        
    else :
        result = "Error : Division by zero"
        
else :
    result = "Invalid Operation"            
    
print("Result = " , result)    

fruits = ["apple" , "banana" , "cherry"]           # (The For Loop)

for fruit in fruits :                              # (Iterate over a list)
    print("Healthy Fruits" , fruit) 
    
word : str = "Practice"                           # (Iterate over a string)

for letter in word :
    print("Letters" , letter)
    
numbers = [1 , 2 , 3 , 4 , 5]                    # (for loop with else (no break)) 

for num in numbers :
    print("Number" , num)
    
else :
    print("Loop completed successfully !")      
    
numbers = [2 , 4 , 6 , 8]                       # (for loop with break (Skipping else))    

for num in numbers :
    print(num)
    
    if num == 6 :
        print("Loop is breaked !")
        break
    
else :
    print("Loop is completed !")
    
for i in range(8) :                             # (Controlling Loops) (continue example)
    
    if i == 6 :                                 # (6 ke ilawa sab print ho jaye) 
         continue
    print(i)

# << practiced by Bint e Zain >>