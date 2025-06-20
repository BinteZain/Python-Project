# Exception Handling with try , except , else , finally :

try  :                                     # (the try block)
    result = 10 / 0
    
except :
    print("try example = 0 se divide nahi hota hai.")    
    
try :                                     # (the except block)
    result = 10 / 0
    
except ZeroDivisionError :
    print("except example = 0 se divide nahi hota hai.")
    
except Exception as e :
    print(f"except example = yahan koi ghalti hai.{e}") 
    
try :                                    # (the else block)       
    result = 10 / 2
    
except ZeroDivisionError :
    print("else example = 0 se divide nahi hota hai.")
    
else :
    print(f"else example = divide ho gaya hai. Result = {result}")        
    
try :                                    # (the finally block)
    result = 10 / 0
    
except ZeroDivisionError :
    print("finally example = 0 se divide nahi hota hai.")
    
finally :
    print("finally har haal mein print hoga.")
    
def divide_numbers(a , b) :              # (mix example of try , except , else , finally)       
    try :
        result = a / b
        
    except ZeroDivisionError :
        print("0 se divide nahi hota hai.")
        
    except TypeError :
        print("number ko number hi se divide karen.")        
        
    else :
        print(f"taqseem ho gaya = {result}")    
        
    finally :
        print("kam ho gaya.")
            
divide_numbers(10 , 5)
divide_numbers(10 , 0)
divide_numbers(10 , "2")

try :                                    
    num1 = float(input("Enter the first number = "))
    num2 = float(input("Enter the second number = "))
    result = num1 / num2
    
except ValueError :
    print("Error: Invalid input. Please enter numbers.")    
    
except ZeroDivisionError :
    print("Error: Cannot divide by zero.")   
    
else :
    print(f"The result is = {result}")    
    
finally :
    print("Thank you for using error handling program!")    
    
# << practiced by Bint e Zain >>