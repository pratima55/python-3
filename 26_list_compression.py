data = [2,5,7,9]
square_list =[]
square_list = [number* number  for number in data]
print(square_list)

 
# by list compression 
data = [1,2,3,4,5,6]
add_list = [ 100+ number for number in data]
print(add_list)  #output [101, 102, 103, 104, 105, 106]


#oldway
data = [1,2,3,4,5,6]
add_list =[]
for item in data:
    item = item+ 100
    add_list.append(item)
print(add_list)    #output [101, 102, 103, 104, 105, 106]


#wap to check even number using list compression
data = [1,2,3,4,5,6]
check_even = [  item   for item in data if item%2==0]
print(check_even)