# types of condition
# 1.if
# 2.if...else
# 3.if....elif...elif..else(nested condition)


# age = 13
# if age>18:
#     print("yoou can vote")

#syntax:
# if condition true:
#    statements 


# age = 25
# if age>20:
#     print("you can marry")

# else:
#     print("you can't marry")    

# WAP to get output as(child, adult,..old)
age = int(input("enter your age? "))
# age = int(age)

if isinstance(age,str) and not age.isdigit():   #if age.isdigit()== False:
    print("invalid age")

elif age<11:
    print("you are child")

elif age>11 and age<20:
    print("you are teenager")

elif age>20 and age<60:
    print("you are adult")
  

else:
    print("you are old")      


# #######
