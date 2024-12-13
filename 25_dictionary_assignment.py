#WAP which takes user data as input and store students detail in dictionary
# x = int(input("enter the number of student's detail you want to add:  "))
# student =[]
# for i in range(1,x):
#     print("Detail of student", i)
#     data= {
#         "name": input("enter name: "),
#         "id": input ("enter your id: "),
#         "computer_mark": int(input("enter computer mark: ")),
#         "english_mark": int(input("enter english mark: ")),
#         "math_mark": int(input("enter math mark: "))

#     }
#     student.append(data)
# print(student)


##########################################################################################

welcome_message= """
       WELCOME TO MY STUDENT MANAGEMENT SOFTWARE 
       PRESS NUMBER?
       1) Add new student
       2) read all student
       3) search student
       4) delete student
"""
print(welcome_message)
user_input = int(input("Enter option:   "))
data = [
    {"name": " ram", "number": 9800988, "location": "brt"},
    {"name": "shyam", "number": 5235888, "location": "ktm"},
    {"name": "hari", "number": 4523688, "location": "pokhara"}

]
#print(type(data))
# statement = "y"

if user_input == 1:
    print("Do you want to add data? Press (y/n)")
    statement =input()
    while statement == "y":
        new_data ={
        "name" : input("enter name: "),
        "number" : int(input("enter number: ")),
        "location" : input("enter location: ")
        }
        print("Do you want to add data ? Press (y/n)")
        statement = input()
        if statement == "n":
            pass
    data.append(new_data)  
 

elif user_input==2:
    print("All students in data:")
    print(data)

elif user_input == 3:
    search_student = input("Enter name whose information do you want to search?  ").strip().lower() #strip() remove whitespace
    found = False
    for student in data:
        if student["name"].strip().lower() == search_student :
            print("Student found: ", student)
            found = True
            break

        if not found :
            print("student not found")




elif user_input == 4:
    delete_data = input("Enter the name of the student you want to delete from the software: ").strip().lower()
    found = False
    for student in data:
        if student["name"].strip().lower() == delete_data.lower():  
            
            found = True
            if found:
                data.remove(student)
                print(f"Student {delete_data} has been deleted.")
                print(data)
            break
    if not found:
        print(f"Student {delete_data} not found.")


else:
    print("Invalid option")            



