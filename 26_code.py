welcome_message = """
       WELCOME TO MY STUDENT MANAGEMENT SOFTWARE 
       PRESS NUMBER?
       1) Add new student
       2) Read all students
       3) Search student
       4) Delete student
"""
print(welcome_message)
user_input = int(input("Enter option:   "))
data = [
    {"name": "ram", "number": 9800988, "location": "brt"},
    {"name": "shyam", "number": 5235888, "location": "ktm"},
    {"name": "hari", "number": 4523688, "location": "pokhara"}
]
print(type(data))

if user_input == 1:
    print("Do you want to add data? Press (y/n)")
    statement = input()
    while statement == "y":
        new_data = {
            "name": input("Enter name: "),
            "number": int(input("Enter number: ")),
            "location": input("Enter location: ")
        }
        data.append(new_data)
        print("Do you want to add more data? Press (y/n)")
        statement = input()

elif user_input == 2:
    print("All students data:")
    for student in data:
        print(student)

elif user_input == 3:
    search_student = input("Whose information do you want to search? ")
    found = False
    for student in data:
        if student["name"].lower() == search_student.lower():  # Case insensitive search
            print(f"Student found: {student}")
            found = True
            break
    if not found:
        print("Student not found.")

elif user_input == 4:
    delete_data = input("Enter the name of the student you want to delete from the software: ")
    found = False
    for student in data:
        if student["name"].lower() == delete_data.lower():  # Case insensitive check
            data.remove(student)
            print(f"Student {delete_data} has been deleted.")
            found = True
            break
    if not found:
        print(f"Student {delete_data} not found.")

else:
    print("Invalid option.")

print("Updated student data:")
for student in data:
    print(student)
