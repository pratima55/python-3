mod = ["w","r","w+","r+","a","wb","rb"]

# with open("file_name.extension",mod) as file_obj:

# with open ("readme.txt","w") as file_obj:
#     pass

# with open("readme.txt","r") as file_obj :
#     # file_obj.write("hello world")
#     data=file_obj.readlines()
#     print(data)

# with open("readme.txt","w") as file_obj:
#     file_obj.write("helloooo")    

# with open("readme.txt", "w+") as file_obj:
#     a= file_obj.write("helllllloooo")
#     print(a)

# with open("readme.txt","r") as file_obj:
#     data = file_obj.read()
#     print(data)

# with open("readme.txt","a") as file_obj:
#     file_obj.write("\nbe happy")
    

# with open("readme.txt", "r+") as file_obj:
#     data = file_obj.readlines()
#     print(data)    #output: ['helllllloooo\n', 'good evening\n', 'friendbe happy\n', 'be happy\n', 'be happy']


#**********************************************************************************************************************************************


#WAP to make a system for computer shop to store computers datalike, computer name, brand, price, id, generation, core


# with open ("42_oops/computershop.txt","w") as file_obj:
#     pass



brand = input("enter brand name : ")
price = (input ("enter price of device: "))
id = input("Id of device: ")
generation = input("enter generation of device:  ")

class Computershop():
     def create():
      with open("42_oops/computershop.txt","w") as file_obj:
        file_obj.write(brand)
        file_obj.write("\n")
        file_obj.write(price)
        file_obj.write("\n")
        file_obj.write(id)
        file_obj.write("\n")
        file_obj.write(generation)
        file_obj.write("\n")
        file_obj.write("\n")
        file_obj.write("\n")

def append():
        with open("42_oops/computershop.txt","a+") as file_obj:
            file_obj.write(brand)
            file_obj.write("\n")
            file_obj.write(price)
            file_obj.write("\n")
            file_obj.write(id)
            file_obj.write("\n")
            file_obj.write(generation)
            file_obj.write("\n")
            file_obj.write("\n")
            file_obj.write("\n")

object = Computershop()

while True:
    option = input("user input: ")
    if option == "1":
          object.create()
    elif option == "2":
         object.append()

        
        

      


        








