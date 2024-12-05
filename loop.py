#loop types:
#1. while loop
#2. for loop

# while True:
#     print("hello NPL!!!") #output : infinite




# i = 0
# while i<=100:
#     print(i)
#     i= i+ 1
    

#WAP to find odd and even upto 50

# i = 1
# while  i <=50:
#     if i % 2==0:
#         print("even",i)
#     else:
#         print("odd ",i)    
#     i = i+1    


WAP to find prime number 
num = 12
start = 1
count = 0 
while start <= num:
    if num % start == 0:
        count = count + 1
    start = start + 1

if count<= 2:
    print(f"{num} is prime number")


else:
    print(f"{num} is composite number")            







    