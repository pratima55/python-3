#Find odd and even numbers up to 100

# num = 1
# while num <= 100:
#     if num % 2 ==0:
#          #print(f"{num}  is even")
#          print(num , "is even number")
#     else:
#         print(f"{num}  is odd")

#     num +=1  



#Find the higest number from the string
# numbers = "01234392566"
# highest = 0
# for i in numbers:
#     if int(i)> highest:
#         highest=int(i)
# print(f"highest number is {highest}")



#Remove and pop elements from a list
# my_list = [1,9,3,4,5]
# my_list.remove(6) #the remove method will raise a value error since 6 is not in the list.
# print(my_list)
# popped_item = my_list.pop(3)
# print(popped_item)


#Set creation and adding items
# my_set = {1,2,3}
# my_set.update([4,5])
# print(my_set)



#WAP that asks the user to input a number and then prints whether the number is even or odd

# while True:
#     num = int (input("enter number: "))
#     if num %2 ==0:
#         print(f"{num} is even")

#     else:
#         print(f"{num} is odd") 



#     command = input("do you want to continue? (y/n):") 
#     if command.lower() != "y":
#         break
  


#WAP that finds the highest and lowest digit in a given string of numbers.

# numbers = "01234392566"
# highest = 0
# lowest = 0

# for num in numbers:
#     if int(num) > highest:
#         highest = int(num)
# print(f"heighest number {highest}")

  

# for num in numbers:
#     if int(num) < lowest:
#         lowest = int(num) 
# print(f"lowest number {lowest}")      





#WAP that takes a sentence as input and counts the number of words in it.

# words = "Python is fun"
# length = len(words.split()) #The split() method splits a string into a list.
# print(f"Number of words ={length}") #output: Number of words =3




#WAP that takes a positive u=integer as input and calculates the sum of its difits.
#Example input: 1234
#example output : sum of digits = 10

