#WAP to make a system for computer shop to store computers data like, computer name,brand,price,id,generation,core


def menu():
    print(""" 

        Press 1 for store item
        press 2 for search item
        press 3 for read items
    
    """)


class ComputerShop:
    def __init__(self,file_path):
        self.file_path = file_path

    def store_computer(self,c_id,name,brand,price,generation,core):
        with open(self.file_path,"a") as file_obj:
            file_obj.write(f"\n ID :  {c_id}, Name : {name}, Brand :{brand}, Price: {price} , Generation:  {generation},Core: {core}")

    def search_computer(self):
        what_to_search = input("Enter pc name or ID : ")
        with open(self.file_path, "r") as file_obj:
            data = file_obj.readlines()


        for item in data :
            if what_to_search in item:
                print("search found", item)
                
            else:
                print("search not found")

    def delete_computer(self):
        pass
    def read_computer(self):
        with open(self.file_path,"r") as file_obj:
            data = file_obj.readlines()
        print(data)




while True:
    menu()
    input_menu = input("#>>>")
    computer_shop_obj = ComputerShop("42_oops/store_room.txt")


    if input_menu == "1":
        c_id = input("Enter computer ID: ")
        name = input("Enter computer Name: ")
        brand= input("Enter computer brand: ")
        price = input("Enter computer price: ")
        generation = input("Enter generation: ")
        core = input("Enter number of cores: ")

        computer_shop_obj.store_computer(c_id,name,brand,price,generation,core)
    
    elif input_menu == "2":
        computer_shop_obj.search_computer()
    
    elif input_menu == "3":
        computer_shop_obj.delete_computer()
    
    elif input_menu == "4":
        computer_shop_obj.read_computer()

    else:
        print("Invalid input.")    


