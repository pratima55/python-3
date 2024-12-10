# first_list = ["apple","ball","shyam",99,"9.0",4.3]
# # print(type(first_list))
# # print(first_list[3])  #outpur: 99
# # print(first_list)
# # first_list[0]="Apple"
# # print(first_list)
# # print(first_list[1:4]) #start:stop:step
# # print(first_list[::-1])

# # #add item in list(using append)
# # first_list.append("cat")
# print(first_list)


# # ######2nd method of creating list
# second_list = list((5,9,"cat","dog"))
# print(second_list)

# #Access list item using loop
# for item in first_list:
#     print(item, end=",")

#WAP to remove duplicate item from list ["apple, "ball", "cat","ball","5","7","5"]

list1=["apple", "ball", "cat","ball","5","7","5"]


        


#WAP to remove ball  from list ["apple, "ball", "cat","ball","5","7","5"]
word =["apple", "ball", "cat","ball","5","7","5"]  

for item in word:
    if item == "ball":
        continue
    print(item)

       
          
