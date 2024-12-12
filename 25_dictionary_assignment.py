#WAP which takes user data as input and store students detail in dictionary
x = int(input("enter the number of student's detail you want to add:  "))
student =[]
for i in range(1,x):
    print("Detail of student", i)
    data= {
        "name": input("enter name: "),
        "id": input ("enter your id: "),
        "computer_mark": int(input("enter computer mark: ")),
        "english_mark": int(input("enter english mark: ")),
        "math_mark": int(input("enter math mark: "))

    }
    student.append(data)
print(student)
