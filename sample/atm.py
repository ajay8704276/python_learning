total_amount = 500

pin = int(input("please enter the pin  :  "))
if pin == 12345:
    print("welcome to atm")
    print("enter 1 : banalce enquiry")
    print("enter 2 : amount withdrawl")
    num = int(input())
    if num == 1:
        print("Your balance amount is :" ,total_amount)
        exit(1)
    elif num == 2:
        amount_to_withdraw = int(input("enter amount to withdraw : "))
        if amount_to_withdraw > 500 :
            print("please enter valid amount to withdraw")
            exit(1)
        else:
            balance_amount = total_amount - amount_to_withdraw
            print("please wait for amount you request to withdraw : ",amount_to_withdraw)
            print("thanks ! your request is successful ")
            exit(1)
    else:
        print("please enter valid input!!")
        exit(1)
else:
    print("Please enter valid pin!!")
    exit(1)