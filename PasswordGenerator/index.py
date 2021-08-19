# from Password.interface import check_credendtials
# from Password.interface import passlocker
from passlock import User, Credentials

def create_new_user(username,password):
    new_user = User(username,password)
    return new_user

def save(self):
    User.save_user()

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



if __name__ == '__main__':
    passwordlocker()