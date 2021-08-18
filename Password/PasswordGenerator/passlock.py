import random
import string
import pyperclip

class User:
    user_list = []

    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def saveUser (self):
        User.user_list.append(self)

    @classmethod
    def dispaly_user(cls):
        return cls.user_list

    def delete_user(self):
        User.user_list.remove(self)
