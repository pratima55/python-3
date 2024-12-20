
def is_prime(number):
    for i in range(2,number):
            if number % i ==0:
                return False

    return True
a=7
check_prime = is_prime(a)
if check_prime == True:
    print(f"{a} is prime number")

else:
    print(f"{a} is composite number")    


### WAP TO CHECK EVEN NUMBER

def is_even(number):
    if number % 2 == 0 :
        return True
    else:
        return False
    
check_num = is_even(100)
if check_num == True:
    print("number is even")

else:
    print("number is odd")      