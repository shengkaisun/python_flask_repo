from flask_bcrypt import Bcrypt

bycrypt = Bcrypt()

password = 'supersecretpassword'

print("---- Using Bycrypt -----")
hash = bycrypt.generate_password_hash(password)
print(hash)

check = bycrypt.check_password_hash(hash, 'wrongpassword')
print(check)

check = bycrypt.check_password_hash(hash, password)
print(check)

print("---- Using Werkzeug -----")
from werkzeug.security import generate_password_hash, check_password_hash

hash = generate_password_hash(password)
print(hash)
check = check_password_hash(hash, 'wrongpassword')
print(check)
check = check_password_hash(hash, password)
print(check)

