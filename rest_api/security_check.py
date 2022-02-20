from user import User

users = [
    User(1, 'John', 'password'),
    User(2, 'Jerry', 'password'),
    User(3, 'Eric', 'password'),
]

# Build dictionary {username: user_obj}
usernames = {u.username:u for u in users}
# Build dictionary {userid: user_obj}
userids = {u.id:u for u in users}

def authenticate(username, password):
    # Check if username exists
    user = usernames.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    userid = payload['identity']
    return userids.get(userid, None)