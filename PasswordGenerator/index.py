# from Password.interface import check_credendtials
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