cp = int(input("enter cost price: "))
sp = int(input("enter selling price: "))


def bonus_calc(percentage_bonus, cost_price):
    bonus =((percentage_bonus/100) * cost_price)
    return bonus

if cp < sp:
    print("you are in profit!!!")
    profit_amount = sp-cp
    bonus =bonus_calc(5,cp)
    total_amount = profit_amount + bonus
    print("profit amount is: ", total_amount)

else:
    print("you are in loss!!!") 
    loss_amount = cp - sp
    bonus = bonus_calc(20,cp)
    total_amount = loss_amount + bonus
    print("loss amount is: ", total_amount)




    