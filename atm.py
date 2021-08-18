print("Welcome to mybank.hub Bank ATM")
restart = ("Y")
chances = 3
balance = 9999999.12

while chances >= 0:
    pin = int(input('Please Enter your 4 Digit Pin:'))
    if pin == (1234):
        print("Correct pin")
        print("press 1 for your balance ")
        print("press 2 to make a withdrawal ")
        print("press 3 to pay in ")
        print("press 4 to return card\n ")
        while restart not in ('n', 'NO', 'no', 'N'):
            print("Correct pin")
            print("press 1 for your balance ")
            print("press 2 to make a withdrawal ")
            print("press 3 to pay in ")
            print("press 4 to return card\n ")
            option = int(input("What would you like to choose ?"))
            if option == 1:
                print("you balance is ksh", balance)
                restart = input("Would ypu like to go back ?")
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(input(
                    "How much would you like to withdraw ? 10,20, 40, 80, 100 for other enter 1:"))
                if withdrawl in [10, 20, 40, 80, 100]:
                    balance = balance - withdrawl
                    print("\n your balance is now ksh", balance)
                    restart = input("Would ypu like to go back ?")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                    break
                elif withdrawl != [10, 20, 40, 80, 100]:
                    print("Invalid amount")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Enter Amount"))
            elif option ==3:
                pay_in = float(input("How much would you like to deposit"))
                balance = balance + pay_in
                print("\n your balance is now ksh", balance)
                restart = input("Would ypu like to go back ?")
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                break
            elif option == 4:
                print("Pleas wait whilst your card is returned...\n")
                print("Thank you for your services")
                break
            else:
                print("Please enter a correct number. \n")
                restart = ("y")
    elif pin != ('1234'):
        print("Incorrect Password")
        chances = chances -1
        if chances == 0:
            print("\nNo more tries")
            break

