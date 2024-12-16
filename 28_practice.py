#WAP to find highest number   

numbers = "01234127556789"
highest_num = 0
for n in numbers:
    if int(n)> highest_num:  #int(n) = chnaging string into integer
        highest_num = int(n)

print(f"highest number is {n}")        



#wap to find lowest number
numbers = "1234127556789"
lowest_num = 1
for n in numbers:
    if int(n)< lowest_num:  #int(n) = chnaging string into integer
        lowest_num = int(n)

print(f"lowest number is {n}")  