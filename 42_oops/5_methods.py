# class Student:
#     school = "Telusko"

#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avg (self):
#         return(self.m1 + self.m2 + self.m3)/3   

#     @classmethod
#     def getSchool(cls):
#         return cls.school 
#     @staticmethod

#     def info():
#         print("This is student class..in abc module")


# s1 = Student(25,35,36)
# s2= Student(25,58,96)

# print(s1.avg())
# print(s2.avg())
# print(Student.info())



#************************************************************

# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
        

#     def __str__(self):
#         return (f"{self.name} {self.age}") 


# p1 = Person("john", 36)     
# print(p1)
 


#************************************************************
#OBJECT METHODS
# class Person :
#     def __init__(self,name,age):
#         self.name = name
#         self.age= age

#     def myfunc(self) :
#         print("Hello my name is "+ self.name)

# p1 = Person("john", 36)   
# p1.myfunc()        


#************************************************************
#THE SELF PARAMETER
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
# class Person:
#     def __init__(mysillyobject, name,age):
#         mysillyobject.name = name
#         mysillyobject.age = age


#     def myfunc(abc):
#         print("Hello my name is" +  abc.name)

# p1 = Person("john",36)
# p1.myfunc()  


#************************************************************
#MODIFY OBJECT PARAMETER
# p1.age= 40

#DELETE OBJECT PROPERTIES
# del p1

        
#************************************************************
#CLASS CONSTRUCTOR
# class Chritmas:
#     welcome_text = "Every one is welcome on chritmas party"


#     def __init__(self,a,b):
#         print("this will automatically called when object is created")
#         self.a=a
#         self.b=b


#     def check_authorize_person(self):
        
#         print("he is authorized")  

# obj1 = Chritmas(4,9)
# obj2 = Chritmas(2,6)

# print(obj1.a, obj2.a)         


#************************************************************
class Cat:
    species = "Fenine"

    def __init__(self,name, sound,color, age ):
        self.name = name
        self.sound = sound
        self.color = color
        self.age = age
        pass

    def food_calculator(self, weight):
        if weight in range (200, 500):
            print("can give 50g of food")
        elif weight in range(501, 1000):
            print("can give 100g of food")
        elif weight in range(1100, 2000):
            print("can give 150g of food")
        elif weight in range(2000, 3000):
            print("can give 200g of food")
        else:
            print("3 days of water fasting")            



first_cat = Cat("pinky", "meow","white",2) 
second_cat = Cat ("lucy", "meuu", "grey", 3)
third_cat= Cat("juliy", "meeeoouuuu", "golden", 4)
print(first_cat.name)
print(second_cat.sound)
print(third_cat.color) 
print(first_cat.food_calculator(250))  #output:can give 50g of food