#WAP to take 5 friends data and store it in total_list
# ["ram", 3652,"ktm"]
# ["shyam",1235,"pokh"]
#["hari",5284,"brt"]


# print("fill info of first person ")
# first_person =[ input("enter your name: "),int(input("enter your phone number: ")),input("enter your address: ")]

# print("fill info of second person ")
# second_person= [ input("enter your name: "),int(input("enter your phone number: ")),input("enter your address: ")]

# print("fill info of third person ")
# third_person= [ input("enter your name: "),int(input("enter your phone number: ")),input("enter your address: ")]
# total_list= []
# total_list.append(first_person)
# total_list.append(second_person)
# total_list.append(third_person)
# print(total_list)




#########USING LOOP#########
# total_list=[]
# for i in range(1,6):
#     print("Enter details of person",i)
#     person=[ {input("enter your name: "),int(input("enter your phone number: ")),input("enter your address: ")}]
#     total_list.append(person)
    
# print(total_list)    

##########
total_list=[]
for i in range(1,6):
    name = input("enter user name:  ")
    mobile_number= input("enter your number:  ")
    location = input("enter your location:  ")

    user_data =[]
    user_data.append(name)
    user_data.append(mobile_number)
    user_data.append(location)

    total_list.append(user_data)

print(total_list)    