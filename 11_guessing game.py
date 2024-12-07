import random
secret_num = random.randint(1,100)

count = 1

while count<=5 :
    guess_num = int(input('enter number: '))
    
    if secret_num < guess_num:
        print("Guess number is too high")
        count = count+1

    elif secret_num> guess_num:
        print("too low")
        count = count + 1
        
    else:
        print("Your guess is correct in count",count)
        break

else:
    print('Attempt finished')                  



#######################################
#wap to check number is positive, negative or zero


num = int(input("enter number"))
if num <0:
    print("negative")
elif num >0:
    print("positive")
else :
    print("zero")        
