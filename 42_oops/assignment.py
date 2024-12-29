# with open ("store.txt", "w") as file_obj:
#     file_obj.write("1,dell vostro,95000,core i5")

# with open("store.txt","r") as file_obj:
#     data = file_obj.read()
#     print(data) 
       
# with open("store.txt","r") as file_obj:
#     data = file_obj.readlines()
#     print(data)    


class Notes:
    def append_notes(self):
        id  = input("Enter computer id : ")
        name  = input("Enter computer name : ")
        price = input("Enter price: ")
        core = input ("Enter core: ")
        full_detail = (f"id: {id}, name: {name}, price: {price}, core: {core}")
        with open("store.txt","a") as file_obj:
            file_obj.write("\n"+ full_detail)


    def display_notes(self):
        print(" All data on the file :/n")
        with open("store.txt","r")  as file_obj:
            data = file_obj.read()
            print(data)     

    def  search(self):
        search_item = input("what to search? ")
        print(f"searching  ID :{search_item}.......") 
        with open("store.txt","r") as file_obj:
            all_data=  file_obj.readlines()
        #print(all_data)   

        found = False
        for item in all_data:
            splitted_item = item.strip().split(",")
            if search_item.lower() in splitted_item[0]:
                print("***********search founds! ", item)
                found = True
        if not  found :
            print("No matches found")  



    def delete(self):
        delete_item = input("Enter  the ID of the computer to delete ")
        with open ("store.txt","r") as file_obj:
            data=file_obj.readlines()
            
        updated_data=[]
        found= False
        for item in data:
            splitted_item = item.strip().split(",")
            if delete_item.strip().lower() in splitted_item[0]:
                print(f"The computer ID {delete_item} has been deleted!!! ",item)
                found = True
            else :
                updated_data.append(item)

        if not found :
            print("no matches found")
        
        with open("store.txt","w") as file_obj:
            file_obj.writelines(updated_data)


notes_obj = Notes()
while True:
    print("""
        1: Append notes
        2: Display notes 
        3: search
        4: Delete 
        5: Exit    
        """)
    
    menu_input = input("Enter menu:  ")
    if menu_input == "1":
        notes_obj.append_notes()
    elif menu_input == "2":
        notes_obj.display_notes()  
    elif menu_input == "3"   :
        notes_obj.search()  
    elif menu_input == "4":
        notes_obj.delete() 
    elif menu_input == "5":
        exit()    
