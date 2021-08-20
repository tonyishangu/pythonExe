# from _typeshed import Self
import random
import string
import pyperclip

class User:
    user_list = []

    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def save_user (self):
        User.user_list.append(self)

    @classmethod
    def dispaly_user(cls):
        return cls.user_list

    def delete_user(self):
        User.user_list.remove(self)

class Credentials:
    credentials_list = []

    def __init__ (self, account,userName,password):
        self.account = account
        self.username = userName
        self.password = password

    def save_details(self):
        Credentials.credentials_list.append(self)

    def delete (self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    def generatePassword(stringLength=8):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))