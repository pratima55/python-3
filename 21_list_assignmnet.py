#WAP to take 5 friends data and store it in total_list
# ["ram", 3652,"ktm"]
# ["shyam",1235,"pokh"]
#["hari",5284,"brt"]


print("fill info of first person ")
first_person =[ {input("enter your name: "),int(input("enter your phone number: ")),input("enter your address: ")}]

print("fill info of second person ")
second_person= [ {input("enter your name: "),int(input("enter your phone number: ")),input("enter your address: ")}]

print("fill info of third person ")
third_person= [ {input("enter your name: "),int(input("enter your phone number: ")),input("enter your address: ")}]
total_list= []
total_list.append(first_person)
total_list.append(second_person)
total_list.append(third_person)
print(total_list)