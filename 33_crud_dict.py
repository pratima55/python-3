welcome_message= """
       WELCOME TO MY STUDENT MANAGEMENT SOFTWARE 
       PRESS NUMBER?
       1) Add new student
       2) read all student
       3) search student
       4) delete student
"""
data = [
    {"name": " ram", "number": 9800988, "location": "brt"},
    {"name": "shyam", "number": 5235888, "location": "ktm"},
    {"name": "hari", "number": 4523688, "location": "pokhara"}

]


def add_student():
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


def search():
    search_student = input("Enter name whose information do you want to search?  ").strip().lower() #strip() remove whitespace
    found = False
    for student in data:
        if student["name"].strip().lower() == search_student :
            print("Student found: ", student)
            found = True
            break

        if not found :
            print("student not found")

def delete():
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

def display_all_student():
    print("All students in data:")
    print(data)


while True:
    print(welcome_message)
    user_input = input("enter option #: ")
    if user_input == "1":
        add_student()

    elif user_input == "2":
        display_all_student()

    elif user_input == "3":
        search()
        
    elif user_input == "4"   :
        delete() 