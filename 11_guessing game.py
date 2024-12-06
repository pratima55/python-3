secret_num = 67
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