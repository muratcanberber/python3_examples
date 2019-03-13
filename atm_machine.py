import os
os.system("CLS")
main_menu = """
*********************************
*                               *
*      Welcome To MCB Bank      *
*                               *
*********************************
        Prosedures :

        1. Check Accounts

        2. Deposit Money

        3. Withdraw Money


        Type "q" to exit

"""

## Details
account = 1000

    

def main():
    os.system("CLS")
    print(main_menu)
    while True:
        prosedure = input("Select a prosedure\n")
        if prosedure.lower() =="q":
            print("Good Bye!")
            break
        elif prosedure == "1":
            check_accounts()
        elif prosedure == "2":
            deposit_money()
        elif prosedure == "3":
            withdraw_money()

def check_accounts():
    os.system("CLS")
    print("""

        Account Details
    
    """)
    print("Current Account: ${} \n".format(account))

    if input("Press m to Back to Main Menu\n") == "m":
        return main()

def deposit_money():
    os.system("CLS")
    print("""

        Deposit Money
    
    """)
    ammount = int( input("Enter desired money ammount to be deposit\n"))
    questions = input("Are you sure to deposit ${} to your account? y/n \n".format(ammount))
    if questions == "n":
        return main()
    elif questions == "y":  
        print("Your deposit has been complated")
        print("You are being navigate to Check Accounts...\n")
        global account
        account = account + ammount

        answer = input("Do you wish to go your accounts? y/n \n")
        if answer == "n":
            return main()
        else:
            return check_accounts()

def withdraw_money():
    os.system("CLS")
    print("""

        Withdraw Money
    
    """)
    global account
    print("Your current Acount is : ${} \n".format(account))
    cash = int( input("Enter desired ammount money to withdraw \n") )
    if account >= cash and cash >= 0:
        question = input("Are you sure to withdraw ${} ? \n Your balance will be ${} after this prosedure \n y/n \n".format(cash, account - cash))
        if question == "y":
            account -= cash
            answer = input("Do you wish to go your accounts? y/n \n")
            if answer == "n":
                return main()
            else:
                return check_accounts()
    else:
        print("Please enter a valid ammount to draw")
        question = input("Want to try again? y/n \n")
        if question == "y":
            return withdraw_money()
        else:
            return main()         
main()
