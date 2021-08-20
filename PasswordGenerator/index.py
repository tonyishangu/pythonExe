# from Password.interface import check_credendtials
# from Password.interface import passlocker
# from Password.interface import save_user
from passlock import User, Credentials

def create_new_user(username,password):
    new_user = User(username,password)
    return new_user

def save_user(user):
    user.save_user()

def display_user(self):
    return User.dispaly_user()

def login_user(username, password):

    check_users=Credentials.verify_user(username, password)
    return check_users

def create_new_credentials(account, userName, password):
    new_credentials=Credentials(account, userName, password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_details()

def display_account_details():
    return Credentials.display_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()

def find_credentials(account):
    return Credentials.find_credential(account)

def check_credentials(account):
    return Credentials.if_credential_exist(account)

def generate_password():
    auto_password = Credentials.generatePassword()
    return auto_password

def copy_password(account):
    return Credentials.copy_password(account)

def passwordlocker():
    print("Welcome to Passlocker..\n Select one of the following to proceed\n CA to create an new account\n LN to login to your Account")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 20)
        username = input("User_name: ")
        while True:
            print("TP to type your own password\n GP to generate your own password")
            password_choice = input().lower().strip()
            if password_choice == "tp":
                password = input("Enter Your Password\n")
                break
            elif password_choice == "gp":
                password = generate_password()
                break
            else:
                print("Incorrect Pasword")
        save_user(create_new_user(username, password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "ln":
        print('*' * 80)
        print("Enter your Username and Password to login")
        print("*"* 80)
        username = input("Enter Your Username")
        password = input("Enter your Password")
        login = login_user(username, password)
        if login_user == login:
            print(f"Welcome {username} to password generator")
            print("\n")
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credentials(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_account_details():
                print("Here's your list of acoounts: ")
                print('*' * 30)
                print('_'* 30)
                for account in display_account_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")




if __name__ == '__main__':
    passwordlocker()