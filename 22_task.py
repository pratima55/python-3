a = 5
b = 9
print("before swap value of a is: ",a)
print("before swap value of b is: ",b)

# c = a #5
# a=b   # a=9
# b=c   #b=5

a,b = b,a #without  using temporary

print("after swap value of a is: ",a)
print("after swap value of a is: ",b)




#wap to square the number in the list
data = [2,5,6,7,3] #[4,25,36,49,9]
square_data=[]
for item in data:
    
    sq = item * item
    square_data.append(sq)
    
print(square_data)    

   