def menu():
    print(""" 

        Press 1 for store item
        press 2 for search item
        press 3 for read items
    
    """)


class ComputerShop:
    def __init__(self,file_path):
        self.file_path = file_path

    def store_computer(self,c_id,name,brand,price,quantity):
        with open(self.file_path,"a") as file_obj:
            file_obj.write(f"\n{name},{brand},{price},{quantity}")

    def search_computer(self):
        pass
    def delete_computer(self):
        pass
    def read_computer(self):
        pass

while True:
    menu()
    input_menu = input("#>>>")
    computer_shop_obj = ComputerShop("42_oops/store_room.txt")
    if input_menu == "1":
        computer_shop_obj.store_computer(c_id=1,name="dell i5",brand="dell",price="4500",quantity="8")
    elif input_menu == "2":
        computer_shop_obj.search_computer()
    elif input_menu == "3":
        computer_shop_obj.delete_computer()
    elif input_menu == "4":
        computer_shop_obj.read_computer()


