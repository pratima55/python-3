#WAP for calculator
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# operator = input("enter operator")

# if operator == "+":
#     sum = a+b
#     print("addiction of a and b is  ",sum)
# elif operator == "-":
#     sub = a-b 
#     print("subtraction of a and b is", sub)
# elif operator == "*":
#     mul = a*b
#     print("multiplication of a and b is", mul)
# elif operator == "/":
#     div = a/b 
#     print("division of a and b is ",div)
# elif operator == "%":
#     mod = a%b 
#     print("modulus of a and b is", mod)      

######  USING FUNCTION

a = int(input("enter first number: "))
b = int(input("enter second number: "))
operator = input("enter operator")

def sum():
    sum = a+b
    print("addiction of a and b is  ",sum)

def subtract():
    sub = a-b 
    print("subtraction of a and b is", sub) 

def multiplication():
    mul = a*b
    print("multiplication of a and b is", mul)

def division()    :
    div = a/b 
    print("division of a and b is ",div)

def  modulus():
    mod = a%b 
    print("modulus of a and b is", mod)   

if operator == "+":
    sum()
elif operator == "-":
    subtract()  
elif operator == "*":
    multiplication()
elif operator == "/":
    division()              
elif operator == "%":
    modulus()    