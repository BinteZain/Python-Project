# OOP urf Object Oriented Programming :

class DemoClass :                               # (example of class)
    
    a = 10
    b = 20
    
demoobject = DemoClass()    
print(demoobject.a , demoobject.b)

                                              
class DemoClass :                               # (example : class with methods)
    
    a = 10
    b = 20
    
    def sumvalue(self) :
        print(2 + 2)
    
demoobject = DemoClass()    
print(demoobject.a , demoobject.b)
demoobject.sumvalue() ;

# Inheritace (pillar 1) :

class A :                                       # (Singal inheritance) (1 object se dono class ko call kar sakte hain)
    def displayA(self) :
        print("I am Bint e Zain.")
        
class B(A) :
    def displayB(self) :
        print("Its singal inheritance")       
        
obj = B()
obj.displayA()
obj.displayB() 

class A :                                       # (multilevel inheritance) (a ko b mein or b ko c mein use kar sakte hain)
    def displayA(self) :
        print("I am Bint e Zain.")
        
class B(A) :
    def displayB(self) :
        print("I am a lady.")    
        
class C(B) :
    def displayC(self) :
        print("Its multilevel inheritance")         
        
obj = C()
obj.displayA()
obj.displayB() 
obj.displayC()

class A :                                       # (multiple inheritance) (a or b ko 1 sath c mein use kar sakte hain )
    def displayA(self) :
        print("I am a student.")
        
class B :
    def displayB(self) :
        print("Youthful and modern generation.")    
        
class C(A , B) :
    def displayC(self) :
        print("Its multiple inheritance")         
        
obj = C()
obj.displayA()
obj.displayB() 
obj.displayC()

# Encapsulation (pillar 2) :

class Student :
    def __init__(self) :
        self.__name = ""
        
    def getname(self) :    
        return self.__name
    
    def setname(self , name) :
        self.__name = name
        
obj = Student()
obj.setname("Encapsulation with getter and setter methods.")
name = obj.getname()
print("Pillar = " , name)

# Polymorphism (pillar 3) :

class Ai :                                      
    def displayinfo(self , name = "") :
        print("Polymorphism with overloading " + name)
        
obj = Ai()
obj.displayinfo(" in oop.")
        
class Ai :                                      
    def displayinfo(self , name = "") :
        print("Polymorphism with overriding " + name)
        
class Python(Ai) :
    def displayinfo(self) :
        super().displayinfo()
        print("Inherited parent function in to child with super() keyword.")
    
          
obj = Python()
obj.displayinfo()        

class Area :                                     # (one more example of overloading)
    def find_area(self , a = None , b = None) :
        if a != None and b != None :
            print("Area of rectangle = " , (a * b))
            
        elif a != None :
            print("Area of rectangle = " , (a * a))
            
        else :
            print("Nothing to find.")           # (agar koi bhi parameter pass nahi karenge to ye jawab ayega )
            
obj = Area()
obj.find_area()
obj.find_area(10)
obj.find_area(5 , 3)                            # (function 1 hi hai lekin kam teen kar raha hai)        
    
# (method amd constructor)    
class DemoClass :                               # (method)
    a = 4
    def showvalue(self) :
        print("Real value = " , self.a)
        self.c = self.a * self.a
        print("After multiply = " , self.c)
        
    def showvalue1(self , a , b) :              # (method)
        print(a + b)     
        
obj = DemoClass()
obj.showvalue()        
obj.showvalue1(2 , 2)

class DemoClass :                               # (constructor jisko call nahi karna parta hai)
    def __init__(self) :
        print("By By Python , I will miss you so much.")

obj = DemoClass()

# << practiced by Bint e Zain >>