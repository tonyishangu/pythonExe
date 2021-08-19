from passlock import User, Credentials

def create_new_user(username,password):
    new_user = User(username,password)
    return new_user