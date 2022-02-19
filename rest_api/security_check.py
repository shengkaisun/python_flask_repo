from user import User

users = [
    User(1, 'John', 'password'),
    User(2, 'Jerry', 'password'),
    User(3, 'Eric', 'password'),
]

usernames = {u.username for u in users}
userids = {u.id for u in users}

def authenticate(username, password):
    # Check if username exists
    user = usernames.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    userid = payload.get('identity', None)
    return userids.get(userid, None)