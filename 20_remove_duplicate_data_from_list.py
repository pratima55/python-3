#WAP to remove duplicate item from list ["apple, "ball", "cat","ball","5","7","5"]

first_list=["apple", "ball", "cat","ball","5","7","5"]
second_list =[]

for item in first_list:
    if item  not in second_list:
        #continue #skip

        second_list.append(item)    
        
print(second_list)


#WAP to take user input "first name","mobile number", address, and add it to list
first_name =input("enter your first name: ")
mobile_number = int(input("enter your mobile number: "))
address = input("enter your address: ")
user_list =[]
user_list.append(first_name)
user_list.append(mobile_number)
user_list.append(address)
print(user_list)






