marks = int(input("enter your marks   "))

if isinstance(marks,str) and  not marks.isdigit():
    print("Invalid")

elif marks>40 and marks< 50 :
    print("Pass")

elif marks>50 and marks<60 :
    print("Second Division")

elif marks>60 and marks< 75:
    print("First Division")

elif marks >75 and marks<= 100:
    print("Distinction")               

else :
    print("Fail")

